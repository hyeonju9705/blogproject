from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog #같은경로에 있는 models에 class Blog를 데려온다는 뜻
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    blogs = Blog.objects
    blog_list=Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    return render(request,'home.html', {'blogs':blogs, 'posts':posts})
    #{}라는 딕셔너리에 넣으면 html에서 키를 사용할 수 있음

def detail(request, blog_id):
    detail= get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'detail': detail})

def new(request):
    return render(request, 'new.html' )

def create(request):
    print('hello')
    blog=Blog()
    blog.title=request.GET['title']
    blog.body= request.GET['body']
    blog.pub_date=timezone.datetime.now()
    
    blog.save()
    return redirect('/blog/'+str(blog.id))

def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 -->post
   
    if request.method == 'POST':
        form=BlogPost(request.POST)
        if form.is_valid() :
            post= form.save(comit=False)
            post.pub_date= timezone.now()
            post.save()
            return redirect('home')
      # 2. 빈 페이지를 띄워주는 기능 -->get
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})