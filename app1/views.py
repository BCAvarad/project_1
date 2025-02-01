from django.shortcuts import render ,redirect ,HttpResponse
from app1.models import *
# Create your views here.
def demo(request):
    return render(request, "index.html")

def regi(request):
      return render(request, "index.html")

def register(request):
    if request.method == "POST":
        
        fname = request.POST['name']
        age = request.POST['age']
        s_class = request.POST['class']
        gender = request.POST['gender']
        username = request.POST['userid']
        password = request.POST['password']
        image = request.FILES['pic']
        role = request.POST['role']
        # user pahilech ahe ka te pahu
        user = Student.objects.filter(user_id=username)

        if user :
            sandesh = "student is already exist!!"
            return render(request, "index.html",{"key": sandesh})
        else:
            cpassword = request.POST['cpassword']

            if cpassword == password :
                s = Uesrmaster.objects.create(role = role,password = password)
                std = Student.objects.create(s_id = s , Name=fname,age=age,gender=gender,S_class=s_class,profile_pic=image,user_id=username,Password=password)
                sandesh = "student is successfully registered!!"
                return render(request,"login.html",{"key":sandesh})
            else:
                sandesh = "password and  conform password not match!!"
                return render(request, "index.html",{"key":sandesh})
            
def login(request):
    return render(request,"login.html")
def sdashbord(request):
        return render(request,"deashbord.html")
def std_login(request):
    if request.method == "POST":
        
        role= request.POST['role']
        username= request.POST['userid']
        password= request.POST['password']

        if role == "student":

            try:

                user = Student.objects.get(user_id =username)
            except :
                sandesh = "username is not valid!!"
                return render(request, "login.html",{"key":sandesh})
            if user:
                if user.Password == password:
                    # ata ithe apan session pa sun data ghenar ahet 
                    profile_img = Student.objects.get(user_id=username)
                    request.session['sprofile_pic'] = profile_img.profile_pic.url
                  #  request.session['s_id'] = user.s_id
                    request.session['sName'] = user.Name

                    request.session['sage'] = user.age
                    request.session['S_class'] = user.S_class
                    return render(request,"deashbord.html")
                else:
                    sandesh = " password is wrong!!!"
                    return render(request, "login.html",{"key":sandesh})
            else:
                sandesh = "user is not register !!"

                return render(request,"index.html",{"key":sandesh})
        elif role == "teacher":
            try:
                user = Teacher.objects.get(user_id =username)
            except:
                sandesh = "username is not valid!!"
                return render(request, "login.html",{"key":sandesh})
            if user:
                if user.Password == password:
                    # ata ithe apan session pa sun data ghenar ahet
                    profile_img = Teacher.objects.get(user_id=username)
                    request.session['tprofile_pic'] = profile_img.Teacher_pic.url
                    request.session['tName'] = user.Name
                    request.session['tage'] = user.age
                    request.session['t_class'] = user.T_class
                    return render(request,"tdashbord.html")
                else:
                    sandesh = " password is wrong!!!"
                    return render(request, "login.html",{"key":sandesh})
            



def s_logout(request):
     if 'profile_pic' 'Name' 'age' 'S_class' in request.session:
         
        del request.session['profile_pic']
        del request.session['Name']
        del request.session['age']
        del request.session['S_class']
     return render(request,"login.html")

def showresult(request):
    return render(request,"sresult.html")

#teacher function suru zale


def tdashbord(request):
    return render(request,"tdashbord.html")

def tclass(request):
    return render(request,"tclass.html")

def tstudent(request):
    return render(request,"tstudent.html")

def tresult(request):
    return render(request,"tresult.html")

def tregister(request):
    return render(request,"tregister.html")



def tfregister(request):
    if request.method == "POST":

        role = request.POST['role']
        # he ek gosht lakshat thev tat ki requst.post nahi .files metohod vapartat photo get karnay sathi 

        pic = request.FILES['pic']
        name = request.POST['name']
        age = request.POST['age']
        edu = request.POST['edu']
        gender = request.POST['gender']
        tclass = request.POST['tclass']
        userid = request.POST['userid']
        password = request.POST['password']
        cpass = request.POST['cpassword']


        user = Teacher.objects.filter(user_id=userid)

        if user:
            sandesh = "user is already exsists!!"
            return render(request, "login.html", {'key':sandesh})
        
        else:
            if password == cpass :
                master = Uesrmaster.objects.create(password=password,role=role)
                tea = Teacher.objects.create(t_id=master,Name=name,age=age,educetion=edu,gender=gender,T_class=tclass,Teacher_pic=pic,user_id=userid,Password=password)

                sandesh = "teacher is successfully registered!!"
                return render(request,"login.html",{"key":sandesh})
            else:
                sandesh = "password and  conform password not match!!"
                return render(request, "tregister.html",{"key":sandesh})



def addresultpage(request):
    return render(request, "taddresult.html")


def stdsearch(request): 
    print("gelo")
    if request.method == "POST":
        print("hello")
        prn = request.POST.get('prn')
        #prn = int(prn)
        print(prn)
        try:
            s = Student.objects.get(s_id=prn)
        except:
            sandesh = "student is not exist!!E"
            return render(request,"taddresult.html",{"key":sandesh})
    
        if s:
            if s:
                request.session['s_id'] = str(s.s_id)  # Convert to string if needed
                request.session['sName'] = str(s.Name)
                request.session['sage'] = int(s.age)  # Ensure it's an integer
                request.session['sclass'] = str(s.S_class)

         
            print(request.session['s_id'])
           
            return render(request,"taddresult.html")
        else:
            sandesh = "student is not exist!!ee"
            return render(request,"taddresult.html",{"key":sandesh})
    sandesh = "student is not exist!!END"
    return render(request, "taddresult.html",{"key":sandesh})

def clrear(request):
    del request.session['s_id']
    del request.session['sName']
    del request.session['sage']
    del request.session['sclass']

    return render(request,"taddresult.html")




def taddresult(request):
    if request.method == "POST":
        prn = request.POST.get('prn')
        #pnr = request.session['s_id']
        print(prn)
        #pnr = 1
        s = Student.objects.get(s_id=prn)
        print(type(s))


        if s:
            for i in range(1,2):
                scode = request.POST.get('scode')
                sname = request.POST.get('sname')
                marks = request.POST.get('marks')


                sub,created = subject.objects.update_or_create(
                    sub_code=scode,
                    defaults={'sub_name':sname}
                    
                    )
                
                r,created = result.objects.update_or_create(
                    pnr=s,
                    scode=sub,
                    defaults={'obtained_marks':marks}
                   
                    )
                
            sandesh = "result is successfully added!!"
            return render(request,"taddresult.html",{"key":sandesh})
        else:
            sandesh = "student is not exist!!"
            return render(request,"taddresult.html",{"key":sandesh})
        
def addstudentpage(request):
    return render(request,"taddstu.html")

def tlogout(request):
    return redirect("login")
        
def show_individual_result(request):
    if request.method == "POST":
        pnr = request.POST.get('pnr')  # Get PRN from form
        try:
            # Get student details
            student = Student.objects.get(s_id=pnr)
            # Get all results for this student
            if student:
                 request.session['sName'] = str( student.Name)
                 results = result.objects.filter(pnr=student)
                 pnrn = pnr
                 context = {
                    'student': student,
                    'pnr' : pnrn,
                    'results': results,
                    'found': True
                }

            return render(request, "sresult.html", context)
        except Student.DoesNotExist:
            return render(request, "sresult.html", 
                        {'error': "Student not found!", 'found': False})
    
    return render(request, "sresult.html", {'found': False})