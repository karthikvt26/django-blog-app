from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User 
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

import json

from .models import Author, Article

# Create your views here.

def userSignup(request):
    reqBody = json.loads(request.body)
    requiredFields = ['username', 'email', 'password']
    for field in requiredFields:
        if not field in reqBody or not reqBody[field]:
            return HttpResponse(json.dumps({'message': 'Required field not available ( username, password, email )' }), status=401)
    user = User.objects.create_user(reqBody['username'], reqBody['email'], reqBody['password'],)
    user.save()
    return HttpResponse('User successfully created. Please login to continue')

def userLogin(request):
    reqBody = json.loads(request.body)
    requiredFields = ['username', 'password']
    for field in requiredFields:
        if not field in reqBody or not reqBody[field]:
            return HttpResponse(json.dumps({'message': 'Required field not available ( username, password )' }), status=401)
    user = authenticate(request, username=reqBody['username'], password=reqBody['password'])
    if user is not None:
        login(request, user)
        login_response = {
            'token': request.session.session_key,
            'user_id': request.session['_auth_user_id'],
            'message': 'authenticated',
        }
        return HttpResponse(json.dumps(login_response), 'application/json')
    else:
        return HttpResponse('Invalid credentials!', status=401)


def inspectUser(request):
    if ( request.user.is_authenticated ):
        return HttpResponse('Logged in user: ' + request.user.username)
    else:
        return HttpResponse('User not logged in', status=403)

def getUserArticles(request):
    """
        Reads the user information provided by the session/auth middleware and returns the list of articles for that particular author
    """
    if ( not request.user.is_authenticated):
        return HttpResponse(json.dumps([]))

    if not request.user.id:
        return HttpResponse('Invalid user id', status=400)
    qs = Article.objects.filter(author_id=request.user.id)

    responseObjs = []

    for q in qs:
        rObj = {
            'title': q.title,
            'description': q.description,
            'author_id': q.author_id,
            'id': q.id,
        }
        responseObjs.append(rObj)
    return HttpResponse(json.dumps(responseObjs), 'application/json')

def getAuthorInfo(request):
    """
        Reads the user information provided by the session/auth middleware and returns the list of articles for that particular author
    """

    if ( not request.user.is_authenticated):
        return HttpResponse(json.dumps([]))

    if not request.user.id:
        return HttpResponse('Invalid user id', status=400)
    qs = Author.objects.filter(id=request.user.id)

    responseObjs = []

    for q in qs:
        rObj = {
            'name': q.name,
            'id': q.id,
        }
        responseObjs.append(rObj)
    return HttpResponse(json.dumps(responseObjs), 'application/json')

def getPublicArticles(request):
    """
        Returns all the articles where visibility_level = public
    """
    qs = Article.objects.filter(visibility_level='public')

    responseObjs = []

    for q in qs:
        rObj = {
            'title': q.title,
            'description': q.description,
            'author_id': q.author_id,
            'id': q.id,
        }
        responseObjs.append(rObj)
    return HttpResponse(json.dumps(responseObjs), 'application/json')


