from django.db import models

class SchoolYear(models.Model):
    name = models.CharField(max_length=50)


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)


class SchoolYearAllowance(models.Model):
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)