# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from access.models import *

class SecurityNodeAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Group', 'id',)
    readonly_fields = ('id',)

class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('User', 'Node', 'In', 'Out')
    list_filter = ('In', 'Out',)
    search_fields = ('User__username', 'Node__Name', 'In', 'Out',)
    readonly_fields = ('User', 'Node', 'In', 'Out', 'Force_Out',)


class TagAdmin(admin.ModelAdmin):
    readonly_fields=('Date_Added',)
    list_display = ('Uuid', 'User', 'Date_Added',)
    list_filter = ('Date_Added',)
    search_fields = ('User__username',)

class AclInline(admin.TabularInline):
    model = Acl
    can_delete = False
    filter_horizontal = ('Allowed_Nodes',)

class UserAdmin(UserAdmin):
    inlines = (AclInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(SecurityNode, SecurityNodeAdmin)
admin.site.register(AccessLog, AccessLogAdmin)