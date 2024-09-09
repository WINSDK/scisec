from bs4 import BeautifulSoup
import requests

# Change this to your proxy addr, (use arti with -p 5050).
proxies = {
    'http': 'socks5h://127.0.0.1:5050',
    'https': 'socks5h://127.0.0.1:5050'
}
url = 'http://santat7kpllt6iyvqbr7q4amdv6dzrh6paatvyrzl7ry3zm72zigf4ad.onion'

html = requests.get(url, proxies).text()
soup = BeautifulSoup(html, 'html.parser')
menu_particle = soup.find('div', id='menu-6409-particle')

links = menu_particle.find_all('a')

exceptions = [
    "/how-to-download",
    "/",
    "#",
]

for link in links:
    url = link.get('href')
    text = link.get_text(strip=True)
    if url in exceptions:
        continue

    print("http://santat7kpllt6iyvqbr7q4amdv6dzrh6paatvyrzl7ry3zm72zigf4ad.onion" + url)
