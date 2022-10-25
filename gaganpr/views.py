from django.shortcuts import render, HttpResponse
from gaganpr.models import contact, data
from django.contrib import messages
from django.db.models import Q 
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def myspace(request):
    return render(request, 'myspace.html')

def Contact(request):
    if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone') 
      desc = request.POST.get('desc')
      Contact = contact(name = name, email = email, phone = phone, desc = desc)
      Contact.save()
      messages.success(request, "Message Sent Successfully, Thanks For Contacting. ")
    return render(request, 'index.html')

def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'Gagan' and password == '1975':
            return render(request, 'data.html')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, 'myspace.html')


def Data(request):
    if request.method == "POST":
      dname = request.POST.get('dname')
      daddress = request.POST.get('daddress')
      dphone = request.POST.get('dphone')
      ddesc = request.POST.get('ddesc')
      Data = data(dname = dname, daddress = daddress, dphone = dphone, ddesc = ddesc)
      Data.save()
      messages.success(request, "Listing Posted Successfully")
    return render(request, 'data.html')


def listings(request):
    alldata= data.objects.all()
    context={'alldata': alldata}
    return render(request, "listings.html", context)

def search(request):
    query = request.GET['query']
    # allposts = data.objects.filter(Q(dname__icontains=query) | Q(dphone__icontains=query) | Q(daddress__icontains=query) | Q(ddesc__icontains=query))
    allpostsname = data.objects.filter(dname__icontains=query)
    allpostsphone = data.objects.filter(dphone__icontains=query)
    allpostsaddress = data.objects.filter(daddress__icontains=query)
    allpostsdesc = data.objects.filter(ddesc__icontains=query)
    allposts = allpostsname.union(allpostsphone, allpostsaddress, allpostsdesc)
    context = {'allposts' : allposts}
    return render(request, 'search.html', context)