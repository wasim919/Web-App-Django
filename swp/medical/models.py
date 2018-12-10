from django.db import models
from django.utils import timezone
# Create your models here.
class MedicalLeave(models.Model):
    leave_from=models.DateField(blank=True, null=True)
    leave_to=models.DateField(blank=True, null=True)
    student = models.ForeignKey('api_integration.Student', models.DO_NOTHING, blank=True, null=True)
    hometown=models.CharField(max_length=200)
    reason=models.TextField()
    timestamp = models.DateTimeField(default = timezone.now())
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    isDeleted = models.BooleanField(default = 0)

    def __str__(self):
        return '%s %s %s %s' % (self.student.user.username, self.leave_from, self.leave_to, self.reason)

    @property
    def isDelete(self):
        return bool(self.isDeleted())

class Doctors(models.Model):
    doctor_name=models.CharField(max_length=100,blank=True, null=True)
    specialisation=models.CharField(max_length=45,blank=True, null=True)
    date=models.DateField(blank=True, null=True)
    available_from=models.TimeField(blank=True, null=True)
    available_till=models.TimeField(blank=True, null=True)
    timestamp = models.DateTimeField(default = timezone.now())
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    isDeleted = models.BooleanField(default = 0)

    def __str__(self):
        return '%s %s' % (self.doctor_name,self.date)

    @property
    def isDelete(self):
        return bool(self.isDeleted())

class MedicalAppointment(models.Model):
    doctor=models.ForeignKey('medical.Doctors', models.DO_NOTHING, blank=True, null=True)
    student=models.ForeignKey('api_integration.Student', models.DO_NOTHING, blank=True, null=True)
    appointment_time=models.DateTimeField(blank=True, null=True)
    problem=models.TextField()
    age=models.IntegerField(blank=True, null=True)
    gender=models.CharField(max_length = 5,default="M")
    timestamp = models.DateTimeField(default = timezone.now())
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    isDeleted = models.BooleanField(default = 0)

    def __str__(self):
        return '%s %s' % (self.student.user.username,self.appointment_time)

    @property
    def isDelete(self):
        return bool(self.isDeleted())
