#
# Python-Programm um die Pandas-Bibliothek zu testen
#
# --------------------------------------------------------------------------------

# import section -----------------------------------------------------------------

import os
from os import system
import pandas as pd
import re

# -------------------------------------------------------------------------------

def head():
    print("--------------------------------------------------------------------------------")

# Programmsteuerung -------------------------------------------------------------

df = pd.DataFrame()

show_all = False
trennlinie_sel = 1
dateiname_sel = 2
notebook = False
visual_studio = False

if trennlinie_sel == 0:
    trennlinie = ""
elif trennlinie_sel == 1:
    trennlinie = "--------------------------------------------------------------------------------\n"
    
if dateiname_sel == 1:    
    dateiname_in = "Normalisierungsdaten_in.csv"
    dateiname_out = "Normalisierungsdaten_out.csv"
elif dateiname_sel == 2:
    dateiname_in = "Amazon Sales Report_messy.csv"
    dateiname_out = "Amazon Sales Report_messy_out.csv"
elif dateiname_sel == 3:
    dateiname_in = "Amazon Sales Report_messy_10000.csv"
    dateiname_out = "Amazon Sales Report_messy_out_10000.csv"

if notebook:
    dateiname_in = "dev/dms/" + dateiname_in
    dateiname_out = "dev/dms/" + dateiname_out

# --------------------------------------------------------------------------------

EMPH = '\033[32m'
NORM = '\033[0m'

# --------------------------------------------------------------------------------

def remove_all(muster):
    pass
    
    return()

# --------------------------------------------------------------------------------

def keep_only(muster):
    pass
    
    return()

# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------

def bereinigen_nur_ziffern(s):

    return re.sub(r'[^0-9]', '', s)

# --------------------------------------------------------------------------------

def bereinigen_nur_ziffern_und_bindestrich(s):

    return re.sub(r'[^0-9-]', '', s)

# --------------------------------------------------------------------------------

def ist_gueltige_order_ID(s):

    muster = r'^\d{3}-\d{7}-\d{7}$'

    return bool(re.match(muster, s))

# --------------------------------------------------------------------------------

def return_gueltige_order_ID(s):

    muster = r'^\d{3}-\d{7}-\d{7}$'

    if bool(re.match(muster, s)):
        return(s)
    else:
        return(None)

# --------------------------------------------------------------------------------

def return_gueltiges_datum(s):

    # YYYY-MM-DD:
    if bool(re.match(r'^\d{4}-\d{2}-\d{2}$', s)):
        return(s)
    # MM/DD/YYYY:
    elif bool(re.match(r'^\d{2}/\d{2}/\d{4}$', s)):
        return(s)
    # DD-MM-YYYY:
    elif bool(re.match(r'^\d{2}-\d{2}-\d{4}$', s)):
        return(s)
    else:
        return(None)

# --------------------------------------------------------------------------------

def return_gueltigen_status(s):

    gueltige_stati = {"CANCELLED": "Cancelled",
                      "SHIPPEDDELIVEREDTOBUYER": "Shipped - Delivered to Buyer",
                      "SHIPPED": "Shipped",
                      "SHIPPEDRETURNEDTOSELLER": "Shipped - Returned to Seller",
                      "SHIPPEDREJECTEDBYBUYER": "Shipped - Rejected by Buyer",
                      "SHIPPEDLOSTINTRANSIT": "Shipped - Lost in Transit",
                      "SHIPPEDOUTFORDELIVERY": "Shipped - Out for Delivery",
                      "SHIPPEDRETURNINGTOSELLER": "Shipped - Returning to Seller",
                      "SHIPPEDPICKEDUP": "Shipped - Picked Up",
                      "PENDING": "Pending",
                      "PENDINGWAITINGFORPICKUP": "Pending - Waiting for Pick Up",
                      "SHIPPEDDAMAGED": "Shipped - Damaged",
                      "SHIPPING": "Shipping"}

    if s in gueltige_stati:
        return(gueltige_stati[s])
    else:
        return("#unknown")

# --------------------------------------------------------------------------------

def compare_strings(s1, s2):

    # Kriterium 1: Beide Strings sind gleich

    if s1 == s2:
        return True
    
    # Kriterium 2: Die Strings unterscheiden sich in genau einem Zeichen

    if len(s1) == len(s2):
        differences = sum(1 for a, b in zip(s1, s2) if a != b)
        if differences == 1:
            return True
    
    # Kriterium 3: Ein String hat ein zusätzliches Zeichen

    if abs(len(s1) - len(s2)) == 1:

        # Bestimme die längere und die kürzere Version

        longer, shorter = (s1, s2) if len(s1) > len(s2) else (s2, s1)

        # Überprüfe, ob die Strings gleich sind, außer an einer Stelle

        for i in range(len(shorter)):
            if longer[i] != shorter[i]:

                # Überprüfe, ob der Rest der längeren String gleich ist

                return longer[i+1:] == shorter[i:]

        return True  # Falls das letzte Zeichen unterschiedlich ist
    
    return False  # Falls keine der Bedingungen zutrifft

# Beispielaufrufe
# print(compare_strings("test", "test"))        # True
# print(compare_strings("test", "tost"))        # True
# print(compare_strings("test", "teest"))       # True
# print(compare_strings("test", "teestt"))      # False
# print(compare_strings("test", "tostt"))       # False

# --------------------------------------------------------------------------------

def programmanfang():

    system("clear")
    print("Python-Programm um die messed Daten zu bereinigen")

    return()
    
# --------------------------------------------------------------------------------

def daten_laden():
    global df

    head()
    print(f"Tabelle '{dateiname_in}' in ein Pandas dataframe (df) einlesen mit {EMPH}pd.read_csv{NORM}:")

    if dateiname_sel == 1:
        df = pd.read_csv(dateiname_in, sep=";", skiprows=1) 
    elif dateiname_sel == 2:    
        df = pd.read_csv(dateiname_in, sep=",", skiprows=0) 
    elif dateiname_sel == 3:    
        df = pd.read_csv(dateiname_in, sep=",", skiprows=0) 

    print("")
    print("Erledigt.")

    df = df.astype(str)

    if show_all:
        print("")    
        input("--> Return")
        
    return()
    
# --------------------------------------------------------------------------------

def daten_speichern():
    global df

    head()
    print(f"Dataframe in die Datei '{dateiname_out}' schreiben mit {EMPH}df.to_csv('Dateiname'){NORM}:")

    df.to_csv(dateiname_out, sep=";", decimal=",")

    print("")
    print("Erledigt.")

    if show_all:
        print("")    
        input("--> Return")

    return()
    
# --------------------------------------------------------------------------------
    
def programmende():

    head()
    print("Programmende (Bereinigung der messed-Daten)")

    return()
    
# --------------------------------------------------------------------------------

def p00_dataset_analysieren():
    global df

    head()
    print(f"Infos zum Dataframe anzeigen mit {EMPH}df.info(){NORM}:")
    print("")    
    print(df.info())

    if show_all:
        print("")    
        input("--> Return")
    
    head()
    print(f"Beispieldatensätze anzeigen mit {EMPH}df.sample(){NORM}:")
    print("")
    print(df.sample(10))

    if show_all:
        print("")    
        input("--> Return")

    return()

# --------------------------------------------------------------------------------

def p00_alle_felder_einzeln_analysieren():
    global df
    
    head()
    print("Informationen zu allen Feldern anzeigen:")
    
    # for all fields:
    #     show field#, field_name
    #     show content, count() sorted by content ascending
    #     show content, count() sorted by count() descending
    #     input("--> Return")
    
    for feldname in df.columns:
        
        os.system("clear")
        print(f"Feld: '{feldname}':")
        
        print("")
        print(df[feldname].value_counts().sort_index())
        
        print("")
        print(df[feldname].value_counts())
        
        print("")
        input("--> Return")

    return()

# --------------------------------------------------------------------------------



# --------------------------------------------------------------------------------

def p01_funktionen_auf_allen_Feldern():
    head()
    print("Funktionen auf allen Feldern ausführen:")

    df_copy = df.copy()

    print("")
    print("Alle leading oder trailing spaces werden entfernt:")

    df_copy = df_copy.apply(lambda x: x.str.strip())

    print("")
    print("Erledigt.")

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------

def p02_01_index():
    head()
    print("Feld 01 'Index' wird bereinigt:")

    df_copy = df.copy()

    df_copy['index'] = df_copy['index'].apply(bereinigen_nur_ziffern)
    
    # df_copy['index'] = df_copy['index'].apply(return_gueltigen_index)

    print("")
    print("Erledigt.")

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def p02_02_order_ID():
    head()
    print("Feld 02 'Order ID' wird bereinigt:")
    
    df_copy = df.copy()

    df_copy['Order ID'] = df_copy['Order ID'].apply(bereinigen_nur_ziffern_und_bindestrich)
    
    df_copy['Order ID'] = df_copy['Order ID'].apply(return_gueltige_order_ID)

    # Alle Datensätze löschen, bei denen das Feld 'Order ID' leer ist.
    df_copy = df_copy.dropna(subset=['Order ID'])

    print("")
    print("Erledigt.")

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def p02_03_date():
    head()
    print("Feld 03 'Date' wird bereinigt:")
    
    df_copy = df.copy()

    muster = r'[^0-9/-]'

    df_copy['Date'] = df_copy['Date'].apply(lambda x: re.sub(muster, '', x))
    
    df_copy['Date'] = df_copy['Date'].apply(return_gueltiges_datum)

    df_copy['Date'] = pd.to_datetime(df_copy['Date'], format='mixed')

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['Date'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def p02_04_status():
    head()
    print("Feld 04 'Status' wird bereinigt:")

    df_copy = df.copy()

    df_copy['Status'] = df_copy['Status'].str.upper()

    df_copy['Status'] = df_copy['Status'].apply(lambda x: re.sub(r'[^A-Z]', '', x))
    
    df_copy['Status'] = df_copy['Status'].apply(return_gueltigen_status)

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['Status'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def p02_05_fulfilment():

    def return_gueltiges_fulfilment(s):
        if s == "AMAZON" or s == "MERCHANT":
            return(s)
        else:
            return("#unknown")
            
    head()
    print("Feld 05 'Fulfilment' wird bereinigt:")

    df_copy = df.copy()

    df_copy['Fulfilment'] = df_copy['Fulfilment'].str.upper()

    df_copy['Fulfilment'] = df_copy['Fulfilment'].apply(lambda x: re.sub(r'[^A-Z]', '', x))
    
    df_copy['Fulfilment'] = df_copy['Fulfilment'].apply(return_gueltiges_fulfilment)

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['Fulfilment'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def p02_06_sales_channel():

    def return_gueltigen_sales_channel(s):
        if s == "AMAZONIN":
            return("Amazon.in")
        elif s == "NONAMAZON":
            return("Non-Amazon")
        else:
            return("#unknown")
            
    head()
    print("Feld 06 'Sales Channel' wird bereinigt:")

    df_copy = df.copy()

    df_copy['Sales Channel'] = df_copy['Sales Channel'].str.upper()

    df_copy['Sales Channel'] = df_copy['Sales Channel'].apply(lambda x: re.sub(r'[^A-Z]', '', x))
    
    df_copy['Sales Channel'] = df_copy['Sales Channel'].apply(return_gueltigen_sales_channel)

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['Sales Channel'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def p02_07_ship_service_level():

    def return_gueltigen_ship_service_level(s):
        if s == "STANDARD" or s == "EXPEDITED":
            return(s)
        else:
            return("#unknown")
            
    head()
    print("Feld 07 'ship-service-level' wird bereinigt:")

    df_copy = df.copy()

    df_copy['ship-service-level'] = df_copy['ship-service-level'].str.upper()

    df_copy['ship-service-level'] = df_copy['ship-service-level'].apply(lambda x: re.sub(r'[^A-Z]', '', x))
    
    df_copy['ship-service-level'] = df_copy['ship-service-level'].apply(return_gueltigen_ship_service_level)

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['ship-service-level'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def p02_08_category():

    def return_gueltige_category(s):

        gueltige_category = {"TSHIRT": "T-shirt",
                             "SHIRT": "Shirt",
                             "BLAZZER": "Blazzer",
                             "TROUSERS": "Trousers",
                             "PERFUME": "Perfume",
                             "SOCKS": "Socks",
                             "SHOES": "Shoes",
                             "WALLET": "Wallet",
                             "WATCH": "Watch"}

        if s in gueltige_category:
            return(gueltige_category[s])
        else:
            return("#unknown")

    head()
    print("Feld 08 'Category' wird bereinigt:")

    df_copy = df.copy()

    df_copy['Category'] = df_copy['Category'].str.upper()

    df_copy['Category'] = df_copy['Category'].apply(lambda x: re.sub(r'[^A-Z]', '', x))
    
    df_copy['Category'] = df_copy['Category'].apply(return_gueltige_category)

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['Category'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def feld_bereinigen(feld_nr, feld_name, replace_string, set_of_valid_values):

    def return_valid_value(s):

        if s in set_of_valid_values:
            return(set_of_valid_values[s])
        else:
            return("#unknown")

    head()
    print(f"Feld '{feld_nr}' '{feld_name}' wird bereinigt:")

    df_copy = df.copy()

    df_copy[feld_name] = df_copy[feld_name].str.upper()

    df_copy[feld_name] = df_copy[feld_name].apply(lambda x: re.sub(replace_string, '', x))
    
    df_copy[feld_name] = df_copy[feld_name].apply(return_valid_value)

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy[feld_name].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def p02_09_size():

    def return_gueltige_size(s):

        gueltige_size = {"S": "S",
			 "3XL": "3XL",
			 "XL": "XL",
			 "L": "L",
			 "XXL": "XXL",
			 "XS": "XS",
			 "6XL": "6XL",
			 "M": "M",
			 "4XL": "4XL",
			 "FREE": "Free",
			 "5XL": "5XL"}

        if s in gueltige_size:
            return(gueltige_size[s])
        else:
            return("#unknown")

    head()
    print("Feld 09 'Size' wird bereinigt:")

    df_copy = df.copy()

    df_copy['Size'] = df_copy['Size'].str.upper()

    df_copy['Size'] = df_copy['Size'].apply(lambda x: re.sub(r'[^3456EFLMRSX]', '', x))
    
    df_copy['Size'] = df_copy['Size'].apply(return_gueltige_size)

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['Size'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy
    
# --------------------------------------------------------------------------------

def p02_10_courier_status():

    def return_gueltigen_courier_status(s):

        gueltiger_courier_status = {"CANCELLED": "Cancelled",
					                "ON THE WAY": "On the Way",
                					"SHIPPED": "Shipped",
				                	"UNSHIPPED": "Unshipped"}

        if s in gueltiger_courier_status:
            return(gueltiger_courier_status[s])
        else:
            return("#unknown")

    head()
    print("Feld 10 'Courier Status' wird bereinigt:")

    df_copy = df.copy()

    df_copy['Courier Status'] = df_copy['Courier Status'].str.upper()

    df_copy['Courier Status'] = df_copy['Courier Status'].apply(lambda x: re.sub(r'[^A-Z ]', '', x))
    
    df_copy['Courier Status'] = df_copy['Courier Status'].apply(return_gueltigen_courier_status)

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['Courier Status'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy
    
# --------------------------------------------------------------------------------

def p02_11_qty():

    def return_gueltige_qty(s):
        if s is not None and s != "":
            if eval(s) >= 1:
                return(s)
            else:
                return(None)
        else:
            return(None)
            
    head()
    print("Feld 11 'Qty' wird bereinigt:")

    df_copy = df.copy()

    df_copy['Qty'] = df_copy['Qty'].apply(lambda x: re.sub(r'[^0-9]', '', x))
    
    # (lambda x: random_misspelling(str(x)) if pd.notnull(x) else x)
    
    # df_copy['Qty'] = df_copy['Qty'].apply(lambda x: str(x) if (eval(str(x)) >= 1) else None)

    df_copy['Qty'] = df_copy['Qty'].apply(return_gueltige_qty)

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['Qty'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def p02_12_waehrungen():
    head()
    print("Feld 12 'Currency' wird bereinigt:")

    df_copy = df.copy()

    # Unerlaubte Zeichen entfernen
    df_copy['currency'] = df_copy['currency'].str.replace(r'[^a-zA-Z€₹$]', '', regex=True)

    # alles in Grossbuchstaben ändern
    df_copy['currency'] = df_copy['currency'].str.upper()

    # definierte Zeichenketten in gültige Währungscodes umschlüsseln
    waehrungen = {"Rs": "INR",
                  "₹": "INR", 
                  "RUPEES": "INR",
                  "€": "EUR", 
                  "EURO": "EUR", 
                  "$": "USD",
                  "DOLLAR": "USD"}

    df_copy['currency'] = df_copy['currency'].replace(waehrungen)    

    # alle Codes die aus drei Grossbuchstaben bestehen akzeptieren; ansonsten in "#unknown" ändern
    df_copy['currency'] = df_copy['currency'].apply(lambda x: x if len(str(x)) == 3 else '#unknown')

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['currency'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def p02_13_amount():

    def return_gueltigen_amount(s):

        allowed_chars = f'^[0-9.]*$'

        # Prüfe, ob die Zeichenkette nur erlaubte Zeichen enthält

        if re.match(allowed_chars, s):
            return(str(s))
        else:
            return(None)

    head()
    print("Feld 13 'Amount' wird bereinigt:")

    df_copy = df.copy()

    methode = 2
    
    if methode == 1:

        df_copy['Amount'] = df_copy['Amount'].astype(str)

        df_copy['Amount'] = df_copy['Amount'].str.replace(" ", "", regex=False)

        df_copy['Amount'] = df_copy['Amount'].apply(return_gueltigen_amount)

        # Alle Datensätze löschen, bei denen das Feld 'Amount' leer ist.
        df_copy = df_copy.dropna(subset=['Amount'])

        df_copy['Amount'] = df_copy['Amount'].astype('float64', errors='ignore')

    else:
        df_copy['Amount'] = pd.to_numeric(df_copy['Amount'], errors='coerce')
    
        # Alle Datensätze löschen, bei denen das Feld 'Amount' leer ist.
        df_copy = df_copy.dropna(subset=['Amount'])

    print("")
    print("Erledigt.")
    print("")
    print(df_copy['Amount'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy
    
# --------------------------------------------------------------------------------

def p02_14_ship_city():

    def return_gueltige_ship_city(s):

        gueltige_ship_city = {""}

        if s in gueltige_ship_city:
            return(gueltige_ship_city[s])
        else:
            return("#unknown")

    head()
    print("Feld 14 'ship-city' wird bereinigt:")

    df_copy = df.copy()

    df_copy['ship-city'] = df_copy['ship-city'].str.upper()

    df_copy['ship-city'] = df_copy['ship-city'].apply(lambda x: re.sub(r'[^A-Z ]', '', x))
    
    # df_copy['ship-city'] = df_copy['ship-city'].apply(return_gueltige_ship_city)

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['ship-city'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def p02_15_ship_state():

    def return_gueltigen_ship_state(s):

        gueltiger_ship_state = {""}

        if s in gueltiger_ship_state:
            return(gueltiger_ship_state[s])
        else:
            return("#unknown")

    head()
    print("Feld 15 'ship-state' wird bereinigt:")

    df_copy = df.copy()

    df_copy['ship-state'] = df_copy['ship-state'].str.upper()

    df_copy['ship-state'] = df_copy['ship-state'].apply(lambda x: re.sub(r'[^A-Z ]', '', x))
    
    # df_copy['ship-state'] = df_copy['ship-state'].apply(return_gueltigen_ship_state)

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['ship-state'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def p02_16_ship_postal_code():
    head()
    print("Feld 16 'ship-postal-code' wird bereinigt:")

    df_copy = df.copy()

    # Wenn der Feldinhalt mit ".0" endet, dann dieses abschneiden
    df_copy['ship-postal-code'] = df_copy['ship-postal-code'].str.replace(r'\.0$', '', regex=True)

    # Alle Zeichen entfernen, die keine Ziffern sind
    df_copy['ship-postal-code'] = df_copy['ship-postal-code'].apply(lambda x: re.sub(r'[^0-9]', '', x))

    # Wenn der Feldinhalt aus exakt 6 Ziffern besteht, dann behalten. Ansonsten löschen.    
    df_copy['ship-postal-code'] = df_copy['ship-postal-code'].apply(lambda x: x if len(x) == 6 else '')

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['ship-postal-code'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def p02_17_ship_country():

    def return_gueltiges_ship_country(s):

        if s == "IN":
            return(s)
        else:
            return("#unknown")

    head()
    print("Feld 17 'ship-country' wird bereinigt:")

    df_copy = df.copy()

    df_copy['ship-country'] = df_copy['ship-country'].str.upper()

    df_copy['ship-country'] = df_copy['ship-country'].apply(lambda x: re.sub(r'[^A-Z]', '', x))
    
    df_copy['ship-country'] = df_copy['ship-country'].apply(return_gueltiges_ship_country)

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['ship-country'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

def p02_18_B2B():

    def return_gueltige_B2B(s):
        if s == "TRUE" or s == "FALSE":
            return(s)
        else:
            return("unknown")

    head()
    print("Feld 18 'B2B' wird bereinigt:")

    df_copy = df.copy()

    df_copy['B2B'] = df_copy['B2B'].str.upper()

    df_copy['B2B'] = df_copy['B2B'].apply(lambda x: re.sub(r'[^A-Z]', '', x))
    
    df_copy['B2B'] = df_copy['B2B'].apply(return_gueltige_B2B)

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['B2B'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy
    
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------

def p02_24_Phone_Number():
    head()
    print("Feld 24 'Phone_Number' wird bereinigt:")

    df_copy = df.copy()

    # Alle Zeichen entfernen, die keine Ziffern sind
    df_copy['Phone_Number'] = df_copy['Phone_Number'].apply(lambda x: re.sub(r'[^0-9]', '', x))

    print("")
    print("Ergebnis:")
    print("")
    print(df_copy['Phone_Number'].value_counts())

    if show_all:
        print("")
        input("--> Return")

    return df_copy

# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------

programmanfang()

daten_laden()

p00_dataset_analysieren()

df = p01_funktionen_auf_allen_Feldern()

# p00_alle_felder_einzeln_analysieren()

df = p02_01_index()
df = p02_02_order_ID()
df = p02_03_date()
df = p02_04_status()
df = p02_05_fulfilment()
df = p02_06_sales_channel()
df = p02_07_ship_service_level()

# p02_08_Category ----------------------------------------

gueltige_kategorien = {"TSHIRT": "T-shirt",
	                   "SHIRT": "Shirt",
	                   "BLAZZER": "Blazzer",
      	               "TROUSERS": "Trousers",
	                   "PERFUME": "Perfume",
	                   "SOCKS": "Socks",
	                   "SHOES": "Shoes",
	                   "WALLET": "Wallet",
	                   "WATCH": "Watch"}

df = feld_bereinigen("08", "Category", "r'[^A-Z]'", gueltige_kategorien)

# ----------------------------------------

df = p02_09_size()
df = p02_10_courier_status()
df = p02_11_qty()
df = p02_12_waehrungen()
df = p02_13_amount()
df = p02_14_ship_city()
df = p02_15_ship_state()
df = p02_16_ship_postal_code()

# p02_17_ship-country ----------------------------------------

df = feld_bereinigen("17", "ship-country", "r'[^A-Z]'", {"IN": "IN"})

# ----------------------------------------

df = p02_18_B2B()

df = feld_bereinigen("19", "fulfilled-by", "r'[^AEFHILPSY]'", {"EASY SHIP": "Easy Ship", "FALSE": "False"})

df['New'] = None

df['PendingS'] = None

# df['Delivery_Address'] = 

# df['Customer_Name'] =

df = p02_24_Phone_Number()

p00_dataset_analysieren()

daten_speichern()

programmende()

# --------------------------------------------------------------------------------




