# Generated by Django 4.0.4 on 2022-05-29 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_accessory_alter_reading_options_alter_book_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='accessorys',
            field=models.ManyToManyField(to='main_app.accessory'),
        ),
    ]
