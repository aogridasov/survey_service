# Generated by Django 2.2 on 2023-03-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0003_auto_20230317_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='coins_value',
            field=models.SmallIntegerField(default=10, verbose_name='Награда'),
            preserve_default=False,
        ),
    ]
