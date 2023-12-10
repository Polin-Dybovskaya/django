from django.db import models
from django.contrib.auth.models import User


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(**kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Direction(models.Model):
    name = models.CharField(max_length=50, primary_key=True, verbose_name="name_direction",
                            help_text="Введите название направления", null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return "Институт " + self.name

    class Meta:
        db_table = "Direction"


class Group(models.Model):
    name = models.CharField(max_length=20, verbose_name="group name",
                            help_text="Введите название курса", null=False, blank=False)
    course = IntegerRangeField(min_value=1, max_value=5, verbose_name="number course",
                               help_text="Ввелите номер курса", null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Group"


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name="student name",
                                  help_text="Введите имя студента ", null=True, blank=False)
    first_name = models.CharField(max_length=50, verbose_name="student name",
                                  help_text="Введите имя студента ", null=True, blank=False)
    last_name = models.CharField(max_length=100, verbose_name="student last name",
                                 help_text="Введите фамилию студента ", null=False, blank=False)
    date_birth = models.DateField()  # verbose_name="date birth", help_text="Введите дату рождения студента",null=True, blank=True
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="group",
                              help_text="Введите группу студента ", null=False, blank=False)

    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="id User", help_text="выберите id",
                                null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = "Student"


class Tutor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name="tutor name",
                                  help_text="Введите имя преподавателя ", null=False, blank=False)
    last_name = models.CharField(max_length=100, verbose_name="tutor last name",
                                 help_text="Введите фамилию преподавателя ", null=False, blank=False)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, verbose_name="direction",
                                  help_text="Введите название дисциплины ", null=False, blank=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="id User", help_text="выберите id",
                                null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + ", " + self.direction.__str__()

    class Meta:
        db_table = "Tutor"


class Lab(models.Model):
    name = models.CharField(max_length=20, verbose_name="Title",
                            help_text="Введите название лабы", null=True, blank=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="student",
                                help_text="Введите имя студента", null=False, blank=False)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, verbose_name="tutor",
                              help_text="Введите имя преподавателя", null=False, blank=False)

    mark = IntegerRangeField(min_value=1, max_value=5, verbose_name="mark",
                             help_text="Введите оценку", null=False, blank=False)

    # file = models.FileField()

    def __str__(self):
        return self.student.__str__() + " на " + self.mark.__str__()

    class Meta:
        db_table = "Lab"


# Create your models here.

class Extra_Lessons(models.Model):
    name = models.CharField(max_length=20, verbose_name="Title",
                            help_text="Введите название факутальтива", null=True, blank=False)
    student = models.ManyToManyField(Student, verbose_name="student",
                                     help_text="Ввыберите имя", blank=False)
    tutor = models.ManyToManyField(Tutor, verbose_name="tutor",
                                   help_text="Ввыберите имя", blank=False)

    def __str__(self):
        return self.name.__str__()

    class Meta:
        db_table = "Extra_Lessons"
