from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from apps.users.forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from apps.users.models import Profile


class RegisterView(View):
    template_name = "users/signup.html"

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('homepage:main')

        return render(request, self.template_name, {'form': form})


class UserLoginView(LoginView):
    template_name = "users/login.html"


def user_logout(request):
    logout(request)
    return redirect("users:login")


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)

        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

        return render(
            request,
            "users/profile.html",
            {
                "user_form": user_form,
                "profile_form": profile_form,
                "birthday_value": profile.birthday.strftime(
                    '%Y-%m-%d') if profile.birthday else ''
            },
        )

    def post(self, request):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("users:profile")

        return render(
            request,
            "users/profile.html",
            {
                "user_form": user_form,
                "profile_form": profile_form,
                "birthday_value": request.POST.get('birthday', '')
            },
        )


@require_POST
@login_required
def delete_avatar(request):
    profile = request.user.profile
    if profile.image:
        profile.image.delete()
        profile.image = None
        profile.save()
    return JsonResponse({'status': 'success'})