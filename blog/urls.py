from django.urls import path
from . import views



app_name="blog"


urlpatterns = [
    path("", views.PostList.as_view(),name="post_list"),
    path("<slug:slug>", views.postDetail.as_view(), name="post_detail"),
    path("category/<str:slug>", views.postByCategory.as_view(), name="post_by_category"),
    path("tags/<slug:slug>", views.postByTags.as_view(), name="post_by_tags"),

]