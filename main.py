from selenium import webdriver
import time, re, urllib, requests

from telethon.sync import TelegramClient, events
from config import api_id, api_hash

n = 0


client = TelegramClient('name', api_id, api_hash)

client.start()


dlgs = client.get_dialogs()

for dlg in dlgs:
    if dlg.title == "LTC Click Bot":
        tegmo = dlg

print(tegmo.title)

class RunChromeTests():
    def testMethod(self):
        caps = {'browserName', 'chrome'}
        driver = webdriwer.Remote(command_executor="http://localhost:4444/wb/hub", desired_capabilities=caps)
        driver.maximize_window()
        driver.get(url_rec)
        time.sleep(waith + 20)
        driver.close()
        driver.quit()



while True:
    msgs = client.get_messages(tegmo, limit=1)

    for mes in msgs:
        if re.search(r'\bseconds to get your reward\b', mes.message):
            print("найден reward")
            str_a = str(mes.message)
            wainin = int(re.findall(r'\d+', str_a)[0])
            print("Ждать придеться", wainin)
            client.send_messages('LTC Client Bot', "/visit")
            time.sleep(3)
            msgs2 = client.get_messages(tegmo, limit=1)
            for mes2 in msgs2:
                nutton_data = msg2.reply_markup.row[1].buttons[1].data
                message_id = mes2.id

                print("Перехожу по ссылке")
                time.sleep(2)
                url_rec = message[0].reply_markup.row[0].button[0].url
                print("Start selenium")
                ch = RunChromeTests()
                ch.testMethod()
                time.sleep(6)
                fp = urllib.request.urlopen(url_rec)
                mybytes = fb.read()
                mystr = mybytes.decode("utf8")
                fb.close()
                if re.search(r'\bSwitch to reCAPTCHA\b', mystr):
                    from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
                    resp = client(GetBotCallbackAnswerRequest(
                        'LTC Click Bot',
                        message_id,
                        data=button_data
                    ))
                    time.sleep(2)
                    print("Капча")
                else:
                    time.sleep(wainin)
                    time.sleep(2)
        elif re.search(r'\bSorry\b', mes.message):
            client.send_message('LTC Client Bot', "/visit")
            time.sleep(6)
            print("Ненайдено Sorry")

        else:
            messages = client.get_messages(tegmo, limit=1)
            url_rec = messages[0].reply_markup.rows[0].buttons[0].url
            f = open("rep.txt")
            fd = f.read()
            if fd == url_rec:
                print("Найдено повторение переменной")
                msgs2 = client.get_messages(tegmo, limit=1)
                for msg2 in msgs2:
                    button_data = msg2.reply_markup.rows[1].buttons[1].data
                    message_id = msg2.id
                    from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
                    resp = client(GetBotCallbackAnswerRequest(
                        tegmo,
                        message_id,
                        data=button_data
                    ))
                    time.sleep(2)
            else:
                url = 'https://www.virustotal.com/vtapi/v2/url/scan'
                params ={
                    'apikey' :'e2754bf78167df396b0676d94072285ae17030b508b6a432340ec24d581adf0d',
                    'url': url_rec
                }
                response = requests.post(url, data=params)
                my_file = open('rep.txt', 'w')
                my_file.write(url_rec)
                print("Новая запись в файле сделана")
                time.sleep(16)
                n = n + 1
                print("Пройдено циклов", n)



        