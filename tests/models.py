from django.db import models

from br_utils.models import (
    BRCNPJField,
    BRCPFField,
    BRPostalCodeField,
    BRStateField,
    BRBankField
)


class BRPersonProfile(models.Model):
    cpf = BRCPFField()
    cnpj = BRCNPJField()
    postal_code = BRPostalCodeField()
    state = BRStateField()


class BankingDataBR(models.Model):
    bank = BRBankField()