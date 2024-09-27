from django.db import models

class Produto(models.Model):
    status= models.CharField(max_length=20)
    respEntrada= models.DateTimeField
    numeroEntrada= models.CharField(max_length=100)
    dataEntrada= models.Model
    ptn= models.CharField(max_length=100)
    serie= models.CharField(max_length=100)
    sku= models.CharField(max_length=100)
    modeloRevenda= models.CharField(max_length=100)
    respTriagem= models.CharField(max_length=100)
    modeloSufixo= models.CharField(max_length=100)
    tipoDefeito= models.CharField(max_length=100)
    respPecas= models.CharField(max_length=100)
    pecas= models.CharField(max_length=100)
    respConserto= models.CharField(max_length=100)
    tipoReparo= models.CharField(max_length=100)
    respEmbalagem= models.CharField(max_length=100)
    endereco= models.CharField(max_length=100)
    respSaida= models.CharField(max_length=100)
    dataSaida= models.CharField(max_length=100)
    registroSaida= models.CharField(max_length=100)
    tipoSaida= models.CharField(max_length=100)
