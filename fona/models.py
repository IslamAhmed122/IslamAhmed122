from typing import Reversible
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class web (models.Model):
    title=models.CharField(max_length=300,verbose_name=_("sitename"),null=True)
    logo=models.ImageField(verbose_name=_("logo"),upload_to="img/",null=True)
    homepage=models.CharField(max_length=100,verbose_name=_("Home"),null=True)
    About=models.CharField(max_length=100,verbose_name=_("About"),null=True)
    Services=models.CharField(max_length=100,verbose_name=_("Services"),null=True)
    Blog=models.CharField(max_length=100,verbose_name=_("Blog"),null=True)
    Contact=models.CharField(max_length=100,verbose_name=_("Contact"),null=True )
    Photo_Gallery=models.CharField(max_length=100,verbose_name=_("Photo"),null=True)
    name_ft = models.CharField(max_length=100, verbose_name=_("name"),null=True)
    title_ft = models.CharField(max_length=100, verbose_name=_("title"),null=True)
    description_ft = models.TextField(max_length=3000, verbose_name=_("description"),null=True)
    image_ft= models.ImageField(verbose_name=_("image"),upload_to="img/",null=True)
    fac_link=models.URLField(max_length=300, verbose_name=_("facbook"),null=True)
    twi_link=models.URLField(max_length=300, verbose_name=_("twitter"),null=True)
    gma_link=models.URLField(max_length=300, verbose_name=_("gmail"),null=True)
    ins_link=models.URLField(max_length=300, verbose_name=_("instgram"),null=True)
    yout_link=models.URLField(max_length=300, verbose_name=_("youtube"),null=True)
    crated_by=models.URLField(max_length=300, verbose_name=_("auther"),null=True)
    contect_us=models.CharField(max_length=300, verbose_name=_("contect"),null=True)
    phone=PhoneNumberField( verbose_name=_("phone"),null=True)
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True )
    


def __str__(self):
    return str(self.title)


def get_absolute_url(self):
        return Reversible('web', args=[str(self.id)])


def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(web,self).save(*args, **kwargs)  # save







