from django.contrib import admin
from .models import Post, Invite, AMOS


admin.site.register(Post)



class InviteAdmin(admin.ModelAdmin):
    list_display = ("name", "branch", "gender", "date_of_birth", "race")
    list_filter = ("branch", "gender", "race")
    search_fields = ("name",)


class AMOSlist(admin.ModelAdmin):
    list_display = ("dataSource", "has_errors", "exec_start", "exec_end")
    list_filter = ("dataSource", "has_errors")
    search_fields = ("dataSource",)


admin.site.register(Invite, InviteAdmin)
admin.site.register(AMOS, AMOSlist)