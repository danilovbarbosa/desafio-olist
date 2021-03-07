# Generated by Django 3.1.7 on 2021-03-07 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fantasy_name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=15)),
                ('complete_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.address')),
            ],
        ),
    ]
