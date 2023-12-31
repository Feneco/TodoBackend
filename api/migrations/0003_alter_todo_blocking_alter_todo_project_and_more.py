# Generated by Django 4.2.3 on 2023-07-14 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_project_todo_delete_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='blocking',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.todo'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='project',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.project'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='to_date',
            field=models.DateTimeField(blank=True, verbose_name='Assigned date'),
        ),
    ]
