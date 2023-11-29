from django.contrib import admin
from Users.models import Users
from django.contrib.auth import admin as admin_auth_django
from Users.forms import UserChangeForm, UserCreationForm

@admin.register(Users)
class CustomUserAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Cargo', {'fields': ('cargo',)}),
    )
