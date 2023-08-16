from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    Document,
    Institution,
    InstitutionType,
    Category,
    DocumentType
)
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin


class LogEntryAdmin(admin.ModelAdmin):
    # to have a date-based drilldown navigation in the admin page
    date_hierarchy = 'action_time'

    # to filter the resultes by users, content types and action flags
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_repr',
        'action_flag',
    ]

class CustomUserAdmin(BaseUserAdmin):
    list_display = BaseUserAdmin.list_display + ('group_list', )

    def group_list(self, obj):
        """
        get group, separate by comma, and display empty string if user has no group
        """
        return ','.join([g.name for g in obj.groups.all()]) if obj.groups.count() else ''


class DocumentResource(resources.ModelResource):

    institution = fields.Field(
        column_name='institution',
        attribute='institution',
        widget=ForeignKeyWidget(Institution, 'name')
    )
    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name')
    )
    type = fields.Field(
        column_name='type',
        attribute='type',
        widget=ForeignKeyWidget(DocumentType, 'name')
    )

    class Meta:
        model = Document
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'institution', 'category', 'type', 'title', 'year', 'publisher', 'note', 'url')


class CustomDocumentAdmin(ImportExportModelAdmin):
    resource_class = DocumentResource


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Document, CustomDocumentAdmin)
admin.site.register(Institution)
admin.site.register(InstitutionType)
admin.site.register(Category)
admin.site.register(DocumentType)
admin.site.register(LogEntry, LogEntryAdmin)
