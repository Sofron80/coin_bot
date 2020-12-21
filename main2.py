from selenium import webdriver
import time, re, urllib, requests

from telethon.sync import TelegramClient
from config import api_id, api_hash


client = TelegramClient('name', api_id, api_hash)

client.start()


dlgs = client.get_dialogs()

tegmo = None

for dlg in dlgs:
    if dlg.title == "LTC Click Bot":
        tegmo = dlg

if tegmo == None:
    print("Отсутствует чат с ботом")
    exit()


print(tegmo.title)

# dr_options = webdriver.FirefoxOptions()
# dr_options.set_headless()
# driver = webdriver.Firefox(options=dr_options)

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(chrome_options=chrome_options)

tmp_url = ''
n = 0
nn = 0
links = True
links2 = True
try:
    while True:
        msg = client.get_messages(tegmo, limit=1)[0]

        if re.search(r'\bThere is a new site for you to\b', msg.message):
            client.send_message(  tegmo , "🖥 Visit sites")

        if re.search(r'\bPlease stay on the site for at least 10 seconds\b', msg.message):
            time.sleep(10)
            continue

        if re.search(r'\bSorry\b', msg.message):
            time.sleep(10)
            nn = nn + 1
            print('Закончились ссылки ждем','.'*nn,  end='\r')
            client.send_message(  tegmo , "🖥 Visit sites")
            continue

        if re.search(r'\bPress the "Visit website" button to earn LTC\b', msg.message):
            nn = 0
            url = msg.reply_markup.rows[0].buttons[0].url
            if tmp_url == url:
                nn = nn + 1

                print("ссыдка с задежкой", '.'*nn , end='\r')
                time.sleep(5)

                t_el = driver.find_elements_by_class_name('timer')
                text = ''
                for i in t_el:
                    if (len(i.text) > 0):
                        text = i.text
                        i.click()
                print(text)
                
                if ''.join(text) == '':
                    client.send_message(  tegmo , "🖥 Visit sites")

                links2 = False
                continue
            links = True
            print("переходим по ссылке", url)
            driver.get(url)
            
            n = n + 1
            print("проходов ",n)

            tmp_url = url
            time.sleep(2)
            
except Exception as ex:
    print(ex)
finally:
    driver.close()
