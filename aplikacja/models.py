from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=64)
    car_model = models.CharField(max_length=64)
    year_of_production = models.PositiveSmallIntegerField(default=2000)
    mileage = models.PositiveIntegerField()
    photo = models.ImageField(upload_to="img", null=True, blank=True)
    def __str__(self):
        return "{} {} ({})".format(self.brand, self.car_model, self.year_of_production)


class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Transaction(models.Model):
    final_price = models.PositiveIntegerField()
    date = models.DateField()
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)    


    def __str__(self):
        return "{} ({} PLN)".format(self. date, self.final_price)