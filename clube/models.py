from django.db import models

# Create your models here.

associacao = [
        ('fundador', 'Sócio Fundador'),
        ('proprietario', 'Sócio Proprietário'),
        ('cotista', 'Sócio Cotista'),
        ('voluntario', 'Sócio Voluntário')
    ]

uf = [
    ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
]

class Associado(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, choices=uf)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    email = models.EmailField()
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    tipo_associacao = models.CharField(max_length=50, choices=associacao)
    
    def __str__(self):
        return self.nome

class Dependente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    tipo_vinculo = models.CharField(max_length=50)
    socio_titular = models.ForeignKey(Associado, on_delete=models.CASCADE, related_name='dependentes')

class EspacoLocavel(models.Model):
    nome = models.CharField(max_length=100)
    tamanho = models.IntegerField()
    capacidade_pessoas = models.IntegerField()
    data_construcao_aquisicao = models.DateField()
    locavel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome_razao_social = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, choices=uf)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    email = models.EmailField()
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    contato = models.CharField(max_length=100)

class Convidado(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=20)
    celular = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

class Agenda(models.Model):
    espaco_locavel = models.ForeignKey(EspacoLocavel, on_delete=models.CASCADE)
    valor_locacao = models.DecimalField(max_digits=10, decimal_places=2)
    data_inicio = models.DateField()
    hora_inicio = models.TimeField()
    data_fim = models.DateField()
    hora_fim = models.TimeField()
    responsavel_locacao = models.ForeignKey(Associado, on_delete=models.CASCADE)
    convidados = models.ManyToManyField(Convidado, blank=True)
