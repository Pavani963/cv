from django.shortcuts import render
from pdf.models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.


def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        c_o = request.POST.get("c_o","")
        degree = request.POST.get("degree","")
        grade = request.POST.get("school","")
        university = request.POST.get("university","")
        work_experience= request.POST.get("work_experience","")
        skills = request.POST.get("skills","")

        profile = Profile(name=name,email=email,phone=phone,c_o=c_o,degree=degree,grade=grade,university=university,work_experience=work_experience,skills=skills)
        profile.save()


    return render(request,'pdf/accept.html')

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile':user_profile})
    options ={
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] ='attachment'
    filename = "resume.pdf"
    return response


def list(request):
    p = Profile.objects.all()
    context ={
     'p':p
    }
    return render(request,'pdf/list.html',context)
