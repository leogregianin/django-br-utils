"""BR-specific Form helpers."""

import re

from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.forms.fields import CharField, Select
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _

from .br_cities import BR_CITY_CHOICES
from .br_states import BR_STATE_CHOICES
from .br_bank import BR_BANK_CHOICES
from .br_country import BR_COUNTRY_CHOICES
from .validators import BRCNPJValidator, BRCPFValidator, BRPostalCodeValidator

process_digits_re = re.compile(
    r'^(\d{7})-?(\d{2})\.?(\d{4})\.?(\d)\.?(\d{2})\.?(\d{4})$'
)


class BRCPFField(CharField):
    """
    A form field that validates a CPF number or a CPF string.

    A CPF number is compounded by XXX.XXX.XXX-VD. The two last digits are check digits.

    More information:
    http://en.wikipedia.org/wiki/Cadastro_de_Pessoas_F%C3%ADsicas

    Use BRCPFValidator to centralize validation logic and share with equivalent model field.
    More details at: https://github.com/django/django-localflavor/issues/334
    """

    default_error_messages = {
        'invalid': _("Invalid CPF number."),
        'max_digits': _("This field requires at most 11 digits or 14 characters."),
    }

    def __init__(self, max_length=14, min_length=11, **kwargs):
        super().__init__(max_length=max_length, min_length=min_length, **kwargs)
        self.validators.append(BRCPFValidator())


class BRCNPJField(CharField):
    """
    A form field that validates input as `Brazilian CNPJ`_.

    Input can either be of the format XX.XXX.XXX/XXXX-XX or be a group of 14
    digits.

    If you want to use the long format only, you can specify:
        brcnpj_field = BRCNPJField(min_length=16)

    If you want to use the short format, you can specify:
        brcnpj_field = BRCNPJField(max_length=14)

    Otherwise both formats will be valid.

    .. _Brazilian CNPJ: http://en.wikipedia.org/wiki/National_identification_number#Brazil

    Use BRCNPJValidator to centralize validation logic and share with equivalent model field.
    More details at: https://github.com/django/django-localflavor/issues/334
    """

    default_error_messages = {
        'invalid': _("Invalid CNPJ number."),
        'max_digits': _("This field requires at least 14 digits"),
    }

    def __init__(self, min_length=14, max_length=18, **kwargs):
        super().__init__(max_length=max_length, min_length=min_length, **kwargs)
        self.validators.append(BRCNPJValidator())


class BRPostalCodeField(CharField):
    """
    A form field that validates input as a Brazilian zip code, with the format 00000-000.

        Use BRPostalCodeValidator to centralize validation logic and share with equivalent model field.
        More details at: https://github.com/django/django-localflavor/issues/334
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.validators.append(BRPostalCodeValidator())


class BRCitySelect(Select):
    """A Select widget that uses a list of Brazilian cities as its choices."""

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=BR_CITY_CHOICES)


class BRCityChoiceField(CharField):
    """A choice field that uses a list of Brazilian cities as its choices."""

    widget = Select
    default_error_messages = {
        'invalid': _('Select a valid brazilian cities.'),
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.widget.choices = BR_CITY_CHOICES

    def clean(self, value):
        value = super().clean(value)
        if value in self.empty_values:
            return value
        valid_values = {force_str(entry[0]) for entry in self.widget.choices}
        if value not in valid_values:
            raise ValidationError(self.error_messages['invalid'], code='invalid')
        return value


class BRStateSelect(Select):
    """A Select widget that uses a list of Brazilian states/territories as its choices."""

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=BR_STATE_CHOICES)


class BRStateChoiceField(CharField):
    """A choice field that uses a list of Brazilian states as its choices."""

    widget = Select
    default_error_messages = {
        'invalid': _('Select a valid brazilian state. That state is not one of the available states.'),
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.widget.choices = BR_STATE_CHOICES

    def clean(self, value):
        value = super().clean(value)
        if value in self.empty_values:
            return value
        valid_values = {force_str(entry[0]) for entry in self.widget.choices}
        if value not in valid_values:
            raise ValidationError(self.error_messages['invalid'], code='invalid')
        return value


class CountrySelect(Select):
    """A Select widget that uses a list of Countries as its choices."""

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=BR_COUNTRY_CHOICES)


class CountryChoiceField(CharField):
    """A choice field that uses a list of Countries as its choices."""

    widget = Select
    default_error_messages = {
        'invalid': _('Select a valid Countries.'),
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.widget.choices = BR_COUNTRY_CHOICES

    def clean(self, value):
        value = super().clean(value)
        if value in self.empty_values:
            return value
        valid_values = {force_str(entry[0]) for entry in self.widget.choices}
        if value not in valid_values:
            raise ValidationError(self.error_messages['invalid'], code='invalid')
        return value


def mod_97_base10(value):
    return 98 - ((value * 100 % 97) % 97)


class BRProcessoField(CharField):
    """
    A form field that validates a Legal Process(Processo) number or a Legal Process string.

    A Processo number is compounded by NNNNNNN-DD.AAAA.J.TR.OOOO. The two DD digits are check digits.
    More information:
    http://www.cnj.jus.br/busca-atos-adm?documento=2748

    """

    default_error_messages = {'invalid': _("Invalid Process number.")}

    def __init__(self, max_length=25, min_length=20, **kwargs):
        super().__init__(max_length=max_length, min_length=min_length, **kwargs)

    def clean(self, value):
        """Value can be either a string in the format NNNNNNN-DD.AAAA.J.TR.OOOO or an 20-digit number."""
        value = super().clean(value)
        if value in self.empty_values:
            return value

        orig_value = value[:]
        if not value.isdigit():
            process_number = process_digits_re.search(value)
            if process_number:
                value = ''.join(process_number.groups())
            else:
                raise ValidationError(self.error_messages['invalid'], code='invalid')

        orig_dv = value[7:9]

        value_without_digits = int(value[0:7] + value[9:])

        if str(mod_97_base10(value_without_digits)).zfill(2) != orig_dv:
            raise ValidationError(self.error_messages['invalid'], code='invalid')

        return orig_value

class BRBankSelect(Select):
    """A Select widget that uses a list of Bank in Brazil."""

    def __init__(self, attrs=None):
        super().__init__(attrs, choices=BR_BANK_CHOICES)


class BRBankChoiceField(CharField):
    """
    A choice field that uses a list of Brazilian Banks as its choices.

    """
    widget = Select
    default_error_messages = {
        'invalid': _('Select a valid brazilian bank. Value not available.'),
        'max_digits': _('This field requires 03 digits'),
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.widget.choices = BR_BANK_CHOICES

    def clean(self, value):
        value = super().clean(value)
        if value in EMPTY_VALUES:
            value = ''
        value = force_str(value)
        if value == '':
            return value
        valid_values = set([force_str(entry[0]) for entry in self.widget.choices])
        if len(value) != 3:
            raise ValidationError(self.error_messages['max_digits'])
        if value not in valid_values:
            raise ValidationError(self.error_messages['invalid'])
        return value