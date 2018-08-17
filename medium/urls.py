from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.userSignup, name='signup'),
    path('login', views.userLogin, name='userLogin'),
    path('author/articles', views.getUserArticles, name='getUserArticles'),
    path('author/info', views.getAuthorInfo, name='getAuthorInfo'),
    path('articles', views.getPublicArticles, name='getPublicArticles'),
    path('validate_request', views.inspectUser, name='inspectUser'),
]
