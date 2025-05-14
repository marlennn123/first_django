from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.brand_name


class CarModel(models.Model):
    car_model_name = models.CharField(max_length=10, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand}, {self.car_model_name}'


class Car(models.Model):
    car_name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    year = models.DateField()
    mileage = models.PositiveIntegerField(verbose_name='Пробег')
    color = models.CharField(max_length=16)
    city = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.car_name
