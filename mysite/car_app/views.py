from django.urls import reverse_lazy
from .models import Car
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from .forms import CarForms


class CarListView(ListView):
    queryset = Car.objects.all()
    template_name = 'car_list.html'
    context_object_name = 'cars'


class CarDetailView(DetailView):
    queryset = Car.objects.all()
    template_name = 'car_detail.html'
    context_object_name = 'car'


class CarCreateView(CreateView):
    template_name = 'car_create.html'
    form_class = CarForms
    success_url = reverse_lazy('car_list')


class CarUpdateView(UpdateView):
    queryset = Car.objects.all()
    template_name = 'car_update.html'
    form_class = CarForms
    success_url = reverse_lazy('car_list')


class CarDeleteView(DeleteView):
    queryset = Car.objects.all()
    template_name = 'car_delete.html'
    success_url = reverse_lazy('car_list')
