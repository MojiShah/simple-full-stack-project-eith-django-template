from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.DecimalField(decimal_places=0,max_digits=3)

    def __str__(self):
        return self.name + ' ,' + str(self.age)