from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    DetailView,
)
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from apps.works.models import Event, Feedback
from apps.works.forms import EventForm, FeedbackForm


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "works/events.html"
    context_object_name = "events"

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)


class EventDetailView(DetailView):
    model = Event
    template_name = "works/event_detail.html"
    context_object_name = "event"


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = "works/event_form.html"
    success_url = reverse_lazy("works:events")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = "works/event_form.html"
    success_url = reverse_lazy("works:events")

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = "works/event_confirm_delete.html"
    success_url = reverse_lazy("works:events")

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)


class FeedbackView(LoginRequiredMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "works/feedback.html"
    success_url = reverse_lazy("works:feedback")

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        return HttpResponseRedirect(f"{self.request.path}?success=1")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["success"] = self.request.GET.get("success") == "1"
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "works/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = Event.objects.filter(user=self.request.user).order_by('date')
        context["event_count"] = events.count()
        context["completed_events"] = events.filter(date__lt=timezone.now()).count()
        context["next_event"] = events.filter(date__gte=timezone.now()).first()
        return context
