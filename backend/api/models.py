from django.db import models
from django.db.models import Manager


class NamesModel(models.Model):
    objects = Manager()

    name = models.CharField(max_length=64)
    # TODO need to make these fields more optimized
    age_distribution_10 = models.IntegerField()
    age_distribution_20 = models.IntegerField()
    age_distribution_30 = models.IntegerField()
    age_distribution_50 = models.IntegerField()
    age_distribution_70 = models.IntegerField()
    age_distribution_71 = models.IntegerField()

    total_bearing_name = models.IntegerField()
    average_age = models.IntegerField()
    number_of_letters = models.CharField(max_length=16)
    double_name = models.BooleanField()
    frequency = models.CharField(max_length=128)
    meaning = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class BoyName(NamesModel):
    pass


class GirlName(NamesModel):
    pass


class PopularName(models.Model):
    year = models.IntegerField()
    position = models.IntegerField()
    name = models.CharField(max_length=64)
    gender = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Variant(models.Model):
    name = models.CharField(max_length=64)
    language = models.CharField(max_length=256)
    variants = models.TextField()

    def __str__(self):
        return self.name


class Email(models.Model):
    email = models.EmailField()
    domain = models.CharField(max_length=256)
    date = models.DateField()
    time = models.TimeField()
