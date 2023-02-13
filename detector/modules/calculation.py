import pandas as pd
import os
from django.conf import settings
from sqlalchemy import create_engine
import datetime
from detector.models import FileNames, Products
from .list import get_list

# engine = create_engine(f'sqlite:///{settings.DATABASES["default"]["NAME"]}', echo=False)


# engine = create_engine("postgresql+psycopg2://yimpwzehvxdnpd:1230e673eef1483094982314c43771209f4aec1193de94b180e5dcbe3a55435c@ec2-3-248-121-12.eu-west-1.compute.amazonaws.com:5432/dbjulh0nu26mt8", echo=False)
engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/detectordb", echo=False)


class Calculation:
    @staticmethod
    def merge_dfs(left_df, dc):
        left_df.rename({'Model': 'Part number'}, axis=1, inplace=True)

        # with pd.ExcelWriter(os.path.join(settings.MEDIA_ROOT, 'file_output.xlsx')) as writer:
        for name, df in dc.items():
            df['Part number'] = df['Part number'].astype('object')
            left_df = left_df.merge(df, on='Part number', how='left', )
        # result = pd.read_excel(os.path.join(settings.MEDIA_ROOT, 'file_output.xlsx'))
        return left_df

    @staticmethod
    def to_dc(files):
        df_lst, all_dfs = list(), list()
        for file in files:
            format = str(file.name).split(sep='.')
            try:
                if format[-1] == 'xlsx':
                    df = pd.read_excel(file)
                elif format[-1] == 'csv':
                    try:
                        df = pd.read_csv(file, sep=';', encoding='unicode_escape')
                    except Exception as ex:
                        df = pd.read_csv(file, sep=';', encoding='utf-8')
                else:
                    raise Exception('WrongFormant')
            except Exception as ex:
                return ex

            col_list = list(df.columns)
            if get_list()['faro'] == col_list:
                dialer_name = 'faro'
            elif get_list()['2S'] == col_list:
                dialer_name = '2S'
            elif get_list()['convena'] == col_list:
                dialer_name = 'convena'
            elif col_list == get_list()['apex']:
                dialer_name = 'apex'
            else:
                dialer_name = 'unknown'

            try:
                df.insert(loc=0, column='shape', value=f'{df.shape}')
                df.insert(loc=0, column='filename', value=f'{file.name}')
                df.insert(loc=0, column='filename2', value=f'{str(file.name).split(sep=".")[0] + ".csv"}')
                df.insert(loc=0, column='dealer_name', value=f'{dialer_name}')
            except Exception as ex:
                df['shape'] = str(df.shape)
                df['filename'] = str(file.name)
                df['filename2'] = str(file.name).split(sep=".")[0] + ".csv"
                df['dealer_name'] = str(dialer_name)
                print(df['dealer_name'])
            sep = '.'
            df.to_csv(
                f'{os.path.join(settings.MEDIA_ROOT, f"documents/temp/{str(file.name).split(sep=sep)[0]}.csv")}',
                index=False)
            all_dfs.append(df)
            df = df.head(1)

            df_lst.append(df)

            excel = pd.concat(df_lst)

            cols = [i for i in excel]

            FileNames.objects.all().delete()
            # queryset = [dict(zip(cols, i)) for i in excel.values]
            for index, row in excel.iterrows():
                model = FileNames()
                model.filename = row['filename']
                model.shape = str(row['shape'])
                model.dealer_name = row['dealer_name']
                model.save()

        return FileNames.objects.all()

    @staticmethod
    def load_to(filelst):
        data_list = list()
        edit_dict = {
            'Part number': 'part_number',
            'Product Code': 'part_number',
            'ProductPartNo': 'part_number',
            'Herstellernummer': 'part_number',
            'dealer_name': 'dealer_name',
            'Price ex tax': 'price',
            'Preis': 'price',
            'Euro Price': 'price',
            'Price': 'price',
            'On stock': 'on_stock',
            'Quantity': 'on_stock',
            'AvailableInventory': 'on_stock',
            'Lieferbar': 'on_stock',
            'Part description': 'description',
            'Bezeichnung': 'description',
            'shape': 'shape',
            'filename': 'filename',

        }
        statndard = [*set(x for x in edit_dict.values())]
        sep = '.'
        for file in filelst:
            df = pd.read_csv(
                f'{os.path.join(settings.MEDIA_ROOT, f"documents/temp/{str(file).split(sep=sep)[0]}.csv")}')
            if df['dealer_name'].iloc[0] == 'apex':
                shape, filename, dealer_name = df['shape'].iloc[0], df['filename'].iloc[0], df['dealer_name'].iloc[0]
                df.columns = df.iloc[1]
                lsts = ['SUMSUNG', 'XIAOMI', 'HUAWEI'
                                             'HUAWEI BATTERY COVER', 'APPLE IPHONE', 'Product Name']
                for lst in lsts:
                    df = df[df["Product Name"].str.contains(f"{lst}") == False]
                df = df.iloc[0::, 4:9]
                df['shape'], df['filename'], df['dealer_name'] = shape, filename, dealer_name
            for k, v in edit_dict.items():
                df.rename({f'{k}': f'{v}'}, axis=1, inplace=True)
            if df['dealer_name'].any() != 'unknown':
                try:
                    data_list.append(df[[colname for colname in edit_dict.values()]])
                except KeyError as ex:
                    for col in ['dealer_name', 'delivery', 'description']:
                        try:
                            df.insert(loc=0, column=f'{col}', value=None)
                        except Exception as ex:
                            pass
                    df = df[statndard]

                    data_list.append(df[[colname for colname in edit_dict.values()]])
            dataframes = pd.concat(data_list)
            dataframes['last_modified'] = datetime.datetime.now()
            dataframes.to_sql('detector_products', engine, if_exists='append', index=False, index_label=None,
                              method=None)

            df_from_db = pd.read_sql_table(con=engine, table_name='detector_products')
            uniq = df_from_db.sort_values('last_modified').drop_duplicates(subset='part_number')
            Products.objects.all().delete()

            uniq.to_sql('detector_products', engine, if_exists='replace', index=False, index_label=None, method=None)
        else:
            pass
        return uniq

    @staticmethod
    def download():
        return pd.read_sql_table(con=engine, table_name='detector_products')
