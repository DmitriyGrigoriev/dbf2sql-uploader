# Generated by Django 4.0.6 on 2022-12-13 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlimport', '0006_alter_tdcltrans_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tdclplatr',
            name='hash',
            field=models.CharField(db_index=True, max_length=64, null=True),
        ),
    ]
