from tkinter import CASCADE
from django.db import models

class Desarrolladora(models.Model):
    name = models.TextField()
    description = models.TextField()
    image = models.TextField()
    web_page = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Estado(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Segmentos(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Acabado(models.Model):
    name = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Equipamiento(models.Model):
    name = models.TextField()
    type = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tipo_Inmueble(models.Model):
    name = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Municipio(models.Model):
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE) 
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Colonia(models.Model):
    id_municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE) 
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name  

class Zona(models.Model):
    id_municipio = models.ForeignKey(Municipio, on_delete = models.CASCADE)
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

class Proyecto(models.Model):
    id_desarrolladora = models.ForeignKey(Desarrolladora, on_delete=models.CASCADE)
    id_colonia = models.ForeignKey(Colonia, on_delete=models.CASCADE)
    id_zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    name = models.TextField()
    initial_date = models.DateTimeField()
    latitud = models.TextField()
    longitude = models.TextField()
    url_image = models.TextField()
    url_logo = models.TextField()
    phone = models.TextField()   
    address = models.TextField()
    csv = models.TextField()
    pdf_brochure = models.TextField()
    webpage_url = models.TextField()
    social_media = models.TextField()
    description = models.TextField()
    category = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Amenidades(models.Model):
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    ##id_amenidad = models.ForeignKey(????, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Prototipo(models.Model):
    id_proyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE)
    ##id_categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    name = models.TextField()
    price = models.IntegerField()
    total_units = models.IntegerField() 
    sold_units = models.IntegerField()
    m2_terrain = models.IntegerField()
    m2_constructed = models.IntegerField()
    m2_habitable = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

class Transaccion(models.Model):
    id_prototipo = models.ForeignKey(Prototipo, on_delete = models.CASCADE) 
    date = models.DateTimeField()
    type = models.TextField()
    monto = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type 

