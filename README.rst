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

Requisitos
===================

.. code-block:: shell

   Python >= 3.8
   Django >= 4.2


Veja todos os testes rodando em todas as versões Python e Django:
https://github.com/leogregianin/django-br-utils/actions



Instalação
===================

.. code-block:: shell

   pip install django-br-utils


Adicione **br_utils** em INSTALLED_APPS no settings.py:

.. code-block:: python

   INSTALLED_APPS = (
      ...,
      'br_utils',
      ...,
   )


Como utilizar nos models
===================

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



Como utilizar nos forms
===================

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


Contribuição
===================

Contribuições são sempre bem vindas.

Sinta-se a vontade para abrir uma `Issue <1_>`_ para correções, dúvidas ou sugestões.

.. _1: https://github.com/leogregianin/django-br-utils/issues
