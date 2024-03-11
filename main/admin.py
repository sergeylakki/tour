from django.contrib import admin
from main import models
from django.forms.widgets import Textarea
from django.db import models as type_models
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        type_models.TextField: {'widget': CKEditorUploadingWidget},
    }


admin.site.register(models.Client, MyModelAdmin)
admin.site.register(models.AboutUs, MyModelAdmin)
admin.site.register(models.Author, MyModelAdmin)
admin.site.register(models.Event, MyModelAdmin)
admin.site.register(models.CategoryEvent, MyModelAdmin)
admin.site.register(models.EventCarousel, MyModelAdmin)
admin.site.register(models.EventEat, MyModelAdmin)
admin.site.register(models.MainData, MyModelAdmin)
admin.site.register(models.IndexCarousel, MyModelAdmin)
admin.site.register(models.EventProgram, MyModelAdmin)
# Register your models here.
