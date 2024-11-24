# Generated by Django 4.2.16 on 2024-11-24 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_jobs_creator_alter_jobs_price_alter_jobs_task_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('experience', models.TextField()),
                ('soft_skills', models.TextField()),
                ('programming_languages', models.TextField()),
                ('education', models.CharField(max_length=255)),
                ('portfolio', models.FileField(blank=True, null=True, upload_to='portfolios/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='main.jobs')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
