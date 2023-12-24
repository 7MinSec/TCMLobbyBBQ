import requests

url = "https://discord.com/api/webhooks/1188217451549294664/Z9YXQNKd1SVaOZPkv4DNcHT78Ht_otc6R0f3irT7uCk_-zOix7qRRVukZoNU-F1yTYVi"

data = {
    "content" : "OMG I can't believe it, you're actually starting a match!",
    "username" : "TCMLobbyBBQ says:"
    }
    
result = requests.post(url, json = data)
result.raise_for_status()
#break