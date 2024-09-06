#fetching data from an API 

import requests 

response = requests.get("https://open.er-api.com/v6/latest/USD")

if(response.status_code == 200):        
    data = response.json()   # storing all the response data in data variable
    exchangeRates = data["rates"] #extracting only the rates property from data
    
    try:
        
        print("-----Welcome to currency exchange------")
        print("type the standard currency you want to convert to USD")

        print("Convert Currency:", end=" ")    
        initialCurrency = input().strip().upper()  #currency to convert. Type the standard currency example : NRB , USD , INR
        print("To:",end=" ")
        secondCurrency = input().strip().upper()  # Here also type the standard currency
        print(f"initial currency:{initialCurrency} {exchangeRates[initialCurrency]} is equivalent to: {secondCurrency} {exchangeRates[secondCurrency]}")
        
    except:
        print("No such currency Found ")
        

