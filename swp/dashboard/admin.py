from django.contrib import admin
from .models import HostelAnnouncements, MessAnnouncements, MedicalAnnouncements, ImportantContacts

admin.site.register(HostelAnnouncements)
admin.site.register(MessAnnouncements)
admin.site.register(MedicalAnnouncements)
admin.site.register(ImportantContacts)
