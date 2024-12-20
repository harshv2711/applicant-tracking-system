from django.contrib import admin
from .models import ClientViewPermission

# Register your models here.
@admin.register(ClientViewPermission)
class ClientViewPermission(admin.ModelAdmin):
    list_display = [
        "client__email",
        "company_profile__company_name",
        "allow"
    ]   

    search_fields = [
        "client__email",
        "company_profile__company_name",
        "allow"
    ]

    list_filter = [
        "company_profile__company_name",
        "allow"
    ]