from django.contrib import admin

# Register your models here.
from .models import Instrument, TimeSeriesDatum, Tag

admin.site.register(Instrument)
admin.site.register(TimeSeriesDatum)
admin.site.register(Tag)
