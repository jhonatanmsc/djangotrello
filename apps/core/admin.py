import pdb

from django.contrib import admin

from apps.core.models import Task, CheckList, Label, TaskList, Comment

admin.site.register(Task)
admin.site.register(CheckList)
admin.site.register(Label)
admin.site.register(TaskList)
admin.site.register(Comment)
