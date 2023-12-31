# Generated by Django 4.2.7 on 2023-11-13 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Associado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('cidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=20)),
                ('data_nascimento', models.DateField()),
                ('tipo_associacao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Convidado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=15)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='EspacoLocavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tamanho', models.IntegerField()),
                ('capacidade_pessoas', models.IntegerField()),
                ('data_construcao_aquisicao', models.DateField()),
                ('locavel', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_razao_social', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('cep', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('contato', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dependente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=20)),
                ('data_nascimento', models.DateField()),
                ('tipo_vinculo', models.CharField(max_length=50)),
                ('socio_titular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependentes', to='clube.associado')),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_locacao', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_inicio', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('data_fim', models.DateField()),
                ('hora_fim', models.TimeField()),
                ('convidados', models.ManyToManyField(blank=True, to='clube.convidado')),
                ('espaco_locavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clube.espacolocavel')),
                ('responsavel_locacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clube.associado')),
            ],
        ),
    ]
