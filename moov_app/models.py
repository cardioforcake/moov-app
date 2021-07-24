from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Furniture(models.Model):
    type = models.CharField(max_length=25)
    length = models.IntegerField()
    width = models.IntegerField()
    color = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('demo', kwargs={'pk': self.id})

class FloorPlan(models.Model):
    name = models.CharField(max_length=20)
    length = models.IntegerField()
    width = models.IntegerField() 
    furnitures = models.ManyToManyField(Furniture, through='LinkedFurniture')
    comment = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('floorplan_index')

class LinkedFurniture(models.Model):
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    floorplan = models.ForeignKey(FloorPlan, on_delete=models.CASCADE)
    rotated = models.IntegerField(default=1)


class Photo(models.Model):
    url = models.CharField(max_length=200)
    floorplan = models.ForeignKey(FloorPlan, on_delete=models.CASCADE)

    def __str__(self):
        return f" photo for floorplan_id: {self.floorplan_id} @{self.url}"

    # def get_absolute_url(self):
    #     return reverse('floorplan_index')
         

    