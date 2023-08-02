from django.shortcuts import render
from django.views import View
import smtplib
import os 
from django.http import FileResponse

from .models import ProjectStorage, MySkill, MyUpdateContact
# Create your views here.
class HomeView(View):

    def get(self, request):
        contactdata = MyUpdateContact.objects.all()[0]
        return render(request, "site/index.html", {
            "data": contactdata
        })
    

class MyProjectView(View):
    
    def get(self, request):
        latest = ProjectStorage.objects.order_by('date')

        return render(request, "site/My_projects.html",{
            "latest": latest,
        })
    

class AboutView(View):

    def get(self, request):
        backend = MySkill.objects.filter(type="backend")
        frontend = MySkill.objects.filter(type="frontend")
        other = MySkill.objects.filter(type="other")
        deploy = MySkill.objects.filter(type="deploy")
        python = MySkill.objects.filter(type="python")

        return render(request, "site/about.html",{
            "backend": backend,
            "frontend": frontend,
            "other": other,
            "deploy": deploy,
            "python": python
        })
    


class ContactView(View):
    def get(self, request):
        data = MyUpdateContact.objects.all()[0]
        return render(request, "site/contact.html",{
            "data": data
        }) 
    
    def post(self, request):
        data = MyUpdateContact.objects.all()[0]
        user_submitt = request.POST
        
        if user_submitt['Name'] == '' or user_submitt['Email_submit'] == '' or user_submitt['Message'] == '':
            return render(request, "site/contact.html",{
                "errors_title": "OPS, SOMETHING WENT WRONG!",
                "errors_text" : "Be sure to not leave with empty field or invalid value!",
                "data" : data
            })

        else:
            token = data.stmplib_token
            email_smtlib = data.email

            nome = str(request.POST["Name"])
            email = str(request.POST["Email_submit"])
            subject = str(request.POST["Subject"])
            message = str(request.POST["Message"])

            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=email_smtlib, password=token)
            connection.sendmail(from_addr=email_smtlib,to_addrs=email_smtlib, msg="Subject: "+ subject +"!\n\nCiao sono " + nome +"\nla mia email: " + email + ".\n" + message)
            connection.close()

            return render(request, "site/contact.html",{
                "success": "success",
                "data" : data
            })
    

def download_file(request):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/style/includes/cv.pdf')
    # Replace 'your_file_name.ext' with the actual name of your file
    file_name = os.path.basename(file_path)
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response
