from django.views.generic import ListView
from .models import TaskItem

class MyTaskListView(ListView):
    model = TaskItem
    template_name = 'tasks/mytask_list.html'
