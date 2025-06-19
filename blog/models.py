from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo


