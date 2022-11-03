from contextvars import Context
from django.shortcuts import render
from .models import Job

# Create your views here.


def job_list(request):
    job_list = Job.objects.all()
    
    Context={'jobs':job_list}
    
    return render(request,'job/job_list.html',Context)



def job_details(request , id):
    job_details = Job.objects.get(id = id)  
    Context={'job':job_details}
    
    return render(request,'job/job_details.html',Context)