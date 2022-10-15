from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('recipe-post/<int:id>', views.recipe_post, name='recipe-post'),
    path('profile/<str:user>', views.profile, name='profile'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('recipe-finder/<str:diet>', views.recipe_finder, name='recipe-finder'),

    # Interacting with recipes
    path('recipe-comment/<int:post_id>', views.recipe_comment, name='recipe-comment'),
    path('recipe-favorite/<int:post_id>', views.recipe_favorite, name='recipe-favorite'),
]