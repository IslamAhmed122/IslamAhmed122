from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class imagelist(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"),null=True)
    image=models.ImageField(verbose_name=_("image"),upload_to="img/",null=True)
    video=models.FileField(verbose_name=_("video"),upload_to="vid/",null=True,blank=True)
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True   )
    

      


def __str__(self):
    return self.name


def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(imagelist,self).save(*args, **kwargs)



class subservice(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"),null=True)
    description = models.TextField(max_length=3000, verbose_name=_("description"),null=True)
    button_name=models.CharField(max_length=100, verbose_name=_("button_name"),null=True)
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True   )



def __str__(self):
    return self.name


def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(subservice,self).save(*args, **kwargs)


def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])



class section_three(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"),null=True)
    title = models.CharField(max_length=100, verbose_name=_("title"),null=True)
    description = models.TextField(max_length=3000, verbose_name=_("description"),null=True)
    image = models.ImageField(verbose_name=_("image"),upload_to="img/",null=True)
    button = models.CharField(max_length=100, verbose_name=_("button"),null=True)
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True   )
    

def __str__(self):
    return self.name

def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(section_three,self).save(*args, **kwargs)



class section_four(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"),null=True)
    title = models.CharField(max_length=100, verbose_name=_("title"),null=True)
    description = models.TextField(max_length=3000, verbose_name=_("description"),null=True)
    image = models.ImageField(verbose_name=_("image"),upload_to="img/",null=True)
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True   )


def __str__(self):
    return self.name

def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(section_three,self).save(*args, **kwargs)




class section_blog(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("name"),null=True)
    title = models.CharField(max_length=100, verbose_name=_("title"),null=True)
    description = models.TextField(max_length=3000, verbose_name=_("description"),null=True)
    image = models.ImageField(verbose_name=_("image"),upload_to="img/",null=True)
    slug=models.SlugField(verbose_name=_("url"),null=True,blank=True   )


def __str__(self):
    return self.name

def save(self, *args, **kwargs):  # new
    if not self.slug:
     self.slug = slugify(self.title)
    return super(section_blog,self).save(*args, **kwargs)







