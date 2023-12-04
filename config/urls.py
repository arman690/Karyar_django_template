from django.urls import path
from tasks.views import MyTaskListView
from tasks.admin import CustomAdminSite

# Create a custom admin site instance
admin_site = CustomAdminSite(name='admin')

urlpatterns = [
    # Admin URL
    path('admin/', admin_site.urls),

    # MyTaskListView URL
    path('mytask/list/', MyTaskListView.as_view(), name='mytask_list'),

    # Custom admin view URL for task summary
    path('admin/task-summary/', admin_site.task_summary, name='task_summary'),
]

