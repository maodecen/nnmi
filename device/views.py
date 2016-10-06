from django.shortcuts import render
from device.forms import nodeForm

def index(request):
    return render(request,'device/index.html',{})

def device (request):
    return render (request, 'device/device_page.html',{})

def nodeAction (request):
    if request.method == 'GET' :
        form = nodeForm()

    else:

        form = nodeForm(request.POST)

    return render(request, 'device/device_page.html', {'form':form,})
