from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
#Complaint Register
#Courier
#Hostel Leave

class HostelLeave(models.Model):
    leave_from=models.DateField(blank=True, null=True)
    leave_to=models.DateField(blank=True, null=True)
    student = models.ForeignKey('api_integration.Student', models.DO_NOTHING, blank=True, null=True)
    hometown=models.CharField(max_length=200)
    reason=models.TextField()
    timestamp = models.DateTimeField(default = timezone.now())
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    delete = models.BooleanField(default = 0)

    def __str__(self):
        return '%s %s %s %s' % (self.student.user.username, self.leave_from, self.leave_to, self.reason)

    @property
    def isDeleted(self):
        return bool(self.delete())

class ComplaintRegister(models.Model):
    idcomplaint_register = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=200, blank=True, null=True)
    student = models.ForeignKey('api_integration.Student', models.DO_NOTHING, blank=True, null=True)
    room_no = models.IntegerField(blank=True, null=True)
    comp_img = models.ImageField(upload_to='images/'+str(datetime.now()),blank=True,null=True)
    completed = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(default = timezone.now())
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    delete = models.BooleanField(default = 0)

    def __str__(self):
    	return '%s %s %s %s' %(self.student.user.username,self.room_no,self.complaint,self.timestamp)

    @property
    def isDeleted(self):
        return bool(self.delete())

class Courrier(models.Model):
    idcourrier = models.AutoField(primary_key=True)
    courrier_ref_no = models.CharField(max_length=45, blank=True, null=True)
    delivery_agent = models.CharField(max_length=45, blank=True, null=True)
    student = models.ForeignKey('api_integration.Student', models.DO_NOTHING, blank=True, null=True)
    courrier_company = models.CharField(max_length=45, blank=True, null=True)
    expected_arrival_time = models.DateTimeField(blank=True, null=True)
    timestamp = models.DateTimeField(default = timezone.now())
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    delete = models.BooleanField(default = 0)

    def __str__(self):
    	return '%s %s %s' %(self.student.user.username,self.idcourrier,self.expected_arrival_time)
    
    @property
    def isDeleted(self):
        return bool(self.delete())

class SelfHelpGroup(models.Model):
    issue = models.CharField(max_length=100,blank=True,null=True)
    student = models.ForeignKey('api_integration.Student', models.DO_NOTHING, blank=True, null=True)
    timestamp = models.DateTimeField(default = timezone.now())
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    delete = models.BooleanField(default = 0)

    def __str__(self):
        return '%s %s' %(self.issue,self.student.user.username)

    @property
    def isDeleted(self):
        return bool(self.delete())
