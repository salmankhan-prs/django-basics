from django.contrib import admin
from .models import ChaiVariety,ChaiReview,ChaiCertificates,Store
# Register your models here.

class ChaiReviewInLine(admin.TabularInline):
    model = ChaiReview
    extra = 2 
    

class ChaiCertificatesInLine(admin.TabularInline):
    model = ChaiCertificates
    extra = 1
    
    
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added')
    inlines =[ChaiReviewInLine,ChaiCertificatesInLine]
    
class StoreAdmin(admin.ModelAdmin):
    list_display =('name','location')
    filter_horizontal = ('chai_varieties',)
    
    
class ChaiCertificatesAdmin(admin.ModelAdmin):
    list_display =('chai','certificate_number')
        

    
    
    
admin.site.register(ChaiVariety,ChaiVarietyAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(ChaiCertificates,ChaiCertificatesAdmin)
