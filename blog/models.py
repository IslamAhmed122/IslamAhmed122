from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User 

# Create your models here.
class post (models.Model):
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    tags = TaggableManager()
    image = models.ImageField(upload_to="post/")
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=15000)
    category = models.ForeignKey("Category",related_name="post_category",on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True)




def save(self,*args,**kwargs):
    if not self.slug:
        self.slug=slugify(self.title)
    super(post, self).save(*args,**kwargs)


def __str__(self):
    return str(self.title)



def get_absolute_url(self):
    return reverse("blog:post_detail",kwargs={"slug":self.slug})



class Category(models.Model):
    name = models.CharField(max_length=50)




    
def __str__(self):
    return str(self.name)