from django.db import models

# Create your models here.

class Supplier(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.id) + ')' + self.first_name + ' ' +self.last_name

class ServiceArea(models.Model):
    supplier = models.ForeignKey('Supplier')
    x1 = models.DecimalField( max_digits=15, decimal_places=12)
    y1 = models.DecimalField( max_digits=16, decimal_places=12)
    x2 = models.DecimalField( max_digits=15, decimal_places=12)
    y2 = models.DecimalField( max_digits=16, decimal_places=12)
    def __str__(self):
        return str(self.id)
    
class Vertice(models.Model):
    service_area = models.ForeignKey('ServiceArea')
    longitude   = models.DecimalField( max_digits=15, decimal_places=12)
    latitude   = models.DecimalField( max_digits=14, decimal_places=12)
    def __str__(self):
        return str(self.id)

