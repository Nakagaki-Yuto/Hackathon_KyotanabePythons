from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Thread, Post, Category
from .forms import ProfileForm, UserCreateForm
from django.contrib.auth.decorators import login_required



def SignupView(request):
    """サインアップ"""
    user_form = UserCreateForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)
    if request.method == "POST" and user_form.is_valid() and profile_form.is_valid():

        # Userモデルの処理
        user = user_form.save(commit=False)
        user.is_active = True
        user.save()

        # Profileモデルの処理
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        return redirect('/')

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, 'registration/signup.html', context)


@login_required
def ProfileView(request):
    """プロフィール"""
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'notice_board/profilepage.html', {'request': request, 'profile': profile})
    

@login_required
def ToppageView(request):
    """トップページ"""
    profile = UserProfile.objects.get(user=request.user)
    threads = Thread.objects.filter(university=profile.university)
    return render(request, 'notice_board/toppage.html', {'request': request, 'profile':profile, 'threads':threads})


@login_required
def ThreadListView(request, pk):
    """カテゴリーごとの掲示板一覧"""
    if pk == 1:
        cate = '学業・講義'
    elif pk == 2:
        cate='サークル・部活動'
    elif pk == 3:
        cate='アルバイト'
    elif pk == 4:
        cate='就職活動'
    elif pk == 5:
        cate='趣味・遊び'
    elif pk == 6:
        cate = 'その他・雑談'
    
    threads = Thread.objects.filter(category=pk)
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'notice_board/thread_list.html', {'category':cate, 'profile':profile, 'threads':threads})


@login_required
def ThreadDetailView(request, pk):
    """掲示板"""
    thread = get_object_or_404(Thread, pk=pk)
    posts = Post.objects.filter(thread=thread)
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'notice_board/thread_detail.html', {'thread': thread, 'profile':profile, 'posts':posts})


@login_required
def AddPostView(request, pk):
    """掲示板への投稿"""
    if request.method == "POST": 
        thread = get_object_or_404(Thread, pk=pk)
        posts = Post.objects.filter(thread=thread)
        text = request.POST['post-text']
    
        post = Post()
        post.thread = thread
        post.author = request.user
        post.text = text
        post.save()

    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'notice_board/thread_detail.html', {'thread': thread, 'profile':profile, 'posts':posts})


@login_required
def AddThreadView(request):
    """掲示板の作成"""
    if request.method == "POST": 
        category_id = request.POST['thread-form-category']
        title = request.POST['thread-form-title']
        category = Category.objects.get(id=category_id)
        user = UserProfile.objects.get(user=request.user)

        thread = Thread()
        thread.university = user.university
        thread.author = request.user
        thread.title = title
        thread.category = category
        thread.save()

    thread = Thread.objects.latest('created_date')
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'notice_board/thread_detail.html', {'thread': thread, 'profile': profile})
    

@login_required
def ReportView(request):
    """レポート"""
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'notice_board/thread_detail.html', {'profile': profile})