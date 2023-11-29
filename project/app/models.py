# models.py
from django.db import models


class FrontTimesChallenge(models.Model):
    input_string = models.CharField(max_length=100)
    n = models.IntegerField()


class NoTeenSumChallenge(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()


class XYZThereChallenge(models.Model):
    input_string = models.CharField(max_length=100)


class CenteredAverageChallenge(models.Model):
    nums = models.CharField(max_length=100)
