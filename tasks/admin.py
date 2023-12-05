from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import TaskItem
from django.urls import path



def mark_as_completed(modeladmin, request, queryset):
    queryset.update(completed=True)
mark_as_completed.short_description = "Mark selected tasks as completed"

def mark_as_not_completed(modeladmin, request, queryset):
    queryset.update(completed=False)
mark_as_not_completed.short_description = "Mark selected tasks as not completed"

@admin.register(TaskItem)
class TaskItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'completed')
    list_filter = ('completed', 'due_date')
    search_fields = ('title', 'description')
    ordering = ('due_date',)
    actions = [mark_as_completed, mark_as_not_completed]
