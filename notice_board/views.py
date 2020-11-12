from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import ProfileForm, UserCreateForm
from django.contrib.auth.decorators import login_required

@login_required
def ToppageView(request):
    """掲示板ページ"""
    return render(request, 'notice_board/toppage.html', {'request': request})


def SignupView(request):
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
    """プロフィールページ"""

    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'notice_board/profilepage.html', {'request': request, 'profile':profile})