from django.urls import path
from .views import index, post, about, all_posts, category_posts

urlpatterns = [
    path('index/', index, name='index'),
    path('post/<int:post_id>/', post, name='post'), # str, int
    path('about/', about, name='about'),
    path('author-posts/<str:author_name>', all_posts, name='all_posts'),
    path('category-posts/<int:category_id>', category_posts, name='category_posts')
]