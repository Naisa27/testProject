# Generated by Django 4.1.5 on 2023-01-15 12:19

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0004_rename_level_menu_mptt_level_menu_sort'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('menuPoint', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sam.menu')),
            ],
        ),
    ]
