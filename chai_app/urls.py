from django.urls import path
from . import views

urlpatterns = [
    path("", views.chai, name="chai"),
    path("<int:chai_id>/", views.chai_details, name="chai_details"),
    path("stores/", views.chai_store_view, name="stores"),
]
