__all__ = ()
import django.shortcuts


class Description(django.views.generic.View):
    def get(self, request, *args, **kwargs):
        return django.shortcuts.render(request, "about/main.html")
