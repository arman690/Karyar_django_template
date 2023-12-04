from django.contrib import admin
from django.db.models import Count
from django.shortcuts import render
from .models import TaskItem

class TaskItemAdmin(admin.ModelAdmin):
    actions = ['mark_completed', 'mark_not_completed']

    def mark_completed(self, request, queryset):
        queryset.update(task_finished=True)
    mark_completed.short_description = "Mark selected tasks as completed"

    def mark_not_completed(self, request, queryset):
        queryset.update(task_finished=False)
    mark_not_completed.short_description = "Mark selected tasks as not completed"

# Register TaskItem with the default admin site
admin.site.register(TaskItem, TaskItemAdmin)

# The following code sets up a custom admin view for task summary
# It doesn't affect the ability to edit tasks in the default admin

class CustomAdminSite(admin.AdminSite):
    site_header = 'Your Custom Admin Header'  # Optional: Set the header text

    def get_urls(self):
        from django.urls import path
        from .views import task_summary_view

        urls = super().get_urls()
        custom_urls = [
            path('task-summary/', self.admin_view(task_summary_view), name='task_summary'),
        ]
        return urls + custom_urls

admin_site = CustomAdminSite(name='custom_admin')
