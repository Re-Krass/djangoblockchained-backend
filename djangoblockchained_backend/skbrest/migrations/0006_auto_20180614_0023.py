# Generated by Django 2.0.6 on 2018-06-13 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skbrest', '0005_remove_resource_size'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anouncement',
            options={'ordering': ['-date'], 'verbose_name': 'Anouncement', 'verbose_name_plural': 'Anouncements'},
        ),
        migrations.AlterField(
            model_name='anouncement',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
