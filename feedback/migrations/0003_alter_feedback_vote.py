# Generated by Django 4.2 on 2024-09-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_feedback_delete_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='vote',
            field=models.CharField(choices=[('U', 'Up'), ('D', 'Down')], max_length=1),
        ),
    ]
