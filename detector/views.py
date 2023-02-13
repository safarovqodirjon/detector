from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, Http404
from .models import Document, FileNames, Products
import pandas as pd
import os
from django.conf import settings
from .modules.calculation import Calculation


# Create your views here.
def index(request):
    context = {
        'your_sheets': Products.objects.filter(
        ).values('dealer_name', 'shape', 'filename', 'last_modified').distinct()
    }
    return render(request, 'index.html', context=context)


def upload_files(request):
    if request.method == 'POST':
        if request.FILES:
            dc_dfs = Calculation.to_dc(request.FILES.getlist('myfiles'))
            if isinstance(dc_dfs, Exception):
                wrong = True
            else:
                wrong = False
            context = {
                'wrong': wrong,
                'dict_list': dc_dfs,
                'your_sheets': Products.objects.filter(
                ).values('dealer_name', 'shape', 'filename', 'last_modified').distinct()
            }
            return render(request, 'index.html', context=context)
    else:

        dc_dfs = FileNames.objects.all()
        for dc in dc_dfs:
            print(dc.filename, dc.shape)
        if isinstance(dc_dfs, Exception):
            wrong = True
        else:
            wrong = False

        context = {
            'wrong': wrong,
            'checked': False,
            'dict_list': dc_dfs,
            'your_sheets': Products.objects.filter(
            ).values('dealer_name', 'shape', 'filename', 'last_modified').distinct()
        }

        return render(request, 'index.html', context=context)


def load_to_db(request):
    objs = FileNames.objects.all()
    file_lst = [name.filename for name in objs]

    Calculation.load_to(file_lst)

    return redirect('detector:upload')


def see(request, id):
    path = FileNames.objects.values('filename').get(pk=id)['filename'].split(sep='.')[0] + '.csv'
    abs = os.path.join(settings.MEDIA_ROOT, f"documents/temp/")
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename={path}.xlsx'
    result = pd.read_csv(os.path.join(abs, path), nrows=10)
    result.drop(['filename', 'filename2', 'shape', 'dealer_name'], axis=1).to_excel(response, index=False)

    return response


def remove(request, id):
    try:
        path = FileNames.objects.values('filename').get(pk=id)['filename'].split(sep='.')[0] + '.csv'
        abs = os.path.join(settings.MEDIA_ROOT, f"documents/temp/{path}")
        os.remove(abs)
        FileNames.objects.get(pk=id).delete()
    except Exception as ex:
        pass
    return redirect('detector:upload')


def download(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename=all_files.xlsx'
    result = Calculation.download()
    result['last_modified'] = result['last_modified'].astype('str')
    result.to_excel(response, index=False)
    # result.head()
    return response


def detect(request):
    sel_main = request.POST.get('main_df')
    sel_drs = request.POST.getlist('names')
    sel_main_path = Document.objects.filter(pk=sel_main).first().file_path()
    main = pd.read_excel(sel_main_path)
    names = list()
    dfs = list()
    for item in sel_drs:
        cur_path = Document.objects.filter(pk=int(item)).first().file_path()
        name = str(cur_path.split(sep='/')[-1]).split(sep='.')[0]
        df = pd.read_excel(cur_path)
        names.append(name)
        dfs.append(df)

    res_dc = {names[i]: dfs[i] for i in range(len(names))}
    print(res_dc.keys())
    result = Calculation.merge_dfs(left_df=main, dc=res_dc)

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename=outputs.xlsx'
    result.to_excel(response, index=False)
    # result.head()
    return response
