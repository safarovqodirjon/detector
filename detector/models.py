from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Document(models.Model):
    # f_name = models.CharField(max_length=255)
    files = models.FileField(upload_to="documents/")

    def __str__(self):
        return f'{str(self.files).split(sep="/")[-1]}'

    def file_path(self):
        return f'{self.files.path}'

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'


# class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to='documents/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.id}'
#
#     class Meta:
#         verbose_name = 'Document'
#         verbose_name_plural = 'Documents'


class Products(models.Model):
    part_number = models.CharField(max_length=255, null=True, blank=True)
    dealer_name = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    on_stock = models.CharField(max_length=255, blank=True, null=True)
    delivery = models.IntegerField(blank=True, null=True)
    last_modified = models.DateTimeField()
    filename = models.CharField(null=True, blank=True, max_length=255)
    shape = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return f'{self.dealer_name}'


#
# class Dialer(models.Model):
#     name = models.CharField(max_length=255)


class FileNames(models.Model):
    filename = models.CharField(max_length=255)
    shape = models.CharField(max_length=255, null=True, blank=True)
    dealer_name = models.CharField(max_length=255, null=True, blank=True)
    filename2 = models.CharField(default=filename, max_length=255)


class UploadHistory(models.Model):
    filename = models.CharField(max_length=255)
    shape = models.CharField(max_length=255)
    uploaded_on = models.DateTimeField(blank=False, null=filename)
