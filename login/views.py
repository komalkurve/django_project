from django.db import connection
from django.shortcuts import render
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from models import Twit
from tweet_meter import Tweet_final


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )

@csrf_protect
def Search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            print form.cleaned_data['word']
        # keyword =  request.POST['search']


        return HttpResponse(html)

    else:
            return render(request, 'home.html')
        # if form.is_valid():
        #     print form.cleaned_data['keyword']

    # else:
    #     form = SearchForm()
    # return render_to_response('/map.html', context_instance=RequestContext(request))





def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def home(request):
    return render(request,
    'home.html',
    )



# Create your views here.
