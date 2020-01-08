from django.db import models

SEXO = (('M','Masculino'),
        ('F','Femenino'))

class Direccion(models.Model):
    codigo = models.IntegerField()
    callePrincipal=models.CharField(max_length=200)
    calleSecundaria=models.CharField(max_length=200)
    numeroCasa=models.CharField(max_length=10)

class Persona(models.Model):
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fechaNacimiento=models.DateField()
    edad=models.IntegerField(default=0)
    sexo=models.CharField(max_length=1,choices=SEXO)
    direccion=models.ForeignKey(Direccion,null=True,on_delete=models.CASCADE)
