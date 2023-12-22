from django.urls import path
from . import views

urlpatterns = [
    path("refuse-route-confirmation/", views.refuse_route_confirmation),
    path("", views.StartPageView.as_view(), name="start-page"),
    path("routes/", views.RoutesView.as_view(), name="routes-page"),
    path("select-route/", views.SelectRouteView.as_view(), name="select-route-page"),
    path("select-route/refuse-route", views.refuse_route, name="refuse-route-page"),
]
