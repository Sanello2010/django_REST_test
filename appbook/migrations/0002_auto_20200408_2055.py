# Generated by Django 3.0.5 on 2020-04-08 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='appbook.Book'),
        ),
    ]
