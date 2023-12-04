# Generated by Django 4.2.7 on 2023-12-04 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('task_finished', models.BooleanField(default=True)),
            ],
        ),
    ]
