# Generated by Django 4.2.4 on 2023-08-10 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('deleted', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('deleted', models.DateField(auto_now=True)),
                ('description', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Measure Unit',
                'verbose_name_plural': 'Measure Units',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('deleted', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Product name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Product description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Product image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateField(blank=True, editable=False)),
                ('modified', models.DateField(blank=True, editable=False)),
                ('deleted', models.DateField(blank=True, editable=False)),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Product name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Product description')),
                ('image', models.TextField(blank=True, max_length=100, null=True, verbose_name='Product image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Product',
                'verbose_name_plural': 'historical Products',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMeasureUnit',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateField(blank=True, editable=False)),
                ('modified', models.DateField(blank=True, editable=False)),
                ('deleted', models.DateField(blank=True, editable=False)),
                ('description', models.CharField(db_index=True, max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Measure Unit',
                'verbose_name_plural': 'historical Measure Units',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDiscount',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateField(blank=True, editable=False)),
                ('modified', models.DateField(blank=True, editable=False)),
                ('deleted', models.DateField(blank=True, editable=False)),
                ('discount_value', models.PositiveSmallIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.category')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Discount',
                'verbose_name_plural': 'historical Discounts',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCategory',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateField(blank=True, editable=False)),
                ('modified', models.DateField(blank=True, editable=False)),
                ('deleted', models.DateField(blank=True, editable=False)),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('description', models.CharField(blank=True, db_index=True, max_length=50, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('measure_unit', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.measureunit', verbose_name='measure unit')),
            ],
            options={
                'verbose_name': 'historical Category',
                'verbose_name_plural': 'historical Categories',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('deleted', models.DateField(auto_now=True)),
                ('discount_value', models.PositiveSmallIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'verbose_name': 'Discount',
                'verbose_name_plural': 'Discounts',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='measure_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='measure unit'),
        ),
    ]
