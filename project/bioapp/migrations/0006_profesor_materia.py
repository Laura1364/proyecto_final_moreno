# Generated by Django 5.0 on 2023-12-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bioapp', '0005_remove_profesor_email_profesor_apellido'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='materia',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
