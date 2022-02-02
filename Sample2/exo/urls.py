from django.urls import path
from . import views

app_name = "exo"

urlpatterns = [
    path("", views.Index, name="index"),
    path(f"{app_name}/", views.Index),
    path(f"{app_name}/<int:id_person>/", views.Detail, name="detail"),
    path(f"{app_name}/HTML/", views.IndexHTML, name="indexHTML"),
    path(f"{app_name}/HTML/<int:id_person>/", views.DetailHTML, name="detailHTML"),
    path(f"{app_name}/Gen/", views.IndexGen.as_view(), name="indexGen"),
    path(f"{app_name}/Gen/<int:pk>/", views.DetailGen.as_view(), name="detailGen"),
]
