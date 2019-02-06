from django.shortcuts import render, get_object_or_404
from .models import job
import os
# Create your views here.
def home(request):
    jobs = job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})

def detail(request,job_id):
    job_detail= get_object_or_404(job,pk=job_id)
    return render(request,'jobs/detail.html',{'job':job_detail})

def bio(request):
    return render(request,'jobs/HemaDasari_Resume.html')
