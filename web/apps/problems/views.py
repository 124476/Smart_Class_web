from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView
)
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from apps.problems.models import Problem, Status
from apps.problems.forms import ProblemForm, StatusForm


class ProblemListView(LoginRequiredMixin, ListView):
    model = Problem
    template_name = "problems/problems.html"
    context_object_name = "problems"

    def get_queryset(self):
        return Problem.objects.filter(user=self.request.user).select_related('status')


class ProblemDetailView(LoginRequiredMixin, DetailView):
    model = Problem
    template_name = "problems/problem_detail.html"
    context_object_name = "problem"

    def get_queryset(self):
        return Problem.objects.filter(user=self.request.user)


class ProblemCreateView(LoginRequiredMixin, CreateView):
    model = Problem
    form_class = ProblemForm
    template_name = "problems/problem_form.html"
    success_url = reverse_lazy("problems:problems")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ProblemUpdateView(LoginRequiredMixin, UpdateView):
    model = Problem
    form_class = ProblemForm
    template_name = "problems/problem_form.html"
    success_url = reverse_lazy("problems:problems")

    def get_queryset(self):
        return Problem.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ProblemDeleteView(LoginRequiredMixin, DeleteView):
    model = Problem
    template_name = "problems/problem_confirm_delete.html"
    success_url = reverse_lazy("problems:problems")

    def get_queryset(self):
        return Problem.objects.filter(user=self.request.user)
