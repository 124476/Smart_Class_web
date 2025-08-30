import calendar
from datetime import date
from apps.news.models import News
from apps.works.models import Event

import django.views.generic

MONTHS_RU = {
    1: "Январь",
    2: "Февраль",
    3: "Март",
    4: "Апрель",
    5: "Май",
    6: "Июнь",
    7: "Июль",
    8: "Август",
    9: "Сентябрь",
    10: "Октябрь",
    11: "Ноябрь",
    12: "Декабрь",
}


class Home(django.views.generic.ListView):
    template_name = "homepage/main.html"
    context_object_name = "items"
    queryset = [
        {
            "id": 1,
            "name": "first",
        },
        {
            "id": 2,
            "name": "second",
        },
    ]


class CalendarView(django.views.generic.TemplateView):
    template_name = "homepage/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = date.today()
        year = int(self.request.GET.get("year", today.year))
        month = int(self.request.GET.get("month", today.month))

        if month < 1:
            month = 12
            year -= 1
        elif month > 12:
            month = 1
            year += 1

        date_start = date(year, month, 1)
        _, num_days = calendar.monthrange(year, month)
        skip_days = date_start.weekday()

        news_for_month = News.objects.filter(
            created_at__year=year,
            created_at__month=month
        ).order_by('created_at')

        news_by_day = {}
        for news in news_for_month:
            day = news.created_at.day
            if day not in news_by_day:
                news_by_day[day] = []
            news_by_day[day].append(news)

        events_for_month = Event.objects.filter(
            date__year=year,
            date__month=month
        ).order_by('date')

        events_by_day = {}
        for event in events_for_month:
            day = event.date.day
            if day not in events_by_day:
                events_by_day[day] = []
            events_by_day[day].append(event)

        days = []
        for day_num in [""] * skip_days + list(range(1, num_days + 1)):
            if day_num:
                day_date = date(year, month, day_num)
                days.append({
                    'number': day_num,
                    'date': day_date,
                    'is_today': day_date == today,
                    'news': news_by_day.get(day_num, []),
                    'events': events_by_day.get(day_num, [])
                })
            else:
                days.append(None)

        prev_month = month - 1 if month > 1 else 12
        prev_year = year if month > 1 else year - 1
        next_month = month + 1 if month < 12 else 1
        next_year = year if month < 12 else year + 1

        context.update({
            "days": days,
            "month_name": MONTHS_RU[month],
            "year": year,
            "month": month,
            "prev_year": prev_year,
            "prev_month": prev_month,
            "next_year": next_year,
            "next_month": next_month,
            "today": today,
        })

        return context


class Games(django.views.generic.ListView):
    template_name = "homepage/games.html"
    context_object_name = "items"
    queryset = [
        {
            "id": 1,
            "name": "first",
        },
        {
            "id": 2,
            "name": "second",
        },
    ]


class Program(django.views.generic.ListView):
    template_name = "homepage/school_program.html"
    context_object_name = "items"
    queryset = [
        {
            "id": 1,
            "name": "first",
        },
        {
            "id": 2,
            "name": "second",
        },
    ]


class AdminProgram(django.views.generic.TemplateView):
    template_name = "homepage/admin_program.html"
