from django.db import models


# Create your models here.

class Stocks(models.Model):
    name = models.CharField(max_length=80)
    symbol = models.CharField(max_length=10)
    aimed_price = models.FloatField()
    current_price = models.FloatField()
    user_id = models.IntegerField()

    def __str__(self):
        return self.name