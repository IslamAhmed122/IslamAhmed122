from django.contrib import admin
from setting import models

from setting.models import   imagelist,  section_blog, section_four, section_three, subservice

# Register your models here.


admin.site.register(models.imagelist)

admin.site.register(models.section_blog)
admin.site.register(models.section_four)
admin.site.register(models.section_three)
admin.site.register(models.subservice)
