from django.db import models

# Create your models here.

class Player (models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    handicap = models.FloatField()

    def __unicode__(self):
        return u"%s%" % Player.name    

class Field(models.Model):
    holes = models.IntegerField()
    par = models.IntegerField()


class Hole (models.Model):
    field = models.ForeignKey(Field)
    hole_number = models.IntegerField()
    meters = models.IntegerField()
    handicap_hole = models.IntegerField()


class Match (models.Model):
    hole = models.ForeignKey(Hole)
    hole_result = models.IntegerField()
    total_result = models.IntegerField()

class Rules (models.Model):
    rules = models.TextField()
    
    def __unicode__(self):
        return u"%s%" % self.rules
