from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings


def home(request):
    return render(request, "website/index.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("chai/", include("chai_app.urls")),

    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
