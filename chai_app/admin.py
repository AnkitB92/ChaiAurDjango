from django.contrib import admin
from .models import ChaiVariety, ChaiReview, Store, ChaiCertificate

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
  model = ChaiReview
  extra = 1


class ChaiVarietyAdmin(admin.ModelAdmin):
  list_display = ('name', 'type', 'added_on', 'price')
  inlines = [ChaiReviewInline]


class StoreAdmin(admin.ModelAdmin):
  list_display = ('name', 'location',)
  filter_horizontal = ('chai_varieties',)


class ChaiCertificateAdmin(admin.ModelAdmin):
  list_display = ('chai', 'serial_number', 'issued_date',)


admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
