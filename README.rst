==================
django-br-utils
==================

.. image:: https://img.shields.io/github/actions/workflow/status/leogregianin/django-br-utils/test.yml.svg?branch=main&style=for-the-badge
   :target: https://github.com/leogregianin/django-br-utils/actions?workflow=Test

.. image:: https://img.shields.io/badge/Coverage-100%25-success?style=for-the-badge
  :target: https://github.com/leogregianin/django-br-utils/actions?workflow=Test

.. image:: https://img.shields.io/pypi/v/django-br-utils.svg?style=for-the-badge
    :target: https://pypi.org/project/django-br-utils/


Funcionalidades para informações e dados do Brasil.

Por exemplo, pode incluir no **forms** ou nos **models** campos de códigos
postais (CEP), números de CPF, número de CNPJ e número de processo judicial
para validação automática.

Também pode incluir campos de seleção de estados, cidades com código IBGE, 
países com código IBGE e bancos registrados no Brasil.

Este pacote é inspirado no `django-localflavor <0_>`_
com melhorias e adição de novas informações específicas para o Brasil.

.. _0: https://github.com/django/django-localflavor


**Requisitos**

.. code-block:: shell

   Python >= 3.8
   Django >= 4.2


Veja todos os testes rodando em todas as versões Python e Django:
https://github.com/leogregianin/django-br-utils/actions


**Instalação**

.. code-block:: shell

   pip install django-br-utils


Adicione **br_utils** em INSTALLED_APPS no settings.py:

.. code-block:: python

   INSTALLED_APPS = (
      ...,
      'br_utils',
      ...,
   )


**Como utilizar nos models**

.. code-block:: python

   from django.db import models
   from django_br_utils.models import (
       BRCPFField,
       BRCNPJField,
       BRPostalCodeField,
       BRStateField,
       BRCityField
       CountryField,
       BRBankField,
   )
   
   class Cadastro(models.Model):
      nome = models.CharField(max_length=100)
      email = models.EmailField()
      cpf = BRCPFField()
      cnpj = BRCNPJField()
      cep = BRPostalCodeField()
      uf = BRStateField()
      cidade = BRCityField()
      pais = CountryField()
      banco = BRBankField()



**Como utilizar nos forms**

.. code-block:: python

   from django import forms
   from django_br_utils.forms import (
       BRCPFField,
       BRCNPJField,
       BRPostalCodeField,
       BRStateChoiceField,
       BRCityChoiceField
       CountryChoiceField,
       BRBankChoiceField,
   )

   class CadastroForm(forms.Form):
       nome = forms.CharField(max_length=100)
       email = forms.EmailField()
       cpf = BRCPFField()
       cnpj = BRCNPJField()
       cep = BRPostalCodeField()
       uf = BRStateChoiceField()
       cidade = BRCityChoiceField()
       pais = CountryChoiceField()
       banco = BRBankChoiceField()


**Funções Utilitárias**

O módulo também oferece funções utilitárias que podem ser importadas e utilizadas no seu projeto:

.. code-block:: python

   from django_br_utils.utils import get_states_of_brazil, get_countries_of_brazil, get_cities_of_brazil, get_banks_of_brazil

**get_states_of_brazil**

Esta função retorna informações sobre os estados brasileiros.

Parâmetros:
  - ``federative_unit`` (opcional): A sigla da Unidade Federativa. Quando não informado, retorna todos os estados.
  - ``capital_letter`` (opcional, padrão=False): Flag para retornar os nomes dos estados em letras maiúsculas.

Retorno:
  - Se ``federative_unit`` é informado e válido, retorna uma string com o nome do estado.
  - Se ``federative_unit`` é None, retorna um dicionário com todas as siglas e nomes dos estados.
  - Se ``capital_letter`` é True, retorna todos os valores em letras maiúsculas.

Exemplos de uso:

.. code-block:: python

   # Obter todos os estados
   estados = get_states_of_brazil()
   # {'AC': 'acre', 'AL': 'alagoas', 'AP': 'amapá', ...}
   
   # Obter o nome de um estado específico
   nome_estado = get_states_of_brazil('SP')
   # 'são paulo'
   
   # Obter todos os estados em letras maiúsculas
   estados_maiusculos = get_states_of_brazil(capital_letter=True)
   # {'AC': 'ACRE', 'AL': 'ALAGOAS', 'AP': 'AMAPÁ', ...}

**get_countries_of_brazil**

Esta função retorna informações sobre os países no padrão IBGE.

Parâmetros:
  - ``country_code`` (opcional): O código do país no padrão IBGE. Quando não informado, retorna todos os países.
  - ``capital_letter`` (opcional, padrão=False): Flag para retornar os nomes dos países em letras maiúsculas.

Retorno:
  - Se ``country_code`` é informado e válido, retorna uma string com o nome do país.
  - Se ``country_code`` é None, retorna um dicionário com todos os códigos e nomes dos países.
  - Se ``capital_letter`` é True, retorna os nomes em maiúsculas, caso contrário em minúsculas.

Exemplos de uso:

.. code-block:: python

   # Obter todos os países
   paises = get_countries_of_brazil()
   # {'0132': 'afeganistao', '0175': 'albania, republica da', ...}
   
   # Obter o nome de um país específico por código
   nome_pais = get_countries_of_brazil('1058')
   # 'brasil'
   
   # Obter todos os países em letras maiúsculas
   paises_maiusculos = get_countries_of_brazil(capital_letter=True)
   # {'0132': 'AFEGANISTAO', '0175': 'ALBANIA, REPUBLICA DA', ...}

**get_cities_of_brazil**

Esta função retorna informações sobre as cidades brasileiras no padrão IBGE.

Parâmetros:
  - ``city_code`` (opcional): O código da cidade no padrão IBGE. Quando não informado, retorna todas as cidades.
  - ``capital_letter`` (opcional, padrão=False): Flag para retornar os nomes das cidades em letras maiúsculas.

Retorno:
  - Se ``city_code`` é informado e válido, retorna uma string com o nome da cidade.
  - Se ``city_code`` é None, retorna um dicionário com todos os códigos e nomes das cidades.
  - Se ``capital_letter`` é True, retorna os nomes em maiúsculas, caso contrário em minúsculas.

Exemplos de uso:

.. code-block:: python

   # Obter todas as cidades
   cidades = get_cities_of_brazil()
   # {'1100015': 'alta floresta d oeste-ro', '1100023': 'ariquemes-ro', ...}
   
   # Obter o nome de uma cidade específica por código
   nome_cidade = get_cities_of_brazil('3550308')
   # 'são paulo-sp'
   
   # Obter todas as cidades em letras maiúsculas
   cidades_maiusculas = get_cities_of_brazil(capital_letter=True)
   # {'1100015': 'ALTA FLORESTA D OESTE-RO', '1100023': 'ARIQUEMES-RO', ...}


**get_banks_of_brazil**

Esta função retorna informações sobre os bancos registrados no Brasil.

Parâmetros:
  - ``bank_code`` (opcional): O código do banco. Quando não informado, retorna todos os bancos.
  - ``capital_letter`` (opcional, padrão=False): Flag para retornar os nomes dos bancos em letras maiúsculas.

Retorno:
  - Se ``bank_code`` é informado e válido, retorna uma string com o nome do banco.
  - Se ``bank_code`` é None, retorna um dicionário com todos os códigos e nomes dos bancos.
  - Se ``capital_letter`` é True, retorna os nomes em maiúsculas, caso contrário em minúsculas.

Exemplos de uso:

.. code-block:: python

   # Obter todos os bancos
   bancos = get_banks_of_brazil()
   # {'001': 'bco do brasil s.a.', '003': 'bco da amazonia s.a.', ...}
   
   # Obter o nome de um banco específico por código
   nome_banco = get_banks_of_brazil('341')
   # 'itaú unibanco s.a.'
   
   # Obter todos os bancos em letras maiúsculas
   bancos_maiusculos = get_banks_of_brazil(capital_letter=True)
   # {'001': 'BCO DO BRASIL S.A.', '003': 'BCO DA AMAZONIA S.A.', ...}


**Contribuição**

Contribuições são sempre bem vindas.

Sinta-se a vontade para abrir uma `Issue <1_>`_ para correções, dúvidas ou sugestões.

.. _1: https://github.com/leogregianin/django-br-utils/issues
