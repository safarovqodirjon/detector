from django.contrib import admin
from .models import Document


# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    fields = ["files", ]
    list_display = ['id', 'files', ]


admin.site.register(Document, DocumentAdmin)
