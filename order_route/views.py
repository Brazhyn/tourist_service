from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from .models import Tourist, Route
from .forms import TouristForm, RefuseRouteForm
from django.http import HttpResponseRedirect


class StartPageView(ListView):
    template_name = "order_route/start-page.html"
    model = Route
    context_object_name = "routes"
    ordering = ["-rating"]

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class RoutesView(ListView):
    template_name = "order_route/routes.html"
    model = Route
    context_object_name = "routes"


class SelectRouteView(View):
    def get(self, request):
        form = TouristForm()
        return render(request, "order_route/select-route.html", {
            "form": form
        })

    def post(self, request):
        form = TouristForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/select-route")

        return render(request, "order_route/select-route.html", {
            "form": form
        })


def refuse_route_confirmation(request):
    return render(request, "order_route/refuse-route-confirmation.html")


def refuse_route(request):
    if request.method == 'POST':
        form = RefuseRouteForm(request.POST)

        if form.is_valid():
            last_name = form.cleaned_data['last_name']
            user = get_object_or_404(Tourist, last_name=last_name)
            user.delete()
            return HttpResponseRedirect("/refuse-route-confirmation")

    else:
        form = RefuseRouteForm()

    return render(request, 'order_route/refuse-route.html', {'form': form})



