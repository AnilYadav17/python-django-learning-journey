from django.shortcuts import render,redirect
from . import models
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage

def register(request):
    if request.method=="GET":
        return render(request, "registration.html")
    else:
        fullname = request.POST.get("fullname")
        gender = request.POST.get("gender")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        emailid = request.POST.get("emailid")
        pwd = request.POST.get("pwd")
        role = "student"

        res=models.mstuser(fullname=fullname, gender=gender, mobile=mobile, address=address, emailid=emailid, pwd=pwd, role=role)
        res.save()
        return render(request, "registration.html" )

def home(request):
    return render(request , 'index.html')

def login(request):
 if request.method=="POST":
  emailid=request.POST.get("emailid")
  pwd=request.POST.get("pwd")
  result=models.mstuser.objects.filter(emailid=emailid, pwd=pwd)

  if len(result)>0:
     print("Login success!")
     #for fetch rol value from database 
     role=result[0].role
     print("Role :" ,role)
     #for create session
     request.session["emailid"]=emailid
     request.session["role"]=role

     if role=="student":
        return redirect("/studenthome/")
     elif role=="admin":
        return redirect("/adminhome/")
     

  else:
    print("Invalid login credentials!")
  return render (request, 'login.html')
 else:
  return render (request, 'login.html')
 
def studenthome(request):
   return render(request, "studenthome.html")

def adminhome(request):
   return render(request, "adminhome.html")

def logout1(request):
   del request.session["emailid"]
   del request.session["role"]
   logout(request)
   return redirect('http://localhost:8000/')

def addcourse(request):
   if request.method=="GET":
      return  render(request, "addcourse.html")
   else:
      coursename=request.POST.get("coursename")
      courseduration=request.POST.get("courseduration")
      fees=request.POST.get("fees")
      coursedetail=request.POST.get("coursedetail")
      #for file upload ...........................
      courseicon=request.FILES["courseicon"]
      fs=FileSystemStorage()
      courseimg=fs.save(courseicon.name, courseicon)

      result = models.course(coursename=coursename,courseduration=courseduration,fees=fees,coursedetail=coursedetail,courseicon=courseicon)
      result.save()
      return  render(request, "addcourse.html")
   


def courselist(request):
    res=models.course.objects.all()
    return render(request, "courselist.html", {"res": res})

def addbatch(request):
   if request.method=="POST":
      batchtitle=request.POST.get("batchtitle")
      startdate=request.POST.get("startdate")
      facultyname=request.POST.get("facultyname")

      obj = models.batch(batchtitle=batchtitle, startdate=startdate , facultyname=facultyname)
      obj.save()
      return render(request, "addbatch.html")
      
   else:
      return render(request, "addbatch.html")
   
def batchlist1(request):
   res=models.batch.objects.all()
   return render(request , "batchlist1.html", {"res": res })



def studentlist(request):
   res=models.mstuser.objects.filter(role="student")
   return render(request, "studentlist.html", {"res":res})


def courselist1(request):
    res=models.course.objects.all()
    return render(request, "courselist1.html", {"res": res})


def batchlist2(request):
   res=models.batch.objects.all()
   return render(request , "batchlist2.html", {"res": res })


def viewprofile(request):
    emailid = request.session.get("emailid")

    if request.method == "POST":
        result = models.mstuser.objects.filter(emailid=emailid)
        return render(request, "viewprofile.html", {"result": result})

    # Handle GET request as well
    result = models.mstuser.objects.filter(emailid=emailid)
    return render(request, "viewprofile.html", {"result": result})

