# Generated by Django 4.0 on 2022-01-07 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_gallery_art'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='description',
        ),
        migrations.CreateModel(
            name='ArtworkPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('artwork', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.artwork')),
            ],
        ),
    ]
