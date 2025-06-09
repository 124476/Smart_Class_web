from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from apps.users.forms import CustomUserCreationForm, CustomUserChangeForm
from apps.users.models import User
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth import login, update_session_auth_hash


class RegisterView(FormView):
    template_name = 'users/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('homepage:main')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Регистрация прошла успешно!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Исправьте ошибки в форме.')
        return super().form_invalid(form)


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        messages.info(self.request, f"Вы вошли как {form.get_user()}.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Неверное имя пользователя или пароль.")
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('homepage:main')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы успешно вышли из системы.")
        return super().dispatch(request, *args, **kwargs)


class AccountView(LoginRequiredMixin, FormView):
    template_name = "users/profile.html"
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('users:profile')

    def get_initial(self):
        user = self.request.user
        return {
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "avatar": user.avatar,
        }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def form_valid(self, form):
        new_username = form.cleaned_data.get("username")

        if new_username != self.request.user.username:
            if User.objects.filter(username=new_username).exists():
                form.add_error("username", "Это имя пользователя уже занято.")
                return self.form_invalid(form)

        form.save()
        messages.success(self.request, "Профиль успешно обновлен!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Пожалуйста, исправьте ошибки в форме.")
        return super().form_invalid(form)


class PasswordChangeView(LoginRequiredMixin, FormView):
    template_name = 'users/password_change.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        messages.success(self.request, 'Пароль успешно изменен!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Исправьте ошибки в форме.')
        return super().form_invalid(form)


class PasswordChangeDoneView(LoginRequiredMixin, TemplateView):
    template_name = 'users/password_change_done.html'
