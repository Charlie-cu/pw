from django.db import models

class User(models.Model):
    pass
class Rol(models.Model):
    roles={
        'admin':'administrador',
        'estudiante':'estudiante',
        'profesor':'profesor',
    }
    nombre_rol=models.CharField(max_lenght=20,choices=roles)
    
class Subject(models.Model):
    #asignatura
    pass

class Curso(models.Model):
    pass
