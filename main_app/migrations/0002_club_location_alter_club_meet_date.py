# Generated by Django 4.0.1 on 2022-01-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='location',
            field=models.CharField(choices=[('-', 'No meeting place assigned to this club'), ('a', '1st Floor Auditorium'), ('b', '1st Floor Large Study Room'), ('c', '2nd Floor Meeting Room')], default='-', max_length=1),
        ),
        migrations.AlterField(
            model_name='club',
            name='meet_date',
            field=models.DateField(blank=True),
        ),
    ]
