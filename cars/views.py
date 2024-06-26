from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView


class CarsView(View):

    def get(self, request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search')

        if search:
            cars = cars.filter(model__icontais=search)
        
        return render(request, 'cars.html', {'cars': cars})


class CarsListView(ListView):
    pass


class NewCarView(View):

    def get(self,request):
        new_car_form = CarModelForm
        return render(request, 'new_car.html', {'new_car_view': new_car_form})
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('car_list')
        return render(request, 'new_car.html', {'new_car_view': new_car_form})
