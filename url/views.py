from django.shortcuts import render, redirect
from .forms import CreateUrlForm, CreateUserForm
from django.urls import reverse
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    form = CreateUrlForm(request.POST or None)
    code_string = ''
    shortcode = ''
    if request.method == "POST":
        form = CreateUrlForm(request.POST)
        if form.is_valid():

            ac_url = form.cleaned_data.get('actual_url')            
            code_string = form.cleaned_data.get('shortcode')
            shortcode = code_string
            # print('I will try to print path')
            # code_string =  request.build_absolute_uri(reverse('url.home')) +  code_string
            # print(code_string)
            # print('code string was not null')
            if models.Url.objects.filter(actual_url = ac_url).exists():
                prev_obj = models.Url.objects.get(actual_url=ac_url)
                shortcode = prev_obj.shortcode
                print("YES it exists " + shortcode)
            else:
                form.save()
            # form = CreateUrlForm()

    context = {'form': form, 'shortcode':shortcode,}
    return render(request,'home.html',context)

def URLRedirector(request, url):
    url_qs = models.Url.objects.get(shortcode=url)
    real_link = url_qs.actual_url
    print(real_link)
    return redirect(real_link)

def db_view(request):
    objects = models.Url.objects.all()
    context = {'objects' : objects}
    return render(request, 'database.html',context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('Username: ' + str(username))
        print('Password: ' + str(password))
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('url:home')
        else:
            messages.add_message(request, messages.INFO, 'Invalid Credentials')
    context = {}
    return render(request, 'login.html',context)

def register_view(request):
    form = CreateUserForm(request.POST or None)
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url:login')
    context = {'form' : form}
    return render(request, 'register.html',context)

def logout_view(request,*args,**kwargs):
    logout(request)
    return redirect('url:home')

def delete_view(request, id):
    obj = models.Url.objects.get(pk=id)
    obj.delete()
    return redirect('url:database')