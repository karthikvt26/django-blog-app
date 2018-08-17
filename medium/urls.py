from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.userSignup, name='signup'),
    path('login', views.userLogin, name='userLogin'),
    path('resolve_token', views.inspectUser, name='inspectUser'),
    path('author/articles', views.getUserArticles, name='getUserArticles'),
    path('author/info', views.getAuthorInfo, name='getAuthorInfo'),
    path('articles', views.getPublicArticles, name='getPublicArticles'),
]
