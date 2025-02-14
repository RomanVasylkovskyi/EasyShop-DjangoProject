from django.shortcuts import render
import requests
from .models import Postomat
import os
from dotenv import load_dotenv
load_dotenv()

nova_poshta_api_key = os.getenv('NOVA_POSHTA_API_KEY')

def fetch_postomats(request):
    api_key = 'ВАШ_API_КЛЮЧ'
    url = 'https://api.novaposhta.ua/v2.0/json/'
    payload = {
        "apiKey": api_key,
        "modelName": "Address",
        "calledMethod": "getWarehouses",
        "methodProperties": {
            "TypeOfWarehouseRef": "841339c7-591a-42e2-8233-7a0a00f0ed6f"
        }
    }

    response = requests.post(url, json=payload)
    data = response.json()

    if data['success']:
        for item in data['data']:
            Postomat.objects.update_or_create(
                name=item['Description'],
                defaults={
                    'address': item['ShortAddress'],
                    'latitude': float(item['Latitude']),
                    'longitude': float(item['Longitude']),
                }
            )

    return render(request, 'postomats/map.html')
