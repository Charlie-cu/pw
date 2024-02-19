from django.db import models
from django.contrib.auth.models import User

class Admin(User):
    roles={
        'admin':'administrador',
        'estudiante':'estudiante',
        'profesor':'profesor',
    }
    rol=models.CharField(max_length=20,choices=roles)
    
    
class Docente(User):
    roles={
        'admin':'administrador',
        'estudiante':'estudiante',
        'profesor':'profesor',
    }
    rol=models.CharField(max_length=20,choices=roles)
    dni = models.IntegerField()
    
    
class Estudiante(User):
    roles={
        'admin':'administrador',
        'estudiante':'estudiante',
        'profesor':'profesor',
    }
    rol=models.CharField(max_length=20,choices=roles)
    calificacion = models.IntegerField()
    
    
class Subject(models.Model):
    #asignatura
    estudiante=models.ManyToManyField(Estudiante)
    docente=models.OneToOneField(Docente,on_delete=models.CASCADE)
    sesion={"mañana":"mañana","tarde":"tarde"}
    nombre_completo = models.CharField(max_length=19)
    sesion=models.CharField(max_length=19,choices=sesion)
    
class Examen(models.Model):
    nom_asig=models.CharField(max_length=20)
    fecha=models.DateTimeField(auto_now_add=True)
    lugar=models.CharField(max_length=20)