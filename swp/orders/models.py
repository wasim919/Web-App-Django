from django.db import models
from django.utils import timezone
class Items(models.Model):
    item_name = models.CharField(max_length=45, blank=False, null=False, unique = True)
    item_type = models.CharField(max_length=45, blank=False, null=False)
    cost = models.FloatField(blank=False, null=False)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now())
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    delete = models.BooleanField(default = 0)

    def __str__(self):
        return "{} {}".format(self.item_type, self.item_name)

    @property
    def isDeleted(self):
        return bool(self.delete())

class ManualOrder(models.Model):
    order_name = models.CharField(max_length=45, blank=False, null=False)
    order_type = models.CharField(max_length=45, blank=False, null=False)
    timestamp = models.DateTimeField(default =timezone.now())
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    delete = models.BooleanField(default = 0)

    def __str__(self):
        return "{} {}".format(self.order_type, self.order_name)

    @property
    def isDeleted(self):
        return bool(self.delete())

class OrderList(models.Model):
    student = models.ForeignKey('api_integration.Student', models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey('Items', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now())
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    delete = models.BooleanField(default = 0)

    def __str__(self):
        return "{}".format(self.student.user.username)

    @property
    def isDeleted(self):
        return bool(self.delete())

class OrderHistory(models.Model):
    student = models.ForeignKey('api_integration.Student', models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(default = timezone.now())
    created_at = models.DateField(blank=True, null=True, auto_now_add=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)
    delete = models.BooleanField(default = 0)

    def __str__(self):
        return "{} {} {}".format(self.student.user.username, self.item.item_type, self.item.item_name)

    @property
    def isDeleted(self):
        return bool(self.delete())
