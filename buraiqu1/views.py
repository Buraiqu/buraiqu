from django.shortcuts import render

# Create your views here.
def buraiqu_web(request):
    return render(request,'web_templates/wb.html')