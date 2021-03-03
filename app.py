import requests
from lxml import html
from main import add_brand
from datetime import date

url = "https://app.spainery.com/brands"

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

response = requests.get('http://localhost:8050/render.html', params={'url':url,'wait': 2}, headers=headers)

tree = html.fromstring(html=response.text)

for brand in tree.xpath("//h5/text()"):
    brand_name = brand

    brands = {
        'brand_name': brand_name,
        'country': 'ES',
        'date': date.today()
    }

    print(brands)

    add_brand(brands['id'], brands['name'],brands['country'], brands['date'])

    
