from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator
# Create your views here.
def portfolio(request):
    return render(request, 'portfolio.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
          user=User.objects.create_user( username=request.POST['username'], password=request.POST['password1'])
          auth.login(request,user)
          return redirect('blog')  
    return render(request, 'accounts/signup.html')

def login(request):
    if  request.method=='POST':
            username=request.POST['username']
            password= request.POST['password']
            user= auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request, 'accounts/login.html', {'error':'username or password is incorrect.'})
    else:
    
        return render(request, 'login.html')

def logout(request):
    if request.metod == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(jrequest, 'login.html')

def home(request):
    blogs=Blog.objects
    blog_list= Blog.objects.all()
    paginator=Paginator(blog_list, 3)
    page=request.GET.get('page')
    posts=paginator.get_page(page)
    return render(request,'home.html',{'blogs':blogs})

