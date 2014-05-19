from django.db import models


class ClassPh(models.Model):
    # placeholder
    name = models.CharField(max_length=200)


class ClassPl(models.Model):
    # plugin
    name = models.CharField(max_length=200)
    z = models.ForeignKey(ClassPh)

    class Meta:
        unique_together = ('name', 'z')


class ClassPg(models.Model):
    # page
    name = models.CharField(max_length=200)
    z = models.ManyToManyField(ClassPh)


class ClassT(models.Model):
    # title
    name = models.CharField(max_length=200)
    z = models.ForeignKey(ClassPg)
