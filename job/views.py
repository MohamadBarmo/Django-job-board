from django.shortcuts import render ,redirect
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm ,JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter


# Create your views here.

def job_list(request):
    job_list=Job.objects.all()

     ##filters 
    myfilter=JobFilter(request.GET,queryset=job_list)
    job_list=myfilter.qs

    paginator = Paginator(job_list, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    #print(job_list)
    page_obj = paginator.get_page(page_number)


   
    context={"jobs":page_obj,"myfilter":myfilter} #name in template 
    return render(request,'job/job_list.html',context)






#def job_details(request,id):
  #  job_detail=Job.objects.get(id = id)
 #   context={"job":job_detail} #name in template 
  #  return render(request,'job/job_detail.html',context)


def job_details(request,slug):
    job_detail=Job.objects.get(slug = slug)
    if request.method=='POST':
        form=ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job_detail
            myform.save()
            print("Done")
    else:
        form=ApplyForm()
    #context={"job":job_detail} #name in template 
    context={"job":job_detail,'form1':form} #name in template 
    return render(request,'job/job_detail.html',context)

@login_required
def add_job(request):
    if request.method=='POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()
    return render(request,'job/add_job.html',{'form1':form})

