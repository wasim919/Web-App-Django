from django.db import models

class Items(models.Model):
    item_name = models.CharField(max_length=45, blank=False, null=False)
    item_type = models.CharField(max_length=45, blank=False, null=False)
    cost = models.FloatField(blank=False, null=False)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.item_type, self.item_name)

class ManualOrder(models.Model):
    order_name = models.CharField(max_length=45, blank=False, null=False)
    order_type = models.CharField(max_length=45, blank=False, null=False)
    timestamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.order_type, self.order_name)

class OrderList(models.Model):
    student = models.ForeignKey('accounts.Student', models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.student.user.username, self.item.item_name)


class OrderHistory(models.Model):
    student = models.ForeignKey('accounts.Student', models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    modified_at = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.student.user.username, self.item.item_type, self.item.item_name)
