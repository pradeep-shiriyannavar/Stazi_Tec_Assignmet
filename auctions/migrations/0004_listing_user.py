# Generated by Django 3.2.5 on 2021-07-14 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210710_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='auctions.user'),
            preserve_default=False,
        ),
    ]
