from django.db import models


# Create your models here.
class Master(models.Model):
    name = models.CharField('name', max_length=100)
    timetable = models.TextField('timetable')
    phone_number = models.CharField('phone_number', max_length=100)

    def get_weekday(self, num):
        return [i.split(',') for i in str(self.timetable).split(";")][num]


class Appointment(models.Model):
    owner_name = models.CharField('owner_name', max_length=100)
    date = models.DateTimeField('Date')
    master_name = models.ForeignKey(Master, on_delete=models.CASCADE)
