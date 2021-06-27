from django.db import models
from django.contrib.gis.db import models
# Create your models here.

class Province(models.Model):
    name = models.CharField(max_length=64, unique=True)
    population = models.IntegerField()
    pop_density = models.FloatField(verbose_name='People per sq. km')
    area_sq_km = models.FloatField(verbose_name='Land area, sq. km')

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class DistrictType(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "District Types"


class LocationType(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Location Types"


class District(models.Model):
    name = models.CharField(max_length=30, unique=True)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)
    district_type = models.ForeignKey(DistrictType, on_delete=models.DO_NOTHING)
    population = models.FloatField(null=True, blank=True)
    pop_density = models.FloatField(null=True, blank=True, verbose_name='People per sq. km')
    area_sq_km = models.FloatField(null=True, blank=True, verbose_name='Land area, sq. km')

    def get_province(self):
        return self.province.name

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class Constituency(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, null=True)
    population = models.FloatField(null=True, blank=True)
    pop_density = models.FloatField(null=True, blank=True, verbose_name='People per sq. km')
    area_sq_km = models.FloatField(null=True, blank=True, verbose_name='Land area, sq. km')


    # Returns the string representation of the model.
    def __str__(self): 
        return self.name

    def get_district(self):
        return self.district.name

    class Meta:
        verbose_name_plural = "Constituencies"


class Ward(models.Model):
    name = models.CharField(max_length=254)
    constituency = models.ForeignKey(Constituency, on_delete=models.DO_NOTHING, null=True, blank=True)
    population = models.FloatField(null=True, blank=True)
    pop_density = models.FloatField(null=True, blank=True, verbose_name='People per sq. km')
    area_sq_km = models.FloatField(null=True, blank=True, verbose_name='Land area, sq. km')

    def __str__(self):
        return self.name
