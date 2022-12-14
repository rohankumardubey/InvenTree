# Generated by Django 3.2.4 on 2021-07-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0047_auto_20210701_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='reference',
            field=models.CharField(default="PO", help_text='Order reference', max_length=64, unique=True, verbose_name='Reference'),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='reference',
            field=models.CharField(default="SO", help_text='Order reference', max_length=64, unique=True, verbose_name='Reference'),
        ),
    ]
