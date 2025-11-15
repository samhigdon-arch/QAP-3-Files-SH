# Desc: Honest Harry owns a used car lot and would like a program to keep track of his sales. Follow good 
# Author: Sam Higdon
# Date(s): November 12,2025 - 

# Libarbries

import datetime
import FormatValues as FV

# Functions

from datetime import datetime

# FUNCTIONS
def GetValidPlate():
    while True:
        plate = input("Enter plate number (ABC123): ").upper().strip()

        if len(plate) == 6 and plate[:3].isalpha() and plate[3:].isdigit():
            return plate
        else:
            print(" Invalid plate. Use format like ABC123 (3 letters + 3 numbers).")


def GetValidPhone():
    "Prompt until a valid 10 digit Phone Number is entered."

    while True:
        Phone = input("Enter Phone Number (# ### ### ####): ").strip()
        if Phone == "":
            print("  ** DATA ENTRY ERROR - A phone number must be entered.")
            continue

        Digits = FV.CleanPhone(Phone)

        if isinstance(Digits, (list, tuple)):
            Digits = "".join(Digits)
        Digits = str(Digits)

        if len(Digits) == 11 and Digits.startswith("1"):
            Digits = Digits[1:]

        if len(Digits) == 10 and Digits.isdigit():
            return Digits

        print("  ** DATA ENTRY ERROR - Phone number must contain 10 digits.")
        continue


def GetSalesName():
    "Prompt the user to put a seller name"

    while True:
        SalesName = input("Please Enter the name of the seller: ").strip().upper()
        if SalesName == "":
            print("** DATA ENTRY ERROR - A name for the sales person must be entered")
            continue
        return SalesName


# CONSTANTS
LICENSE_FEE_LOW = 75.00
MAX_SELL_PRICE = 50000.00
LICENSE_FEE_HIGH = 165.00
LUXURY_TAX_RATE = 0.016
HST_RATE = 0.15
TRANSFER_FEE_RATE = 0.1
FINANCE_FEE_PER_YEAR = 39.99

# MAIN LOOP
while True:

    # Inputs
    FirstName = input("Please enter the First name: ").strip().title()
    if FirstName.upper() == "END":
        break

    LastName = input("Please enter the last name:  ").strip().title()
    PhoneNum = GetValidPhone()
    Plate = GetValidPlate()
    CarMake = input("Please enter the car make(i.e Toyota):    ").strip().title()
    CarModel = input("Please enter the car model(i.e Corolla): ").strip().title()
    CarYear = input("Please enter the car year:                ").strip()
    SalesName = GetSalesName()

    # Selling Price
    while True:
        try:
            SellPrice = int(input("Please enter the selling price:   ").strip())
        except ValueError:
            print(" ** DATA ENTRY ERROR - Enter a whole number for selling price.")
            continue
        if SellPrice > MAX_SELL_PRICE:
            print(" ** DATA ENTRY ERROR - The Selling price exceeds the Maximum selling price.")
            continue
        break

    # Trade-in Value
    while True:
        try:
            TradeIn = int(input("Please enter the trade in value:  ").strip())
        except ValueError:
            print(" ** DATA ENTRY ERROR - Enter a whole number for trade in value.")
            continue
        if TradeIn > SellPrice:
            print(" ** DATA ENTRY ERROR - The trade in value cannot exceed the selling price")
            continue
        break

    # CALCULATIONS
    PriceAfterTrade = SellPrice - TradeIn

    if SellPrice <= 15000:
        LicenseFee = LICENSE_FEE_HIGH
    else:
        LicenseFee = LICENSE_FEE_LOW

    if SellPrice > 2000:
        TransferFee = SellPrice * LUXURY_TAX_RATE
    else:
        TransferFee = SellPrice * TRANSFER_FEE_RATE

    SubTotal = PriceAfterTrade + LicenseFee + TransferFee
    HSTAmt = SubTotal * HST_RATE
    TotalSales = SubTotal + HSTAmt

    # Format Values
    FormattedPhone = FV.format_phone(PhoneNum)

    # Proper date handling:
    Date = datetime.now().strftime("%Y-%m-%d")

    ReceiptID = FV.create_receipt_id(FirstName, LastName, Plate, PhoneNum)

    # DISPLAY OUTPUT
    print()
    print(f"Honest Harry Car Sales                             Invoice Date:    {Date}")
    print(f"Used Car Sale and Receipt                          Receipt No:      {ReceiptID}")
    print()

    print(f"Sold to:                                           Sale price:       {FV.FDollar2(SellPrice):<10s}")
    print(f"                                                   Trade Allowance:  {FV.FDollar2(TradeIn):<10s}")
    print("                                                  ----------------------------------------------------")
    print()

    print(f"{FirstName[0]}. {LastName}                      Price After Trade: {FV.FDollar2(PriceAfterTrade):<10s}")

    PhoneNumDisplay = "(" + PhoneNum[0:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:10]
    print(f"{FormattedPhone}                               Transfer Fee:      {FV.FDollar2(TransferFee):<10s}")
    print("                                               --------------------------------------------------------")

    print(f"Car Details                                        Subtotal:           {FV.FDollar2(SubTotal):<10s}")
    print(f"{CarYear:<6}{CarMake:<15}{CarModel:<15}{Plate:<8}  HST: {FV.FDollar2(HSTAmt):>10}")
    print("                                                  -------------------------------------------------------")
    print(f"                                               Total Sales Price:  {FV.FDollar2(TotalSales)}")
    print("----------------------------------------------------------------------------------------------------------------")

    print("# Years   # Payments   Financing Fee   Total Price    Monthly Payment")
    print("----------------------------------------------------------------------")

    for Years in range(1, 5):
        Payments = Years * 12
        FinancingFee = FINANCE_FEE_PER_YEAR * Years
        TotalPrice = TotalSales + FinancingFee
        MonthlyFee = TotalPrice / Payments

        print(f"{Years:<9} {Payments:<13} {FinancingFee:<14.2f} {TotalPrice:<14.2f} {MonthlyFee:<14.2f}")

    print("----------------------------------------------------------------------")
    print(f"Best used cars at the best prices!")
    print()
