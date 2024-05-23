# Generated by Django 5.0.6 on 2024-05-22 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pereval_ID', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='autumn_lv',
        ),
        migrations.RemoveField(
            model_name='level',
            name='spring_lv',
        ),
        migrations.RemoveField(
            model_name='level',
            name='summer_lv',
        ),
        migrations.RemoveField(
            model_name='level',
            name='winter_lv',
        ),
        migrations.AddField(
            model_name='level',
            name='autumn_lev',
            field=models.CharField(choices=[('4A', 'winter'), ('2A', 'spring'), ('1A', 'summer'), ('3A', 'autumn')], default='4A', max_length=2),
        ),
        migrations.AddField(
            model_name='level',
            name='spring_lev',
            field=models.CharField(choices=[('4A', 'winter'), ('2A', 'spring'), ('1A', 'summer'), ('3A', 'autumn')], default='4A', max_length=2),
        ),
        migrations.AddField(
            model_name='level',
            name='summer_lev',
            field=models.CharField(choices=[('4A', 'winter'), ('2A', 'spring'), ('1A', 'summer'), ('3A', 'autumn')], default='4A', max_length=2),
        ),
        migrations.AddField(
            model_name='level',
            name='winter_lev',
            field=models.CharField(choices=[('4A', 'winter'), ('2A', 'spring'), ('1A', 'summer'), ('3A', 'autumn')], default='4A', max_length=2),
        ),
        migrations.AlterField(
            model_name='pereval_added',
            name='status',
            field=models.CharField(choices=[('NW', 'new'), ('PN', 'pending'), ('AC', 'accepted'), ('RJ', 'rejected')], default='NW', max_length=2),
        ),
    ]
