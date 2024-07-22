import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetForum', '0005_alter_answer_creationdate_alter_answer_updationdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='creationDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='answer',
            name='updationDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='question',
            name='creationDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='question',
            name='updationDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
