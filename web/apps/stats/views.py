from django.views.generic import TemplateView
from django.db.models.functions import TruncMonth
from django.db.models import Count
from apps.users.models import User


class AnalyticsView(TemplateView):
    template_name = "stats/stats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        registrations = (
            User.objects.annotate(month=TruncMonth("date_joined"))
            .values("month")
            .annotate(total=Count("id"))
            .order_by("month")
        )

        months = []
        counts = []

        for item in registrations:
            months.append(item["month"].strftime("%b"))
            counts.append(item["total"])

        if not months:
            months = [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
            ]
            counts = [120, 190, 170, 220, 300, 280, 350, 400, 370, 420, 390, 450]

        context["chart_data"] = {
            "labels": months,
            "datasets": [
                {
                    "label": "Регистрации",
                    "data": counts,
                }
            ],
        }

        return context
