
from django.shortcuts import render
from.models import OurPlaces
from.models import People
# Create your views here.
def demo(request):
    obj = OurPlaces.objects.all()
    ppl = People.objects.all()
    return render(request,"index.html",{'result':obj,'result1':ppl})