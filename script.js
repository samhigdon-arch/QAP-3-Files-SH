// Desc:
// Author:
// Dates:


var $ = function (id) {
  return document.getElementById(id);
};


// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});


// Define program constants.

const BORDER_PER = 0.4;
const BOREDER_RATE = 0.28;
const MOW_PER = 0.95;
const MOW_RATE = 0.4;
const FERT_RATE = 0.3;
const HST_RATE = 0.15;
const ENV_RATE = 0.14;

// Start main program here.

// inputs

let FirstName = prompt("Enter First Name: ");
let LastName = prompt("Enter Last Name");
let StAdd = prompt("Enter the street Adress: ");
let City = prompt("Enter the City: ");
let PhoneNum = prompt("Please enter the phone number(9 999 999 9999): ");
let TotSqFt = prompt("Please enter the total square foot(#####): ");

// Calculations

let BorderSize = TotSqFt * BORDER_PER;
let BorderCost = BorderSize * BOREDER_RATE;

let MowSize = TotSqFt * MOW_PER;
let MowCost = MowSize * MOW_RATE;

let FertCost = TotSqFt * FERT_RATE;

let TotalCharges = BorderCost + MowCost + FertCost;
let HSTAmt = TotalCharges * HST_RATE;
let EnvTax = TotalCharges * ENV_RATE;
let InvoiceTotal = TotalCharges + HSTAmt + EnvTax;


// ===== Display Section =====
document.writeln("<table class='resultstable'>");

document.writeln("<tr><td colspan='2' class='header' class ='Orangerow'> Mo's Lawncare Services - Customer Invoice</td></tr>");

document.writeln("<tr><td colspan='2'><br />Customer details:<br/>");
document.writeln(FirstName+ " " + LastName + "<br />");
document.writeln(StAdd + "<br />");
document.writeln(City + " " + PhoneNum +  "<br /><br />");
document.writeln("Property size (in sq ft):"+ TotSqFt + "</td></tr>");

document.writeln("<tr><td>Border cost:</td><td class='righttext'>" + cur2Format.format(BorderCost) + "</td></tr>");
document.writeln("<tr><td>Mowing cost:</td><td class='righttext'>" + cur2Format.format(MowCost) + "</td></tr>");
document.writeln("<tr><td>Fertiziler cost:</td><td class='righttext'>" + cur2Format.format(FertCost) + "</td></tr>");

document.writeln("<tr><td colspan='2'> &nbsp;</td></tr>");
document.writeln("<tr><td>Total charges:</td><td class='righttext'>" + cur2Format.format(TotalCharges) + "</td></tr>");

document.writeln("<tr><td colspan='2'>&nbsp;</td></tr>");
document.writeln("<tr><td>Sales Tax (HST):</td><td class='righttext'>" + cur2Format.format(HSTAmt)+ "</td></tr>");
document.writeln("<tr><td>Enviromental tax:</td><td class='righttext'>"  + cur2Format.format(EnvTax) + "</td></tr>");

document.writeln("<tr><td colspan='2'>&nbsp;</td></tr>");
document.writeln("<tr><td> Invoice total:</td><td class ='righttext'>" + cur2Format.format(InvoiceTotal) + "</td></tr>");

document.writeln("<tr><td colspan= '2' class = 'footer' class= 'Orangerow'>Turning Lawns into landscapes</td></tr>");
document.writeln("</table>");
