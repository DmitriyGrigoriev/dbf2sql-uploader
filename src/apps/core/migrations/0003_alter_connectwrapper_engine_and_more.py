# Generated by Django 4.0.6 on 2022-07-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_importtables_upload_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectwrapper',
            name='engine',
            field=models.CharField(choices=[('django.db.backends.sqlite3', 'SQLite'), ('src.db.connection.advantage', 'DBF'), ('mssql', 'MSSQL')], default='mssql', max_length=200, verbose_name='Select engine'),
        ),
        migrations.AlterField(
            model_name='connectwrapper',
            name='name',
            field=models.CharField(max_length=250, verbose_name='NAME'),
        ),
        migrations.AddConstraint(
            model_name='connectwrapper',
            constraint=models.UniqueConstraint(fields=('engine', 'name'), name='unique_database_name'),
        ),
    ]
