from django.db import models
class Products(models.Model):
    name = models.CharField(max_length=6)
    image = models.ImageField(upload_to='pics',default=None)


