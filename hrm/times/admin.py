from django.contrib import admin
from times.models import Adata,EmpMst


class AdataAdmin(admin.ModelAdmin):
    list_display = ('emp_id','cardno',)

class EmpMstAdmin(admin.ModelAdmin):
    list_display = ('empid','ename','orgid','edept','bdate','jdate',)

admin.site.register(Adata,AdataAdmin)
admin.site.register(EmpMst,EmpMstAdmin)

# Register your models here.
