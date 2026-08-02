from django.contrib import admin

from .models import (
    Section,
    Unit,
    Boss,
)

admin.site.register(Section)
admin.site.register(Unit)
admin.site.register(Boss)