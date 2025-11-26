from django.contrib import admin

from users.models import Branch, Customer, User

admin.site.register(Branch)
admin.site.register(Customer)
admin.site.register(User)
