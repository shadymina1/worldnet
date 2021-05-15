from django import forms
from mainapp.form import contactForm , signUpForm ,logInForm
from django.shortcuts import render
from django.core import serializers
from django.shortcuts import redirect
from .models import sender ,user
import json

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def ordering(request):
    if request.method == 'POST':
        submitted_form = signUpForm(request.POST) 
        if submitted_form.is_valid():
            note = "You have signd up "
            fname = submitted_form.cleaned_data['fname']
            lname = submitted_form.cleaned_data['lname']
            email = submitted_form.cleaned_data['email']
            cell = submitted_form.cleaned_data['email']
            address = submitted_form.cleaned_data['email']
            plan = submitted_form.cleaned_data['email']
            password = submitted_form.cleaned_data['password']
            member = user.objects.filter(email= email )
            if member:
                note = "You are already registered , please sign in"
                form = signUpForm()
                return render(request,'pages/ordering.html',{'signUpForm':form ,'note':note})
            else:    
                member = serializers.serialize('json',member)    
                user_data = user(firstName = fname, lastName = lname , email= email, password = password , cell=cell, address=address,plan=plan )
                user_data.save()
                email = submitted_form.cleaned_data['email']
                password = submitted_form.cleaned_data['password']
                member = user.objects.filter(email= email, password = password )
                if member:
                    member = serializers.serialize('json',member)
                    request.session['user'] = member
                    return redirect('/myorder')
    else:
        form = signUpForm()
        return render(request,'pages/ordering.html',{'signUpForm':form})


def login(request):
    if request.method == 'POST':
        submitted_form = logInForm(request.POST) # It can be named as we like
        if submitted_form.is_valid():
            note = "You have signd up"
            email = submitted_form.cleaned_data['email']
            password = submitted_form.cleaned_data['password']
            member = user.objects.filter(email= email, password = password )
            if member:
                member = serializers.serialize('json',member)
                request.session['user'] = member
                return redirect('/myorder')
            else:
                note = "Email and password do not match "
                form = logInForm()
                return render(request, 'pages/login.html',{'logInForm':form , 'note':note })
    else:
        form = logInForm()
        return render(request,'pages/login.html',{'logInForm':form})


def contact(request):
    if request.method =='POST':
        submitted_form = contactForm(request.POST or None) 
        if submitted_form.is_valid():
            note = 'Your message has been sent successfully!! '
            name = submitted_form.cleaned_data['name']
            cell = submitted_form.cleaned_data['cell']
            email = submitted_form.cleaned_data['email']
            message = submitted_form.cleaned_data['message']
            messanger = sender.objects.filter(Email = email)
            messanger = serializers.serialize('json',messanger)
            user_data = sender(name = name, cell = cell , Email= email, message = message )
            user_data.save()
            form = contactForm()
            return render(request,'pages/contact.html',{'contactForm':form, 'note':note})
    note = 0
    defaultnote="One of our team will be in contact with you shortly."
    form = contactForm()
    return render(request,'pages/contact.html',{'contactForm':form, 'note':note , 'defaultnote':defaultnote})

def myorder(request):
    try:
        mydata = json.loads(request.session['user'])        # <<<<====----
        return render(request,'pages/myorder.html', { 'first_name':mydata[0]}) 
    except:                                     
        return redirect('/plzlogin')

def plzlogin(request):
    return render(request,'pages/plzlogin.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return render(request,'pages/plzlogin.html')
    return redirect('/')    
    
