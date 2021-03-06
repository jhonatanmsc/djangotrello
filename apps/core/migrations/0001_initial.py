# Generated by Django 3.0.7 on 2020-06-28 16:11

import apps.core.helpers
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('itens', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descr', models.TextField(blank=True, max_length=400, null=True)),
                ('due_date', models.DateTimeField(auto_now=True)),
                ('pos', models.IntegerField()),
                ('files', django.contrib.postgres.fields.ArrayField(base_field=models.FileField(upload_to='uploads/tasks/'), blank=True, size=None)),
                ('checklist', models.ManyToManyField(related_name='tasks', to='core.CheckList')),
                ('labels', models.ManyToManyField(related_name='tasks', to='core.Label')),
                ('members', models.ManyToManyField(related_name='tasks', to=settings.AUTH_USER_MODEL)),
                ('task_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='core.TaskList')),
            ],
            bases=(models.Model, apps.core.helpers.HistoryHelper),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.TextField(max_length=400)),
                ('reactions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.Task')),
            ],
            bases=(models.Model, apps.core.helpers.HistoryHelper),
        ),
    ]
