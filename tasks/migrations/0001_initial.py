# Generated by Django 5.1.4 on 2024-12-16 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TASK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(verbose_name='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comleted', models.BooleanField(default=False)),
            ],
        ),
    ]
