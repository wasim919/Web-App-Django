from django.db import models

class HostelAnnouncements(models.Model):
    announcement_title = models.CharField(max_length=30, blank=True, null=True)
    announcement = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return str(self.announcement_title3)

class MessAnnouncements(models.Model):
    announcement_title = models.CharField(max_length=30, blank=True, null=True)
    announcement = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return str(self.announcement_title)

class MedicalAnnouncements(models.Model):
    announcement_title = models.CharField(max_length=30, blank=True, null=True)
    announcement = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return str(self.announcement_title)

class ImportantContacts(models.Model):
    name = models.CharField(max_length = 30, blank = False)
    mobile = models.CharField(max_length = 13, blank = False)
    email = models.EmailField(max_length = 70, blank = False)

    def __str__(self):
        return str(self.name)
