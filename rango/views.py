# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response,render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from rango.forms import UserForm, UserProfileForm, DocumentForm, ParametresForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from rango.models import Document
from django.core.urlresolvers import reverse
from django.core.files.base import ContentFile
from django.core.files import File
import PIL
from PIL import Image
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__).decode('utf-8')))



def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            
    else:
        form = DocumentForm() 

    documents = Document.objects.all()

   
    return render_to_response(
        'rango/index.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
            'rango/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
       
        return render(request, 'rango/login.html', {})
    
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rango/')

def list(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            
        else:
            return HttpResponse("You have to select a file")

    documents = Document.objects.all().last()
   
    return render_to_response(
        'rango/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def parametres(request):
    x = request.POST['x']
    position_x = int(x) 
    y = request.POST['y']
    position_y = int(y) 
    ang = request.POST['angle']
    angle = int(ang) 
    w = request.POST['width']
    width = int(w) 
    h = request.POST['height']
    height = int(h) 
    addr = request.POST.get('address')
    
    documents = Document.objects.all().last()
    filepath = documents.docfile.url
    basewidth = 600
    im1 = Image.open(BASE_DIR+filepath)
    wpercent = (basewidth / float(im1.size[0]))
    hsize = int((float(im1.size[1])*float(wpercent)))
    im1 = im1.resize((basewidth,hsize))
    im2 = Image.open(BASE_DIR+addr)
    im2 = im2.resize((width,height)).rotate(-angle, expand=1)
    im1.paste(im2, (position_x,position_y),im2)
    im1.save(BASE_DIR+filepath)
    form = DocumentForm(request.POST, request.FILES)
    return render_to_response(
        'rango/list.html',
        {'documents': documents},
        context_instance=RequestContext(request)
    )

