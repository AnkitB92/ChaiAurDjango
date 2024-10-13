from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety
# Create your views here.

def chai_app(request):
  all_chai = ChaiVariety.objects.all()
  return render(request, 'chai_app/chai_app.html', {'all_chai': all_chai})


def chai_details(request, chai_id):
  chai = get_object_or_404(ChaiVariety, pk=chai_id)
  return render(request, 'chai_app/chai_details.html', {'chai': chai})