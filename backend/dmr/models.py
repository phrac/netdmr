from django.db import models


# Create your models here.
class Outfall(models.Model):
    number = models.IntegerField()
    location = models.TextField(null=True)
    description = models.TextField()

    def __str__(self):
        return "%s: %s" % (self.number, self.location)


class DailyReading(models.Model):
    outfall = models.ForeignKey(Outfall, null=True, on_delete=models.CASCADE)
    date = models.DateField(unique=True)
    flow = models.FloatField()
    ph_start = models.FloatField(null=True, blank=True)
    ph_mid = models.FloatField(null=True, blank=True)
    ph_end = models.FloatField(null=True, blank=True)

    gallons = models.FloatField(null=True, blank=True)
    units = models.FloatField(null=True, blank=True)
    hour_avg = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.gallons = self.flow * 264.172
        self.units = self.gallons / 748
        self.hour_avg = self.gallons / 24
        super(DailyReading, self).save(*args, **kwargs)

    def __str__(self):
        return "%s: %s" % (self.outfall, self.date)
