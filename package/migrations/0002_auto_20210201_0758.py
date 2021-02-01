# Generated by Django 3.1.5 on 2021-02-01 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='package.order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='package',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='package.package'),
        ),
    ]