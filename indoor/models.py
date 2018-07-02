from django.db import models
from django.contrib.auth.models import User
from datetime import date

class IndoorRouteAscent(models.Model):
    REDPOINT = 'RP'
    FLASH = 'FL'
    ONSIGHT = 'ON'
    REPEAT = 'RE'
    ASCENT_TYPE_CHOICES = (
        ('RP', 'Redpoint'),
        ('FL', 'Flash'),
        ('ON', 'Onsight'),
        ('RE', 'Repeat')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    ascent_type = models.CharField(
        max_length=2,
        choices=ASCENT_TYPE_CHOICES,
        default=REDPOINT
    )
    grade = models.SmallIntegerField()

    def __str__(self):
        return "%s - %s - %s" % (str(self.date), str(self.grade), str(self.ascent_type))

class IndoorBoulderAscent(models.Model):
    SEND = 'SN'
    FLASH = 'FL'
    ONSIGHT = 'ON'
    REPEAT = 'RE'
    ASCENT_TYPE_CHOICES = (
        ('SN', 'Send'),
        ('FL', 'Flash'),
        ('ON', 'Onsight'),
        ('RE', 'Repeat')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    ascent_type = models.CharField(
        max_length=2,
        choices=ASCENT_TYPE_CHOICES,
        default=SEND
    )
    grade = models.SmallIntegerField()

    def __str__(self):
        return "%s - %s - %s" % (str(self.date), str(self.grade), str(self.ascent_type))

