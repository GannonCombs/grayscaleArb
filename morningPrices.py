import requests
import json
import os

#Get afternoon prices:
prices_dict = {"BTC": 0, "ETH": 0, "LTC": 0, "BCH": 0, "ETC": 0}
response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot").json()
prices_dict["BTC"] = response["data"]["amount"]
response = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot").json()
prices_dict["ETH"] = response["data"]["amount"]
response = requests.get("https://api.coinbase.com/v2/prices/LTC-USD/spot").json()
prices_dict["LTC"] = response["data"]["amount"]
response = requests.get("https://api.coinbase.com/v2/prices/BCH-USD/spot").json()
prices_dict["BCH"] = response["data"]["amount"]
response = requests.get("https://api.coinbase.com/v2/prices/ETC-USD/spot").json()
prices_dict["ETC"] = response["data"]["amount"]
print("Prices - ", prices_dict)

#Write prices to file
working_directory = os.path.dirname(os.path.abspath(__file__))
file_path = working_directory + '/afternoonPrices.txt'
with open(file_path, 'w') as outfile:
    json.dump(prices_dict, outfile)
