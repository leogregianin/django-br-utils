from .br_states import BR_STATE_CHOICES
from .br_country import BR_COUNTRY_CHOICES
from .br_cities import BR_CITY_CHOICES
from .br_bank import BR_BANK_CHOICES


def get_states_of_brazil(federative_unit=None, capital_letter=False):
    """
    Return a state of Brazil or available options
    Parametes:
    federative_unit (Any, optional): The Federative Unit. If not provided, defaults to None.
    capital_letter (bool, optional): A boolean flag to return the state with capital letter. Defaults to False
    returns:
    Union[str, dict]:
        - If federative_unit not is None and his value is valid, returns a string
        - If federative_unit is None, returns a dictionary
        - If capital_letter is True, returns all values with capital letters
    """

    state_choices_available = {
        acronym: state.upper() if capital_letter else state for acronym, state in BR_STATE_CHOICES
    }

    if federative_unit is None:
        return state_choices_available

    federative_unit = federative_unit.upper() if isinstance(federative_unit, str) else ""

    if federative_unit in state_choices_available:
        return state_choices_available[federative_unit]

    return state_choices_available


def get_countries_of_brazil(country_code=None, capital_letter=False):
    """
    Return a country or available options
    Parameters:
    country_code (Any, optional): The country code. If not provided, defaults to None.
    capital_letter (bool, optional): A boolean flag to return the country name with capital letter. Defaults to False
    returns:
    Union[str, dict]:
        - If country_code not is None and his value is valid, returns a string
        - If country_code is None, returns a dictionary
        - If capital_letter is True, returns all values with capital letters
    """

    country_choices_available = {
        code: name if capital_letter else name.lower() for code, name in BR_COUNTRY_CHOICES
    }

    if country_code is None:
        return country_choices_available

    country_code = str(country_code) if isinstance(country_code, (str, int)) else ""

    if country_code in country_choices_available:
        return country_choices_available[country_code]

    return country_choices_available


def get_cities_of_brazil(city_code=None, capital_letter=False):
    """
    Return a city of Brazil or available options
    Parameters:
    city_code (Any, optional): The city code in IBGE format. If not provided, defaults to None.
    capital_letter (bool, optional): A boolean flag to return the city name with capital letter. Defaults to False
    returns:
    Union[str, dict]:
        - If city_code not is None and his value is valid, returns a string
        - If city_code is None, returns a dictionary
        - If capital_letter is True, returns all values with capital letters
    """

    city_choices_available = {
        code: name if capital_letter else name.lower() for code, name in BR_CITY_CHOICES
    }

    if city_code is None:
        return city_choices_available

    city_code = str(city_code) if isinstance(city_code, (str, int)) else ""

    if city_code in city_choices_available:
        return city_choices_available[city_code]

    return city_choices_available


def get_banks_of_brazil(bank_code=None, capital_letter=False):
    """
    Return a bank of Brazil or available options
    Parameters:
    bank_code (Any, optional): The bank code. If not provided, defaults to None.
    capital_letter (bool, optional): A boolean flag to return the bank name with capital letter. Defaults to False
    returns:
    Union[str, dict]:
        - If bank_code not is None and his value is valid, returns a string
        - If bank_code is None, returns a dictionary
        - If capital_letter is True, returns all values with capital letters
    """

    bank_choices_available = {
        code: name if capital_letter else name.lower() for code, name in BR_BANK_CHOICES
    }

    if bank_code is None:
        return bank_choices_available

    bank_code = str(bank_code) if isinstance(bank_code, (str, int)) else ""

    if bank_code in bank_choices_available:
        return bank_choices_available[bank_code]

    return bank_choices_available
