# Generated by Django 5.0.6 on 2024-07-17 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetForum', '0013_alter_question_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
