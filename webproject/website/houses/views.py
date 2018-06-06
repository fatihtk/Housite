from django.shortcuts import render
from . models import Houses
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms



def houses_list(request):
	house = Houses.objects.all().order_by('owner')
	return render(request,'Houses.html',{'houses':house})


def house_detail(request,house_name):
	#return HttpResponse(house_name)
	house = Houses.objects.get(house_name=house_name)
	return render(request, 'detail2.html',{'house':house})

@login_required(login_url = "/accounts/login/")
def house_create(request):
    if request.method =='POST':
        form = forms.CreateHouses(request.POST,request.FILES)
        if form.is_valid():
            #save house to db
            instance = form.save(commit=False)
            instance.save()
            return render(request, 'login.html')
    else:
        form = forms.CreateHouses()
    return render(request,"house_create.html",{'form':form})

def post(request):
    if request.method =='POST':
        form = forms.posts(request.POST,request.FILES)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.save()
            return render(request, 'contact.html')
    else:
        form = forms.posts()
    return render(request,"contact.html",{'form':form})
