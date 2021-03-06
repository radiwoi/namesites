from django.db import models


class NamesModel(models.Model):
    name = models.CharField(max_length=64, unique=True)
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
    variants = models.ManyToManyField('Variant', related_name='boy_names')
    popular = models.ManyToManyField('PopularName', related_name='boy_names')


class GirlName(NamesModel):
    variants = models.ManyToManyField('Variant', related_name='girl_names')
    popular = models.ManyToManyField('PopularName', related_name='girl_names')


class PopularName(models.Model):
    year = models.IntegerField()
    position = models.IntegerField()
    # name = models.CharField(max_length=64)
    # gender = models.CharField(max_length=16)

    def __str__(self):
        return "{} {}".format(self.year, self.position)

    class Meta:
        unique_together = ('year', 'position',)


class Variant(models.Model):
    # name = models.CharField(max_length=64)
    language = models.CharField(max_length=64)
    name = models.CharField(max_length=64)

    def __str__(self):
        return "{} {}".format(self.language, self.name)

    class Meta:
        unique_together = ('language', 'name',)


class Email(models.Model):
    email = models.EmailField()
    domain = models.CharField(max_length=256)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)


class FooterTexts(models.Model):
    boy_title = models.CharField(max_length=64, null=True)
    girl_title = models.CharField(max_length=64, null=True)
    position = models.CharField(max_length=64)
    boy_names = models.TextField(null=True)
    girl_names = models.TextField(null=True)
    read_more_words = models.IntegerField()

    class Meta:
        verbose_name_plural = "footer text"


class FlicknamnFooterText(models.Model):
    title = models.CharField(max_length=64, null=True)
    position = models.CharField(max_length=64)
    names = models.TextField(null=True)
    read_more_words = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Flicknamn Footer Texts"


class PojknamnFooterText(models.Model):
    title = models.CharField(max_length=64, null=True)
    position = models.CharField(max_length=64)
    names = models.TextField(null=True)
    read_more_words = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Pojknamn Footer Texts"

