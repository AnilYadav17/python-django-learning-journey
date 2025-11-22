from django.shortcuts import render

def home(request):
    # render takes the request and the template name (string).
    # pass the template name as 'home.html'
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def entry1(request):
    a = 10
    b = 25
    c = a+b
    print(c)
    return render(request,"entry1.html",{"c":c})

def entry11(request):
    a=20
    print(a)
    return render(request, "entry11.html", { "a":a })

def entry2(request):
    list1 = [1, 2, 3, 4, 5, 2, 8, 4, 10]
    print(list1)
    list1.append(20)
    print(list1)
    return render(request, "entry2.html", {"list1": list1})

def entry3(request):
    # if request.method=="POST":
    #      x = request.POST.get("n")
    if request.method=="GET":
     return render(request, 'entry3.html')
    else:
    #  x = request.POST.get("n")
    #  print("x", x)
    #  return render(request, 'entry3.html')
       x = request.POST.get("n")
       result = x
       print("result=", result)
       return render(request , "entry3.html" , { "result":result})
    

def entry4(request):
    #      x = request.POST.get("n")
    if request.method=="GET":
     return render(request, 'entry4.html',{"result":""})
    else:
        a = request.POST.get("a")
        b = request.POST.get("b")
        result = int(a)+int(b)
        print("result=", result)
        return render(request , "entry4.html" , { "result":result})
      
def entry5(request):
   if request.method == "GET":
      return render(request , 'entry5.html')
   else:
      p = request.POST.get("principle")
      r = request.POST.get("rate")
      t = request.POST.get("time")
      p = float(p)
      r = float(r)
      t = float(t)
      SI = (p * r * t) / 100
      return render(request, "entry5.html", {"SI": SI})