from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import mimetypes
from django.http import StreamingHttpResponse
# import WSGIREF
from wsgiref.util import FileWrapper
from django.http import HttpResponse
import os
# Create your views here.

def home(request):
    return render(request,'index.html')
def abt(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def con(request):
    return render(request, 'contact.html')
def log(request):
    return render(request, 'login.html')

def home2(request):
    return render(request, 'home2.html')

def mech_home(request):
    return render(request, 'mech_home.html')

def contact2(request):
    return render(request, 'mech_contact.html')

def book(request):
    return render(request,'booking.html')

def signupuser(request):
    if request.method=='POST':
        name=request.POST['name']
        mobnum=request.POST['phone']
        mail=request.POST['email']
        usrname=request.POST['username']
        pas=request.POST['password']
        d=users.objects.create(name=name,number=mobnum,email=mail,username=usrname,password=pas)
        d.save()
        messages.success(request,"Successfully registered")
        return render(request,'login.html')

def signupmech(request):
    if request.method=='POST':
        name=request.POST['name']
        mobnum=request.POST['phone']
        mail=request.POST['email']
        usrname=request.POST['username']
        pas=request.POST['password']
        wrkshopname=request.POST['wrkshpname']
        wrkshoploc=request.POST['location']
        wrkshoplicense=request.POST['license']
        licenseimg=request.FILES['proof']
        d=mechanic.objects.create(name=name,number=mobnum,email=mail,username=usrname,
        password=pas, workshop_name=wrkshopname,
        workshop_location=wrkshoploc,workshop_license=wrkshoplicense,license_img=licenseimg,status = 'pending')
        d.save()
        messages.info(request,"Waiting for Approval !")
        return render(request,'login.html')


def profile(request):
    if 'id' in request.session:
        a=request.session['id']
        data=mechanic.objects.filter(username=a)
        if data:
            d = book_service.objects.filter(status='pending')
            for i in d:
                print(i.status)
            return render(request,'mech_home.html',{'data':d})
        else:
            return render(request, 'home2.html')
    else:
        return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        name=request.POST['usernamelog']
        pswd=request.POST['passwordlog']
        data=users.objects.filter(username=name)
        d=mechanic.objects.filter(username=name)
        if data:
            data1 = users.objects.get(username=name)
            if data1.password == pswd:
                request.session['id'] = name
                return redirect(profile)
            else:
                messages.info(request, 'invalid username or password')
                return render(request,'login.html')
        elif d:
            data1 = mechanic.objects.get(username=name)
            if data1.password == pswd:
                if data1.status=='pending':
                    messages.info(request, "Waiting for Approval!")
                    return render(request, 'login.html')

                else:
                    request.session['id'] = name
                    return redirect(profile)
            else:
                messages.info(request, 'invalid username or password')
                return render(request, 'login.html')
        else:
            messages.info(request, 'invalid username or password')
            return render(request,'login.html')

def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return render(request,'index.html')

def bk_service(request):
    if request.method == 'POST':
        service=request.POST['serv']
        name=request.POST['name']
        vehicle_num=request.POST['vehi']
        date=request.POST['setTodaysDate']
        loc=request.POST['location']
        msg=request.POST['message']
        status='pending'
        d = book_service.objects.create(service=service,name=name,
        vehicle_num=vehicle_num,date=date,location=loc,msg=msg,status=status,username=request.session['id'])
        d.save()
        messages.info(request, "Waiting for Mechanic !")
        return render(request,'home2.html')

def bk_service1(request):
    if request.method == 'POST':
        service=request.POST['serv']
        name=request.POST['name']
        vehicle_num=request.POST['vehi']
        date=request.POST['setTodaysDate']
        loc=request.POST['location']
        msg=request.POST['message']
        status='pending'
        d = book_service.objects.create(service=service,name=name,
        vehicle_num=vehicle_num,date=date,location=loc,msg=msg,status=status,username=request.session['id'])
        d.save()
        messages.info(request, "Waiting for Mechanic !")
        return render(request,'booking.html')

def accept_service(request,name):
    d = book_service.objects.filter(pk=name)
    book_service.objects.filter(pk=name).update(status='accept')
    return render(request, 'mhome_accept.html', {'data': d})

def reject_service(request,name):
    book_service.objects.filter(pk=name).update(status='reject')
    return redirect(profile)


def work_complete(request,name):
    book_service.objects.filter(pk=name).update(status='complete')
    return redirect(profile)

def adminlog(request):
    return render(request,'admin_log.html')

def admin_profile(request):
    if 'id' in request.session:
        d = mechanic.objects.filter(status='pending')
        d1=mechanic.objects.filter(status='approve')
        return render(request,'admin_home.html',{'data':d , 'data1':d1})


def login_admin(request):
    if request.method == 'POST':
        name=request.POST['adminlogin']
        pswd=request.POST['adminpass']
        data=admin_log.objects.filter(admin_name=name)
        if data:
            data1 = admin_log.objects.get(admin_name=name)
            if data1.admin_pass == pswd:
                request.session['id'] = name
                return redirect(admin_profile)
            else:
                messages.info(request, 'invalid username or password')
                return render(request,'admin_log.html')
        else:
            messages.info(request, 'invalid username or password')
            return render(request, 'admin_log.html')

def logout_admin(request):
    if 'id' in request.session:
        request.session.flush()
        return render(request,'index.html')

def admin_con(request):
    d=user_contact.objects.all()
    d1=mech_contact.objects.all()
    return render(request,'admin_contact.html',{'data':d , 'data1':d1})

def download_file(request,f_name):
    fl_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = f_name
    filepath = fl_path + '/media/' + filename
    thefile=filepath
    filename=os.path.basename(thefile)
    chunk_size=8192
    response=StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
                                   content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Length']=os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment; filename=%s" % filename
    return response

def reject_mech(request,name):
    mechanic.objects.filter(pk=name).delete()
    return redirect(admin_profile)

def acc_mech(r,id):
    mechanic.objects.filter(pk=id).update(status='approve')
    return redirect(admin_profile)

def del_mech(request):
    return render(request,'delete_mech.html')

def mech_del(request):
    if request.method == 'POST':
        usrname=request.POST['uname']
        passwd=request.POST['pswd']
        d = mechanic.objects.filter(username=usrname)
        if d:
            data1 = mechanic.objects.get(username=usrname)
            if data1.password == passwd:
                mechanic.objects.filter(username=usrname).delete()
                return render(request,'index.html')
            else:
                messages.info(request, 'invalid username or password')
                return render(request,'delete_mech.html')
        else:
            messages.info(request, 'invalid username or password')
            return render(request, 'delete_mech.html')
    else:
        return render(request,'delete_mech.html')


def user_contactfun(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        d=user_contact.objects.create(username=uname,user_email=email,subject=subject,message=message)
        d.save()
        messages.info(request, "Message send!We will contact You shortly.")
        return render(request,'contact.html')
def responded(request,name):
    user_contact.objects.filter(pk=name).delete()
    return redirect(admin_con)

def mech_contactfun(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        d=mech_contact.objects.create(username=uname,user_email=email,subject=subject,message=message)
        d.save()
        messages.info(request, "Message send!We will contact You shortly.")
        return render(request,'mech_contact.html')

def mech_responded(request,name):
    mech_contact.objects.filter(pk=name).delete()
    return redirect(admin_con)

def update_mech(request):
    return render(request,'update_mech.html')

def mech_update(request):
    if request.method == 'POST':
        usrname = request.POST['uname']
        passwd = request.POST['pswd']
        d = mechanic.objects.filter(username=usrname)
        if d:
            data1 = mechanic.objects.get(username=usrname)
            if data1.password == passwd:
                name=request.POST['name']
                phone=request.POST['phone']
                email=request.POST['email']
                usern=request.POST['username']
                passwrd=request.POST['password']
                wrkshpname=request.POST['wrkshpname']
                location=request.POST['location']
                license=request.POST['license']
                l_img=request.FILES['proof']
                mechanic.objects.update(name=name,number=phone,email=email,username=usern,password=passwrd,
                workshop_name=wrkshpname,workshop_location=location,workshop_license=license,license_img=l_img)
                messages.info(request, "Profile Updated successfully!")
                return render(request, 'update_mech.html')
            else:
                messages.info(request, "Incorrect Username or Password!")
                return render(request, 'update_mech.html')

        else:
            return render(request, 'update_mech.html')

def cancel_work(request,id):
    book_service.objects.filter(pk=id).update(status='cancel')
    return redirect(usrbk_details)

def rebook(request,id):
    book_service.objects.filter(pk=id).update(status='pending')
    return redirect(usrbk_details)

def usrbk_details(request):
    pending_work=[]
    accepted_work=[]
    completed_work=[]
    cancelled_work=[]
    d = book_service.objects.filter(status='pending')
    for i in d:
        if i.username==request.session['id']:
            pending_work.append(i)

    d1 = book_service.objects.filter(status='accept')
    for i in d1:
        if i.username==request.session['id']:
            accepted_work.append(i)

    d2 = book_service.objects.filter(status='complete')
    for i in d2:
        if i.username==request.session['id']:
            print(completed_work)
            completed_work.append(i)

    d3 = book_service.objects.filter(status='cancel')
    for i in d3:
        if i.username==request.session['id']:
            print(cancelled_work)
            cancelled_work.append(i)

    return render(request,'user_booking_details.html',
                {'data':pending_work,'data1':accepted_work,'data2':completed_work,'data3':cancelled_work})
