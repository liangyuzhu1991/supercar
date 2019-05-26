# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect 
from django.urls import reverse
from django.template import loader
from random import randint

from .models import *
# Create your views here.
def  index(request):
    latest_car_list = Car.objects.order_by('speed')[:5]
    drivers=Driver.objects.all()
    template = loader.get_template('race/index.html')
    context={
      'lastest_car_list':latest_car_list,
      'extra_message': "hello have fun!",
      'drivers':drivers
    }#context is just a dictionary for the dataset that you are going to use
    return HttpResponse(template.render(context, request))

def detail(request,driver_id):
  #try:
  #  driver=Driver.objects.get(pk=driver_id)
  #except Driver.DoesNotExist:
  #  raise Http404("Driver does not exist")
  driver=get_object_or_404(Driver,pk=driver_id)
  try:
    driver.name=request.POST['name']
    driver.nickname=request.POST['nickname']
  except:
    return render(request,'race/detail.html',{'driver':driver})
  else:
    driver.save()
    return HttpResponseRedirect(reverse('race:detail',args=(driver_id)))
  
def start(request):
  race=Race()
  race.save()
  
  context={}
  
  max_speed=0
  all_drivers=Driver.objects.all()
  sitting_driver_id=randint(1,len(all_drivers))
  for driver in all_drivers:
    if driver.id==sitting_driver_id:
      context['sitting_driver']=driver
    else:
      race.drivers.add(driver)
      if driver.car.speed>max_speed:
        race.winner=driver
        max_speed=driver.car.speed
  race.save()
  context['race']=race
  context['race_drivers']=race.drivers.all()
  return render(request,'race/race.html',context)
