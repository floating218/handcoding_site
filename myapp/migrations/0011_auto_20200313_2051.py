# Generated by Django 3.0.4 on 2020-03-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_screen_screen_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='screen_id',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='screen',
            name='screen_num',
            field=models.CharField(default='none', max_length=200, primary_key=True, serialize=False),
        ),
    ]