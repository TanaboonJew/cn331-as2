# Generated by Django 4.2.5 on 2023-10-08 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('class_code', models.CharField(max_length=10, unique=True)),
                ('class_semester', models.CharField(max_length=20)),
                ('class_year', models.PositiveIntegerField()),
                ('class_max_enroll', models.PositiveIntegerField()),
                ('class_status', models.CharField(choices=[('open', 'Open'), ('close', 'Close'), ('full', 'Open but full')], default='open', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enrollment.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
