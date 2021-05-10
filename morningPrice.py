import requests
import json
import os
from termcolor import colored

# Look to the path of your current working directory
working_directory = os.path.dirname(os.path.abspath(__file__))
file_path = working_directory + '/afternoonPrices.txt'

# Read afternoon prices:
with open(file_path) as f:
  afternoonPrices = json.load(f)
  print("Afternoon prices: \n", afternoonPrices)

# Get morning prices:
morningPrices = {"BTC": 0, "ETH": 0, "LTC": 0, "BCH": 0, "ETC": 0}
response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot").json()
morningPrices["BTC"] = response["data"]["amount"]
response = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot").json()
morningPrices["ETH"] = response["data"]["amount"]
response = requests.get("https://api.coinbase.com/v2/prices/LTC-USD/spot").json()
morningPrices["LTC"] = response["data"]["amount"]
response = requests.get("https://api.coinbase.com/v2/prices/BCH-USD/spot").json()
morningPrices["BCH"] = response["data"]["amount"]
response = requests.get("https://api.coinbase.com/v2/prices/ETC-USD/spot").json()
morningPrices["ETC"] = response["data"]["amount"]
print("Morning prices: \n", morningPrices)

# Calculate percent difference:
pctDiff = {"BTC": (float(morningPrices["BTC"]) / float(afternoonPrices["BTC"]) - 1) * 100,
           "ETH": (float(morningPrices["ETH"]) / float(afternoonPrices["ETH"]) - 1) * 100,
           "LTC": (float(morningPrices["LTC"]) / float(afternoonPrices["LTC"]) - 1) * 100,
           "BCH": (float(morningPrices["BCH"]) / float(afternoonPrices["BCH"]) - 1) * 100,
           "ETC": (float(morningPrices["ETC"]) / float(afternoonPrices["ETC"]) - 1) * 100}

print("Percent difference (old view): \n", pctDiff)
