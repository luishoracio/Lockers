from django.db import models
from django.db.models.signals import post_save


class Users(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    user_name = models.CharField(max_length=50)
    user_ap = models.CharField(max_length=50)
    user_am = models.CharField(max_length=50)
    user_times = models.IntegerField(default=0)
    user_discount = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    user_match = models.CharField(max_length=50, null=True, blank=True)
    user_has_assigned_key = models.BooleanField(default=0)

# Nombre, first, last,
# Matricula
# Current ROM Code
# Llave asignada

class Areas(models.Model):
    area_id = models.IntegerField(primary_key=True)
    area_name = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        return self.area_name


class Lockers(models.Model):
    locker_id = models.IntegerField(primary_key=True)
    locker_name = models.CharField(max_length=20, null=True, blank=True)
    locker_match = models.CharField(max_length=50, null=True, blank=True)
    locker_status = models.IntegerField(default=0, null=True, blank=True)
    fk_area = models.ForeignKey('Areas')

    def __unicode__(self):
        return self.locker_id


class Rates(models.Model):
    rate_id = models.IntegerField(primary_key=True)
    rate_name = models.CharField(max_length=50, null=True, blank=True)
    rate_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    rate_unit = models.CharField(max_length=10)
    rate_currency = models.CharField(max_length=10, default='MXN', null=True, blank=True)

    def __unicode__(self):
        return self.rate_name


class Log(models.Model):
    log_number = models.AutoField(primary_key=True)
    log_timestamp = models.DateTimeField(auto_now=True)
    log_rate = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    log_discount = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    log_used_time = models.TimeField()
    fk_locker_id = models.ForeignKey('Lockers')
    fk_user_id = models.ForeignKey('Users')