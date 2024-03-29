# Generated by Django 2.2.4 on 2019-08-10 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appliances', '0002_auto_20190810_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliance',
            name='status',
            field=models.CharField(choices=[('UP', 'Up'), ('DOWN', 'Down')], default='DOWN', max_length=15),
        ),
        migrations.AlterField(
            model_name='appliancelink',
            name='dst_appliance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dst_links', to='appliances.Appliance', verbose_name='destination appliance'),
        ),
        migrations.AlterField(
            model_name='appliancelink',
            name='src_appliance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='src_links', to='appliances.Appliance', verbose_name='source appliance'),
        ),
    ]
