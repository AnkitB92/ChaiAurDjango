from django.urls import path
from . import views

urlpatterns=[
  path('', views.chai_app, name='chai_app'),
  path('<int:chai_id>/', views.chai_details, name='chai_details'),
]