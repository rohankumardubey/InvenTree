# Generated by Django 3.2.13 on 2022-05-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0074_alter_stockitem_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitem',
            name='metadata',
            field=models.JSONField(blank=True, help_text='JSON metadata field, for use by external plugins', null=True, verbose_name='Plugin Metadata'),
        ),
        migrations.AddField(
            model_name='stocklocation',
            name='metadata',
            field=models.JSONField(blank=True, help_text='JSON metadata field, for use by external plugins', null=True, verbose_name='Plugin Metadata'),
        ),
        migrations.AlterUniqueTogether(
            name='stocklocation',
            unique_together=set(),
        ),
    ]
