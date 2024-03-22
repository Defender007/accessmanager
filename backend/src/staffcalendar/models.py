from django.db import models

from users.models import Batch, UserProfile

# from users.models import UserProfile


# Create your models here.
class ShiftType(models.Model):
    name = models.CharField(max_length=128, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.PositiveSmallIntegerField()
    # start_date = models.DateField()
    # end_date = models.DateField()
    # user = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)


class WorkDay(models.Model):
    day_symbol = models.CharField(max_length=10)
    day_code = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = (("day_symbol", "day_code"),)
        ordering = ["day_code"]

    def __str__(self):
        return f"{self.day_symbol}"


class MonthlyRoster(models.Model):
    work_day = models.ForeignKey(WorkDay, null=True, on_delete=models.SET_NULL)
    shift = models.ForeignKey(ShiftType, null=True, on_delete=models.SET_NULL)
    week_start_date = models.DateField()
    batch = models.ForeignKey(Batch, related_name="roster", on_delete=models.CASCADE)
    shift_start_date = models.DateField()
    shift_end_date = models.DateField()

    class Meta:
        verbose_name = "Employees' roster"
        # unique_together = (("shift_start_date", "work_day", "shift", "batch"),)

    def __str__(self):
        return f"{self.shift.name.capitalize()} | {self.batch} | {self.work_day.day_symbol}"
