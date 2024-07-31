from __future__ import unicode_literals
from django.db import models



class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "{}-{}-{}".format(self.date, self.user, self.amount)


class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "{}-{}-{}".format(self.date, self.user, self.amount)
