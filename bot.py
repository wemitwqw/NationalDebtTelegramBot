import telegram
import time
from bs4 import BeautifulSoup
import requests
import random
import json

#MAIN
chat_ID = CHAT_ID_SIIA
bot = telegram.Bot(token='BOT_TOKEN_SIIA')

#USA Debt
debt_URL = "https://www.pgpf.org/national-debt-clock"

#HeaderUserAgentSpoof
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3198.0 Safari/537.36 OPR/49.0.2711.0',
    'Opera/9.80 (Linux armv7l) Presto/2.12.407 Version/12.51 , D50u-D1-UHD/V1.5.16-UHD (Vizio, D50u-D1, Wireless)',
    ]

def ProxyGrab():
    req = requests.get("https://proxy11.com/api/proxy.json?key=PROXY11_TOKEN_SIIA&limit=1&port=80")
    dataproxy = req.json()
    proxy = '{' + "'http': '" + dataproxy['data'][0]["ip"] + ":" + dataproxy['data'][0]["port"] + "'}"
    return proxy

def HeaderUserAgentSpoof(list):
    user_agent = random.choice(list)
    headers = { 
    'User-Agent': user_agent, 
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
    'Accept-Language' : 'en-US,en;q=0.5', 
    'Accept-Encoding' : 'gzip', 
    'DNT' : '1',
    'Connection' : 'close' 
    }
    return headers
    
def USADebt():
    proxyFormat = eval(ProxyGrab())
    header = HeaderUserAgentSpoof(user_agent_list)
    
    s = requests.session()
    req = s.get(debt_URL, headers = header, proxies = proxyFormat)
    soup = BeautifulSoup(req.content, 'html.parser')
    debt = soup.find("div", class_ = "debt-gross")
    bot.sendMessage(chat_ID, text = "В данный момент национальный долг США составляет: \n" + debt.text)
    s.cookies.clear()

if __name__ == '__main__':
    USADebt()
