import django.views.generic


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
