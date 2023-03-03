import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
init()

url = 'https://www.amazon.es/Desmontar-Ensamblarde-Construcciones-Excavadora-herramientas/dp/B07WQTSPGF/ref=d_deals_ic_sccl_2_6/262-5740346-3949253?pd_rd_w=HGcKG&content-id=amzn1.sym.5e7ef1f0-5aa4-4fc7-a655-4095e5ef03ad&pf_rd_p=5e7ef1f0-5aa4-4fc7-a655-4095e5ef03ad&pf_rd_r=KB3RV1TZXJGNY3RS7ZGV&pd_rd_wg=1wnTv&pd_rd_r=5f6eddaa-b9a4-4147-b8cb-63a5b70cf8e4&pd_rd_i=B07WQTSPGF&psc=1'  # Server hostname or IP address

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find('span', {'class': 'a-size-large product-title-word-break'}).text.strip()

precio = soup.find('span', {'class': 'a-offscreen'}).text
precio = precio.replace('€', '')
precio = precio.replace(',', '.')
precio = float(precio)

print (Fore.RED + 'Producto: ', title)
print(Fore.GREEN + 'El precio del producto es:', precio,'€')
