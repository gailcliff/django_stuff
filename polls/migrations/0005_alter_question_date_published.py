# Generated by Django 4.1.7 on 2023-03-25 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_question_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_published',
            field=models.DateTimeField(default='django.utils.timezone.now'),
        ),
    ]