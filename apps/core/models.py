from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.core.helpers import HistoryHelper


class CheckList(models.Model):
    name = models.CharField(max_length=100)
    itens = ArrayField(models.CharField(max_length=100), blank=True)

    def __str__(self):
        return f'<Checklist: {self.name}>'


class Label(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f'<Label: {self.name}>'


class TaskList(models.Model):
    name = models.CharField(max_length=100)
    pos = models.IntegerField()

    def __str__(self):
        return f'<TaskList: {self.name}>'


class Task(models.Model, HistoryHelper):
    name = models.CharField(max_length=100)
    descr = models.TextField(max_length=400, null=True, blank=True)
    due_date = models.DateTimeField(auto_now=True)
    pos = models.IntegerField()
    checklist = models.ManyToManyField(CheckList, 'tasks')
    members = models.ManyToManyField(User, 'tasks')
    labels = models.ManyToManyField(Label, 'tasks')
    task_list = models.ForeignKey(TaskList, models.CASCADE, 'tasks')
    files = ArrayField(models.FileField(upload_to='uploads/tasks/'), blank=True)

    def __str__(self):
        return f'<Task: {self.name}>'


class Comment(models.Model, HistoryHelper):
    owner = models.ForeignKey(User, models.CASCADE, 'comments')
    descr = models.TextField(max_length=400)
    reactions = ArrayField(models.CharField(max_length=50), blank=True)
    task = models.ForeignKey(Task, models.CASCADE, 'comments')

    def __str__(self):
        return f'<Comment: {self.owner.name}->{self.task.name}>'
