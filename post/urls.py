from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name="all_posts"),
    path('create', views.create_post, name="create_post"),
    path('<int:post_id>', views.single_post, name="single_post")
]
