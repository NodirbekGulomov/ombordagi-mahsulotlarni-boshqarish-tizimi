from django.shortcuts import render

from core.forms import MahsulotForm
from core.models import Mahsulot


# Create your views here.
def home(request):
    mahsulotlar = Mahsulot.objects.all()
    return render(request, "index.html", {"mahsulotlar": mahsulotlar})


def crate(request):
    if request.method == "POST":
        form = MahsulotForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MahsulotForm()
    return render(request, "create-mahsulot.html", {"form": form})
