from django.db import models
import datetime
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))


class Doujinshi(models.Model):
    titre = models.CharField(max_length=200)
    annee = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    serie = models.ManyToManyField('Serie')
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.titre


class Auteur(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Serie(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.ForeignKey('Auteur', on_delete=models.PROTECT)

    def __str__(self):
        return self.titre


class Tag(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class DoujinshiImage(models.Model):
    doujinshi = models.ForeignKey('Doujinshi', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/doujinshi/%Y/%m/%d/')
