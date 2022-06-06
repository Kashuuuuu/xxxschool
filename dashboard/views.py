from email import message
from multiprocessing import context
import re
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages as sms
from django.contrib.auth.models import User
from dashboard.models import frgt_pwd, professor
from django.core.mail import send_mail
from django.conf import settings
from dashboard.models import admin_profile
from .forms import ProductForm
from dashboard.models import professor,student

# Create your views here.
def ad_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request,"dashboard.html")
    else: 
        return redirect('login')   

def forgot(request):
    if request.user.is_authenticated!=True and request.user.is_superuser!=True:
           if request.method =='POST':
                email=request.POST.get('email')

                if not User.objects.filter(email=email).first():
                    sms.success(request,'no user found,please signup..')
                    return redirect('login')

                else:
                    user_email = User.objects.get(email=email)
                    
                    profile_obj = frgt_pwd.objects.get(user=user_email).frg_token
                
                
                    subject = 'your forgot password link'
                    message = f'Hi,click on the link to reset your password http://127.0.0.1:8000/password_reset/{profile_obj}.'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email]
                    send_mail(subject,message,email_from,recipient_list)
                    
                    sms.success(request,'message sent successfully..')
                    
    return render(request,"forgot.html") 
     

def password_reset(request,token):
    if request.user.is_authenticated!=True and request.user.is_superuser!= True:
        if request.method=='POST':
            try:
                pass1=request.POST['pass1']
                confirm=request.POST['pass2']
                if pass1==confirm:
                    frgpwd=frgt_pwd.objects.get(frg_token=token)
                    user=User.objects.get(username=frgpwd)
                    user.set_password(pass1)
                    user.save()
                    sms.success(request, "Password Change Successfully.\n +Please login. ")
                    return redirect('login')
                else:
                    sms.error(request,'Password Not Match.Enter Same Password.')
            except:
                pass
        return render(request,'password_reset.html')
    else:
        return redirect('error') 

# def admin_prof(request):
#     form = productForm(request.POST)
#     if request.user.is_authenticated and request.user.is_superuser:
#         profile_data = admin_profile.objects.all()
#         if request.method=='POST':
#             if form.is_valid():
#                 form.save()
#     data = {'profile_data':profile_data}
#     return render(request,"admin_profile.html",data)      

def admin_prof(request):
   
    if request.user.is_authenticated and request.user.is_superuser:
            profile_data = admin_profile.objects.all()
        
            if request.POST.get('uss')!=None:
                   
                    old = request.POST['old']
                    new = request.POST['new']
                    confirm = request.POST['confirm']
                    user = User.objects.get(id=request.user.id)
                    mail=user.email
                    check=user.check_password(old)
                    if confirm==new:
                        if check==True:
                            user.set_password(new)
                            user.save()
                            # user=User.objects.get(email=mail)
                            login(request,user)
                            sms.success(request, "Password Updated")
                            return redirect('admin_profile')
                        else:
                            sms.error(request, "Incorrect Old Password")
                            return redirect('admin_profile')
                    else:
                        sms.error(request,'New And Confirm Password Not Match.')

    
    data = {'profile_data':profile_data}
    return render(request,"admin_profile.html",data) 

def edit_admin_profile(request,pk):
    product = admin_profile.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST , request.FILES , instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_profile')
  
    context = {
        'form':form
    }      
  
    return render(request,"edit_admin_profile.html",context)          


def ad_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('ad_dash')
    else:
        if request.method == 'POST':   
            username = request.POST.get('username')
            password= request.POST.get('password') 
            print(username)
            USER = authenticate(request, username=username,password=password)
            if USER is not None:
                login(request,USER)
                if request.user.is_superuser:
                    sms.success(request,"Logged in successfully..")
                    return redirect('ad_dash')
                else:
                    sms.success(request,"wrong username or password")
                    return redirect('login')

    return render(request,"login.html") 

def ad_logout(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            logout(request)
            sms.success(request,"Logged out successfully..")
            return redirect('login')
        except:
            sms.warning(request,'something went wrong !')
            return redirect('login')
    else:        
        return redirect('login')  

def event_man(request):
    return render(request,"event_man.html")        

def all_prof(request):
    professor_data = professor.objects.all()

    sd= request.POST.get('profdel')
    se= request.POST.get('profedit')
    if sd!=None:
        sd= professor.objects.filter(id=sd)
        sd.delete()
        sms.info(request,"Professor deleted successfully ..")
        return redirect('all_prof')
    elif se!=None:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        joining_date = request.POST.get('joining_date')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        dob = request.POST.get('dob')
        education = request.POST.get('education')
        image = request.POST.get('image')
        prod= professor.objects.filter(id=se)

        if len(prod)>0:
            ob=prod[0] 
            print(ob)
            if len(firstname)>0:
                print(firstname)
                ob.firstname=firstname
            if len(lastname)>0:
                ob.lastname=lastname
            if len(email)>0:
                ob.email=email
            if len(joining_date)>0:
                ob.joining_date=joining_date
            if len(password)>0:
                ob.password=password
            if len(confirm_password)>0:
                ob.confirm_password=confirm_password
            if len(mobile)>0:
                ob.mobile=mobile
            if len(gender)>0:
                ob.gender=gender
            if len(designation)>0:
                ob.designation=designation
            if len(department)>0:
                ob.department=department  
            if len(dob)>0:
                ob.dob=dob  
            if len(education)>0:
                ob.education=education                                             
            if len(image)>0:
                ob.image=image 
            ob.save()                                                   
            sms.success(request,'Professor Updated.')
            return redirect('all_prof') 

    context = {'professor_data':professor_data}
    return render(request,"all_professors.html",context)

def add_prof(request):
    if request.method=="POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        joining_date = request.POST.get('joining_date')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        dob = request.POST.get('dob')
        education = request.POST.get('education')
        image = request.FILES.get('image')
       
        data = professor(firstname=firstname,department=department,dob=dob,image=image,education=education,designation=designation,gender=gender,mobile=mobile,confirm_password=confirm_password,lastname=lastname,email=email,joining_date=joining_date,password=password,)
       
        data.save()
        sms.info(request,"Professor successfully added..")
        return redirect('all_prof')
    else:
        sms.info(request," error, try again!!")
        professor_data = professor.objects.all()
        

        context = {'professor_data':professor_data}
            
    return render(request,"add_professor.html",context)
 

def edit_prof(request,myid):
    profs = professor.objects.get(id=myid)
    professor_data = professor.objects.all()
    
        

    context = {'professor_data':professor_data,
        'profs':profs}
            
    
    return render(request,"edit_professor.html",context)


def prof_profile(request):
    return render(request,"professor_profile.html")

def all_student(request):
    stud = student.objects.all()
    sd= request.POST.get('delete')
    se= request.POST.get('edit')
    if sd!=None:
        sd= student.objects.filter(id=sd)
        sd.delete()
        sms.info(request,"Student deleted successfully ..")
        return redirect('all_student')
    elif se!=None:
        print(se)
        firstname = request.POST['firstname']
        print(firstname)
        lastname = request.POST['lastname']
        print(lastname)
        email = request.POST['email']
        education = request.POST['education']
        registration_date = request.POST['registration_date']
        roll_no = request.POST['roll_no']
        sub_class = request.POST['sub_class']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        parent_name = request.POST['parent_name']
        parent_mobile = request.POST['parent_mobile']
        dob = request.POST['dob']
        blood_group = request.POST['blood_group']
        address = request.POST['address']
        image = request.POST['image']
        prod= student.objects.filter(id=se)

        if len(prod)>0:
            ob=prod[0] 
            print(ob)
            if len(firstname)>0:
                print(firstname)
                ob.firstname=firstname
            if len(lastname)>0:
                ob.lastname=lastname
            if len(email)>0:
                ob.email=email
            if len(education)>0:
                ob.education=education
            if len(registration_date)>0:
                ob.registration_date=registration_date
            if len(roll_no)>0:
                ob.roll_no=roll_no
            if len(sub_class)>0:
                ob.sub_class=sub_class
            if len(gender)>0:
                ob.gender=gender
            if len(mobile)>0:
                ob.mobile=mobile
            if len(parent_name)>0:
                ob.parent_name=parent_name
            if len(parent_mobile)>0:
                ob.parent_mobile=parent_mobile
            if len(dob)>0:
                ob.dob=dob
            if len(blood_group)>0:
                ob.blood_group=blood_group
            if len(address)>0:
                ob.address=address 
            if len(image)>0:
                ob.image=image 
            ob.save()                                                   
            sms.success(request,'Student Updated.')
            return redirect('all_student') 
    
    context={'stud':stud}
    return render(request,"all_student.html",context)

def add_student(request):
    if request.method=="POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        education = request.POST.get('education')
        registration_date = request.POST.get('registration_date')
        roll_no = request.POST.get('roll_no')
        sub_class = request.POST.get('sub_class')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        parent_name = request.POST.get('parent_name')
        parent_mobile = request.POST.get('parent_mobile')
        dob = request.POST.get('dob')
        blood_group = request.POST.get('blood_group')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        data = student(firstname=firstname,sub_class=sub_class,image=image,address=address,blood_group=blood_group,dob=dob,parent_mobile=parent_mobile,mobile=mobile,parent_name=parent_name,gender=gender,lastname=lastname,roll_no=roll_no,email=email,education=education,registration_date=registration_date,)       
        data.save()
        sms.info(request,"Student successfully added..")
        return redirect('all_student')
        
    return render(request,"add_student.html")

def edit_student(request):
    return render(request,"edit_student.html")

def about_student(request):
    return render(request,"about_student.html")   

def all_course(request):
    return render(request,"all_courses.html")

def add_course(request):
    return render(request,"add_course.html")

def edit_course(request):
    return render(request,"edit_course.html")

def about_course(request):
    return render(request,"about_course.html") 

def all_library(request):
    return render(request,"all_library.html") 

def add_library(request):
    return render(request,"add_library.html") 

def edit_library(request):
    return render(request,"edit_library.html")   

def all_department(request):
    return render(request,"all_department.html") 

def add_department(request):
    return render(request,"add_department.html") 

def edit_department(request):
    return render(request,"edit_department.html")

def all_staff(request):
    return render(request,"all_staff.html")  

def add_staff(request):
    return render(request,"add_staff.html")  

def edit_staff(request):
    return render(request,"edit_staff.html")  

def staff_profile(request):
    return render(request,"staff_profile.html") 

def all_holiday(request):
    return render(request,"all_holiday.html")

def add_holiday(request):
    return render(request,"add_holiday.html")

def edit_holiday(request):
    return render(request,"edit_holiday.html")

def holiday_calender(request):
    return render(request,"holiday_calender.html")

def fees_collection(request):
    return render(request,"fees_collection.html") 

def add_fees(request):
    return render(request,"add_fees.html") 

def fees_receipt(request):
    return render(request,"fees_receipt.html")

def app_profile(request):
    return render(request,"app_profile.html")  

def email_compose(request):
    return render(request,"email_compose.html")  

def email_inbox(request):
    return render(request,"email_inbox.html")  

def email_read(request):
    return render(request,"email_read.html")                                                                


        