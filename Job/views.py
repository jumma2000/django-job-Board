from django.shortcuts import render

# Create your views here.


def job_list(request):
    return render(request,'job/index.html')

def job_detail(requset,id):
    pass
