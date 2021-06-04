from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    group = models.ForeignKey(Group,
                                 on_delete=models.CASCADE)
    name = models.TextField(max_length=128)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

