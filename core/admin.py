from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import * 
from django.contrib.sessions.models import Session



# Register your models here.
admin.site.register(issues) 
admin.site.register(avail) 
admin.site.register(verify)
admin.site.register(Session)

admin.site.register(comment)

@admin.register(assignhelpline)
class anyname3(ImportExportModelAdmin):
     pass
admin.register(assignhelpline)


@admin.register(helplines)
class anyname2(ImportExportModelAdmin):
     pass
admin.register(helplines)



@admin.register(feedback)
class anyname(ImportExportModelAdmin):
     pass
admin.register(feedback)