from django.shortcuts import render
import datetime

def index(request):

    return render(request,
                  template_name="index.html",
                  context={"data": datetime.datetime.today()})
