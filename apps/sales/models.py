from django.db import models
from apps.products.models import Product
from django.contrib.auth.models import User

class Sale(models.Model):
    product_id  = models.ForeignKey( Product, related_name='sales', on_delete=models.DO_NOTHING)
    user_id     = models.ForeignKey( User, related_name='sales',  on_delete=models.CASCADE)
    quantity    = models.IntegerField( null=False )
    total       = models.DecimalField( max_digits=10, decimal_places=2 )
    dates       = models.DateTimeField( default = False )
    payment     = models.IntegerField( null=False )
    status      = models.BooleanField( default=False )

    class Meta:
        db_table = "sales"
