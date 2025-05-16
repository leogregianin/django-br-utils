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

   from django_br_utils.utils import get_states_of_brazil

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


**Contribuição**

Contribuições são sempre bem vindas.

Sinta-se a vontade para abrir uma `Issue <1_>`_ para correções, dúvidas ou sugestões.

.. _1: https://github.com/leogregianin/django-br-utils/issues
