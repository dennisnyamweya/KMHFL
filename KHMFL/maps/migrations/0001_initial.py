# Generated by Django 3.0 on 2021-06-27 08:04

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('population', models.FloatField(blank=True, null=True)),
                ('pop_density', models.FloatField(blank=True, null=True, verbose_name='People per sq. km')),
                ('area_sq_km', models.FloatField(blank=True, null=True, verbose_name='Land area, sq. km')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Constituencies',
            },
        ),
        migrations.CreateModel(
            name='DistrictType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
            options={
                'verbose_name_plural': 'District Types',
            },
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Location Types',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('population', models.IntegerField()),
                ('pop_density', models.FloatField(verbose_name='People per sq. km')),
                ('area_sq_km', models.FloatField(verbose_name='Land area, sq. km')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('population', models.FloatField(blank=True, null=True)),
                ('pop_density', models.FloatField(blank=True, null=True, verbose_name='People per sq. km')),
                ('area_sq_km', models.FloatField(blank=True, null=True, verbose_name='Land area, sq. km')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('constituency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maps.Constituency')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('population', models.FloatField(blank=True, null=True)),
                ('pop_density', models.FloatField(blank=True, null=True, verbose_name='People per sq. km')),
                ('area_sq_km', models.FloatField(blank=True, null=True, verbose_name='Land area, sq. km')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('district_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='maps.DistrictType')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='maps.Province')),
            ],
        ),
        migrations.AddField(
            model_name='constituency',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='maps.District'),
        ),
    ]
