from django.urls import path
from .views import *

app_name = 'detector'

urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload_files, name='upload'),
    path('check/<int:id>/', see, name='see'),
    path('remove/<int:id>/', remove, name='remove'),
    path('upload/loaddb', load_to_db, name='load'),
    path('detect/', detect, name='detect'),
]
