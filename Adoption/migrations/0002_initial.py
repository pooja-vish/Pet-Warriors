# Generated by Django 5.0.6 on 2024-07-22 20:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Adoption', '0001_initial'),
        ('PetForum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoption',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PetForum.member'),
        ),
    ]
