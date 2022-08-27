# Generated by Django 4.0.6 on 2022-08-26 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_connectset_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectwrapper',
            name='host',
            field=models.CharField(blank=True, max_length=100, verbose_name='HOST'),
        ),
        migrations.AlterField(
            model_name='connectwrapper',
            name='port',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='PORT'),
        ),
    ]
