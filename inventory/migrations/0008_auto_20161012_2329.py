# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 06:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

from django.db import migrations, models

from inventory.models import Inventory
from server.models import Machine


def clean_inventory(apps, schema_editor):
    Inventory = apps.get_model("inventory", "Inventory")
    Machine = apps.get_model("server", "Machine")
    for machine in Machine.objects.all():
        all_inventory = Inventory.objects.filter(machine=machine)
        if all_inventory.count() != 0:
            first_inventory = Inventory.objects.filter(
                machine=machine)[:1].values_list("id", flat=True)
            Inventory.objects.filter(machine=machine).exclude(pk__in=list(first_inventory)).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20160915_0243'),
    ]

    operations = [
        migrations.RunPython(clean_inventory),
        migrations.AlterField(
            model_name='inventory',
            name='machine',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to='server.Machine'),
        ),
    ]
