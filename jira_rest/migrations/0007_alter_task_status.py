# Generated by Django 4.2 on 2023-06-18 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jira_rest', '0006_task_assignee_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('IN_WORK', 'IN_WORK'), ('FREE', 'FREE'), ('IN_REVIEW', 'IN_REVIEW'), ('DONE', 'DONE')], max_length=100, null=True),
        ),
    ]
