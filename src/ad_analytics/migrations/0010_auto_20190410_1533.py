# Generated by Django 2.1.7 on 2019-04-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_analytics', '0009_auto_20190409_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impression',
            name='cost_per_impression_usd',
            field=models.DecimalField(decimal_places=10, max_digits=20, null=True),
        ),
    ]