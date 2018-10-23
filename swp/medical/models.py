from django.db import models

# Create your models here.
class MedicalLeave(models.Model):
    leave_from=models.DateField(blank=True, null=True)
    leave_to=models.DateField(blank=True, null=True)
    student = models.ForeignKey('accounts.Student', models.DO_NOTHING, blank=True, null=True)
    hometown=models.CharField(max_length=200)
    reason=models.TextField()
    timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return '%s %s %s %s' % (self.student.user.username, self.leave_from, self.leave_to, self.reason)
