# Generated by Django 5.2.3 on 2025-06-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('limit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('period', models.CharField(choices=[('Monthly', 'Monthly'), ('Weekly', 'Weekly')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=100)),
                ('target_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saved_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('deadline', models.DateField()),
            ],
        ),
    ]
