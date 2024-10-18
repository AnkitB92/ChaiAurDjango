from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety, Store
from .forms import ChaiVarietyForm

# Create your views here.


def chai(request):
    all_chai = ChaiVariety.objects.all()
    return render(request, "chai_app/chai.html", {"all_chai": all_chai})


def chai_details(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, "chai_app/chai_details.html", {"chai": chai})


def chai_store_view(request):
    stores = None

    if request.method == "POST":
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data["chai_variety"]
            stores = Store.objects.filter(chai_varieties=chai_variety)
    else:
        form = ChaiVarietyForm()
    return render(
        request, "chai_app/chai_stores.html", {"stores": stores, "form": form}
    )
