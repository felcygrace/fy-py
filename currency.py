def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0
    Euro=0.01417
    British_Pound=0.0100
    Australian_Dollar=0.02140
    Canadian_Dollar=0.02027
    if current_currency_name=="Euro":
        current_currency_amount=amount_needed_inr*Euro
    elif current_currency_name=="British_Pound":
        current_currency_amount=amount_needed_inr*British_Pound
    elif current_currency_name=="Australian_Dollar":
        current_currency_amount=amount_needed_inr*Australian_Dollar
    elif current_currency_name=="Canadian_Dollar":
        current_currency_amount=amount_needed_inr*Canadian_Dollar
    else:
        print("-1")
    return current_currency_amount
currency_needed=convert_currency(3500,"British_Pound")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")
