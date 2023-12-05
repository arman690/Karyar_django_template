from django.contrib import admin
from django.urls import path
from tasks.views import MyTaskListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('mytask/list', MyTaskListView.as_view(), name='mytask_list'),
]
