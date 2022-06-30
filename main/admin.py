from django.contrib import admin
from main import models
# Register your models here.

admin.site.register(models.Images)
admin.site.register(models.Containers)
admin.site.register(models.DockerAddresses)
