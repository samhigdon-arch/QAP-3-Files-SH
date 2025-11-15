  # Library of functions for formatting numbers and dates.

import datetime

# Constants
CURRENCY_FORMAT = "${:,.2f}"

def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to #,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to #,###.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to ####.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to ####.#.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to ####.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr

def format_phone(Phone):
    """Format a 10-digit phone number into (XXX) XXX-XXXX format."""
    if len(Phone) == 11 and Phone.isdigit():
        return f"({ Phone[:3]}) {Phone[3:6]}-{Phone[6:]}"
    else:
        return Phone  # Return unchanged if invalid


def FormatCurrency(amount):
    """Format a number as Canadian currency (e.g., $9,999.99)."""
    try:
        return CURRENCY_FORMAT.format(float(amount))
    except (ValueError, TypeError):
        return "$0.00"


def format_date():
    """Return the current system date in the format: Mon dd, yyyy."""
    return datetime.date.today().strftime("%a %d, %Y")


def create_receipt_id(fname, lname, plate, phone):
    """Generate a unique receipt ID in the form XX-XXX-XXXX."""
    try:
        initials = (fname[0] + lname[0]).upper()
        last3_plate = plate[-3:].upper()
        last4_phone = phone[-4:]
        return f"{initials}-{last3_plate}-{last4_phone}"
    except Exception:
        return "XX-XXX-XXXX"


def CleanPhone(Phone):
    """Return only digits from the entered phone number."""
    return "".join(ch for ch in str(Phone) if ch.isdigit())