from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/blog/1
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_pk>', views.blog_detail, name='blog_detail'),
    # http://localhost:8000/blog/type/1
    path('type/<int:blogs_with_type>', views.blogs_with_type, name='blogs_with_type'),
    path('author/<int:blogs_with_author>', views.blogs_with_author, name='blogs_with_author'),
]