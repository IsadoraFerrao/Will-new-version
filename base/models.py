from django.db import models
from django.conf import settings



class Responsavel(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    telefone = models.CharField(max_length=14, verbose_name="Telefone")
    email = models.EmailField(verbose_name="Email")
    logradouro = models.CharField(max_length=50, verbose_name="Logradouro")
    cidade = models.CharField(max_length=50, verbose_name="Cidade")
    bairro = models.CharField(max_length=50, verbose_name="Bairro")
    estado = models.CharField(max_length=20, verbose_name="Estado")
    cep = models.CharField(max_length=10, verbose_name="CEP")
    numero = models.CharField(max_length=5, verbose_name="Numero")
    complemento = models.CharField(max_length=30, verbose_name="Complemento")


class CadastroPet(models.Model):
    tipos_list = (
        ("gato", "Gato"),
        ("cachorro", "Cachorro")
    )
    tipo = models.CharField(max_length=30, verbose_name="Tipo", choices=tipos_list)
    nome = models.CharField(max_length=30, verbose_name="Nome")
    idade = models.IntegerField(verbose_name="Idade")
    raca = models.CharField(max_length=30, verbose_name="Raça")
    peso = models.IntegerField(verbose_name="Peso")
    id_responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30, verbose_name="Tipo", choices=tipos_list)


class ReservaServico(models.Model):
    
    dia_reserva = models.DateField(verbose_name="Dia da Reserva")
    id_pet = models.ForeignKey(CadastroPet, on_delete=models.CASCADE)
    id_reponsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    



