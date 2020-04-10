from django.views.generic import ListView, DetailView

from .models import Manufacture


class ManufactureList(ListView):
    model = Manufacture
    template_name = 'manufacture/manufacture_list.html'


class ManufactureDetail(DetailView):
    model = Manufacture
    template_name = 'manufacture/manufacturers_detail.html'
