def get_list():
    faro_list = ['Artikelnummer',
                 'Bezeichnung',
                 'Warengruppe',
                 'EAN',
                 'Herstellernummer',
                 'Lieferbar',
                 'Preis',
                 'Verpackung',
                 'Bildname']

    convena_list = ['ItemNo', 'ProductPartNo',
                    'ProductTitle', 'Price',
                    'AvailableInventory']

    twoS = ['Part number',
            'Part description',
            'Part category',
            'Status',
            'Quality',
            'On stock',
            'Price ex tax',
            'Packaged quantity',
            'Max order quantity']

    apex = [
        'Unnamed: 0',
        'Unnamed: 1',
        'Unnamed: 2',
        'Unnamed: 3',
        'Unnamed: 4',
        'Unnamed: 5',
        'Unnamed: 6',
        'Unnamed: 7',
    ]

    dict_dealer = {
        '2S': twoS,
        'convena': convena_list,
        'faro': faro_list,
        'apex': apex,
    }

    return dict_dealer
