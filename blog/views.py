from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import post,Category
from django.db.models import Count
from taggit.models import Tag
from django.db.models.query_utils import Q
# Create your views here.




class PostList(ListView):
    model=post
    paginate_by = 10

    

    


class postDetail(DetailView):
    model=post



    def get_context_data(self, **kwargs ): 
        context= super().get_context_data(**kwargs)
        context["categories"]=Category.objects.all().annotate(post_count=Count("post_category"))
        context["tags"]=Tag.objects.all()
        context["recent_posts"]=post.objects.all()[:3]
        return context




class postByCategory(ListView):
    model=post

    def get_queryset(self): 
        slug=self.kwargs['slug']   # عشان يجيب الslug
        object_list= post.objects.filter(
            Q(category__name__icontains=slug)
        )
        return object_list


class postByTags(ListView):
    model=post


    def get_queryset(self): 
        slug=self.kwargs['slug']   # عشان يجيب الslug
        object_list= post.objects.filter(
            Q(tags__name__icontains=slug)
        )
        return object_list