# Generated by Django 4.1.7 on 2023-04-01 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_note_alter_choice_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='timestamp',
            field=models.CharField(default='11:15 PM', max_length=20),
        ),
    ]