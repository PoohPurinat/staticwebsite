# Generated by Django 4.2 on 2023-05-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('detail', models.TextField(blank=True, null=True)),
                ('done', models.BooleanField(default=False)),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
