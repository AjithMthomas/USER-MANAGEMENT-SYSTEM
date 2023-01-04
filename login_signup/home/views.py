import queue
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import signupfeilds
from django.db.models import Q



# Create your views here.
def login(request):
    if 'username' in request.session:
        return redirect('home')
    return render(request,'login.html')
     
def signup(request):
    return render(request,'signup.html')

def home(request):
    if 'username' in request.session:
        return render(request,'home.html')
    else:
        return render(request,'login.html')

def adduser(request):
    return render(request,'adduser.html')


def update_user(request,id):
    context={
        'users':signupfeilds.objects.get(id=id)
    }
    return render(request,'update_user.html',context)


def register(request):
   if request.method == 'POST':
        if signupfeilds.objects.filter(
          Email_address = request.POST['Eaddress'], First_name = request.POST['Fname'] ,Last_name=request.POST['Lname']
        ).exists():
            messages.error(request, "email or username already exist...!",extra_tags='email_exist')
            return render(request, 'signup.html')
        
        elif request.POST['pass'] != request.POST['Cpass']:
            return render(request, 'signup.html')        
        
        else:
            values =signupfeilds(
               First_name = request.POST['Fname'],
               Last_name=request.POST['Lname'],
               Email_address = request.POST['Eaddress'],
               Password = request.POST['pass']
            )
            values.save()
            return render(request, 'login.html')

   else:
        return render(request, 'signup.html')




def ActionLogin(request):
    if request.method == 'POST':
       username = request.POST['username']
       pass1 = request.POST['pass1']
       user = authenticate(request,username=username,password=pass1)
       if user is not None:
        request.session['username']= username
        context={
            'users':signupfeilds.objects.all()
               }
        return render(request,'admin.html',context)

       else:
            if signupfeilds.objects.filter(
                Email_address = request.POST['username'], Password = request.POST['pass1']
                ).exists():
                request.session['username'] = request.POST['username']
                context={
                    'users':signupfeilds.objects.get(Email_address=username)
                }
                return render(request, 'home.html',context)
            else:
                messages.error(request, "Email address or password is incorrect...!",extra_tags='login_fail')
                return render(request, 'login.html')
    else:
        return render (request,'login.html')



def logout(request):
    request.session.flush()
    messages.success(request,"logged out succesfully ",extra_tags='log_out')
    return render(request,'login.html')



def admin_p(request):
    if request.user.is_authenticated:
        context={
        'users':signupfeilds.objects.all()
        }
        return redirect('admin_p')
    elif 'username' in request.session:
        context={
        'users':signupfeilds.objects.all()
        }
        return render(request,'admin.html',context)
    else:
        return render(request,'login.html')
    


def delete_user(request,id):
    data = signupfeilds.objects.get(id=id)
    data.delete()
    context={
        'users':signupfeilds.objects.all()
    }
    return render(request,'admin.html',context)


def adduserin(request):
      if request.method == 'POST':
        if signupfeilds.objects.filter(
          Email_address = request.POST['email'], First_name = request.POST['fname'] ,Last_name=request.POST['lname']
        ).exists():
            messages.error(request, "email or username already exist...!",extra_tags='email_exist')
            return render(request, 'adduser.html')
        elif request.POST['password'] != request.POST['rpassword']:
            return render(request, 'adduser.html')        
        
        else:
            values =signupfeilds(
               First_name = request.POST['fname'],
               Last_name=request.POST['lname'],
               Email_address = request.POST['email'],
               Password = request.POST['password']
            )
            values.save()
            context={
                'users':signupfeilds.objects.all()
            }
            return render(request, 'admin.html',context)

def update_form(request,id):
    if request.method == 'POST':
        ex = signupfeilds.objects.filter(id=id).update(
            First_name = request.POST['fname'],
            Last_name = request.POST['lname'],
            Email_address = request.POST['email'],
            Password = request.POST['password'],
        )
        context={
            'users':signupfeilds.objects.all()
        }
        return render(request, 'admin.html',context)
    else:
        return render(request,'update_user.html')

def search_page(request):
    return render(request,'search.html')

def search(request):
    query = request.GET.get('q')
    if query:
        results = signupfeilds.objects.filter(
            Q(First_name=query) | Q(Email_address=query) 
        )
    else:
        results =signupfeilds.objects.all()
    return render(request, 'search.html', {'results': results})