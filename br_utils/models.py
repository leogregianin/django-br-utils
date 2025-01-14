from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _

from . import validators
from .br_states import BR_STATE_CHOICES
from .br_bank import BR_BANK_CHOICES
from .br_cities import BR_CITY_CHOICES
from .br_country import BR_COUNTRY_CHOICES


class BRCPFField(CharField):
    """
    A model field for the brazilian document named of CPF (Cadastro de Pessoa Física)

    """

    description = _("CPF Document")

    default_error_messages = {
        'invalid': _("Invalid CPF number."),
        'max_digits': _("This field requires at most 11 digits or 14 characters."),
    }

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 14
        super().__init__(*args, **kwargs)
        self.validators.append(validators.BRCPFValidator())


class BRCNPJField(CharField):
    """
    A model field for the brazilian document named of CNPJ (Cadastro Nacional de Pessoa Jurídica)

    """

    description = _("CNPJ Document")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18
        super().__init__(*args, **kwargs)
        self.validators.append(validators.BRCNPJValidator())


class BRPostalCodeField(CharField):
    """A model field for the brazilian zip code"""

    description = _("Postal Code")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 9
        super().__init__(*args, **kwargs)
        self.validators.append(validators.BRPostalCodeValidator())


class BRBankField(CharField):
    """A model field for Brazilian Banks (COMPE code)."""
    
    description = _("Brazilian Bank (COMPE code)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = BR_BANK_CHOICES
        kwargs['max_length'] = 3
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


class BRCityField(CharField):
    """A model field for Brazilian Cities (IBGE code)"""
    
    description = _("Brazilian Cities (IBGE code)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = BR_CITY_CHOICES
        kwargs['max_length'] = 7
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


class BRStateField(CharField):
    """A model field for states of Brazil."""

    description = _("State of Brazil (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = BR_STATE_CHOICES
        kwargs['max_length'] = 2
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs



class CountryField(CharField):
    """A model field for Country."""

    description = _("Country")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = BR_COUNTRY_CHOICES
        kwargs['max_length'] = 4
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs
