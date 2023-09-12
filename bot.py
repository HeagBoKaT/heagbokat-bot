import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard
import time
import datetime

# Токен вашего сообщества
TOKEN = 'vk1.a.qf1brHS5W4SQ4XmMXlO9nBC6fYjg5VfEhMzcFRHLmGn1VYu-l_BDgzwc08nKMCCw2BDXQEgCcaHxFGCwJLjw-f8Q4LEJ0wF5FJWVLpjVGAXmcB1I10l8sFY3_r2TlScPdCreHZzSQN3hWthgSncNRrO2HjwNFK2_k1fuzeQKmxr5YKsNIu5Pcucd-QrqNdJsIq-fGjVK5YCO7JlIxoyO4w'

# Авторизация бота
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

# Получаем объект для работы с Long Poll API
longpoll = VkLongPoll(vk_session)
keyboard = VkKeyboard(one_time=False)
keyboard.add_button('Понедельник', color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
keyboard.add_button('Вторник', color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Среда', color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
keyboard.add_button('Четверг', color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Пятница', color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
keyboard.add_button('Суббота', color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Сегодня', color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
# Основной цикл бота
while True:
    try:
        for event in longpoll.listen():
            if event.to_me:
                time.sleep(1)
                print(event.user_id)
                if event.text != 'Понедельник' and event.text != 'Вторник' and event.text != 'Среда' and event.text != 'Четверг' and event.text != 'Пятница' and event.text != 'Суббота' and event.text != 'Сегодня':
                    vk.messages.send(
                                    user_id=event.user_id,
                                    message='Выберите день недели',
                                    random_id=0,
                                    keyboard=keyboard.get_keyboard()
                                    )
                else:
                    current_date = datetime.date.today()
                    week_number = current_date.strftime('%U')
                    main_time = datetime.datetime.now().strftime('%H'+':'+ '%M'+':'+ '%S')
                    today = datetime.datetime.now().strftime('%A')
                    day = event.text
                    match day:
                        case 'Понедельник':
                            if int(week_number)%2 == 1:
                                with open('monday+.heagbokat', 'r', encoding='utf-8') as f:
                                    txt = f.read()
                                vk.messages.send(
                                                user_id=event.user_id,
                                                message=txt+"\n"+ main_time,
                                                random_id=0,
                                                keyboard=keyboard.get_keyboard()
                                                )
                            else:
                                with open('monday-.heagbokat', 'r', encoding='utf-8') as f:
                                    txt = f.read()
                                vk.messages.send(
                                                user_id=event.user_id,
                                                message=txt+"\n"+ main_time,
                                                random_id=0,
                                                keyboard=keyboard.get_keyboard()
                                                )
                        case 'Вторник':
                            if int(week_number)%2 == 1:
                                with open('tuesday+.heagbokat', 'r', encoding='utf-8') as f:
                                    txt = f.read()
                                vk.messages.send(
                                                user_id=event.user_id,
                                                message=txt+"\n"+ main_time,
                                                random_id=0,
                                                keyboard=keyboard.get_keyboard()
                                                )
                            else:
                                with open('tuesday-.heagbokat', 'r', encoding='utf-8') as f:
                                    txt = f.read()
                                vk.messages.send(
                                                user_id=event.user_id,
                                                message=txt+"\n"+ main_time,
                                                random_id=0,
                                                keyboard=keyboard.get_keyboard()
                                                )
                        case 'Среда':
                            if int(week_number)%2 == 1:
                                with open('wednesday+.heagbokat', 'r', encoding='utf-8') as f:
                                    txt = f.read()
                                vk.messages.send(
                                                user_id=event.user_id,
                                                message=txt+"\n"+ main_time,
                                                random_id=0,
                                                keyboard=keyboard.get_keyboard()
                                                )
                            else:
                                with open('wednesday-.heagbokat', 'r', encoding='utf-8') as f:
                                    txt = f.read()
                                vk.messages.send(
                                                user_id=event.user_id,
                                                message=txt+"\n"+ main_time,
                                                random_id=0,
                                                keyboard=keyboard.get_keyboard()
                                                )
                        case 'Четверг':
                            if int(week_number)%2 == 1:
                                with open('thursday+.heagbokat', 'r', encoding='utf-8') as f:
                                    txt = f.read()
                                vk.messages.send(
                                                user_id=event.user_id,
                                                message=txt+"\n"+ main_time,
                                                random_id=0,
                                                keyboard=keyboard.get_keyboard()
                                                )
                            else:
                                with open('thursday-.heagbokat', 'r', encoding='utf-8') as f:
                                    txt = f.read()
                                vk.messages.send(
                                                user_id=event.user_id,
                                                message=txt+"\n"+ main_time,
                                                random_id=0,
                                                keyboard=keyboard.get_keyboard()
                                                )
                        case 'Пятница':
                            if int(week_number)%2 == 1:
                                with open('friday+.heagbokat', 'r', encoding='utf-8') as f:
                                    txt = f.read()
                                vk.messages.send(
                                                user_id=event.user_id,
                                                message=txt+"\n"+ main_time,
                                                random_id=0,
                                                keyboard=keyboard.get_keyboard()
                                                )
                            else:
                                with open('friday-.heagbokat', 'r', encoding='utf-8') as f:
                                    txt = f.read()
                                vk.messages.send(
                                                user_id=event.user_id,
                                                message=txt+"\n"+ main_time,
                                                random_id=0,
                                                keyboard=keyboard.get_keyboard()
                                                )
                        case 'Суббота':
                            if int(week_number)%2 == 1:
                                with open('saturday+.heagbokat', 'r', encoding='utf-8') as f:
                                    txt = f.read()
                                vk.messages.send(
                                                user_id=event.user_id,
                                                message=txt+"\n"+ main_time,
                                                random_id=0,
                                                keyboard=keyboard.get_keyboard()
                                                )
                            else:
                                with open('saturday-.heagbokat', 'r', encoding='utf-8') as f:
                                    txt = f.read()
                                vk.messages.send(
                                                user_id=event.user_id,
                                                message=txt+"\n"+ main_time,
                                                random_id=0,
                                                keyboard=keyboard.get_keyboard()
                                                )
                        case 'Сегодня':
                            if int(week_number)%2 == 1:
                                name_today = str(today).lower()+"+.heagbokat"
                                #print(name_today)
                                with open(name_today, 'r', encoding='utf-8') as f:
                                    txt = f.read()
                                vk.messages.send(
                                                user_id=event.user_id,
                                                message=txt+"\n"+ main_time,
                                                random_id=0,
                                                keyboard=keyboard.get_keyboard()
                                                )
                            else:
                                name_today = str(today).lower()+"-.heagbokat"
                                #print(name_today)
                                with open(name_today, 'r', encoding='utf-8') as f:
                                    txt = f.read()
                                vk.messages.send(
                                                user_id=event.user_id,
                                                message=txt+"\n"+ main_time,
                                                random_id=0,
                                                keyboard=keyboard.get_keyboard()
                                                )
    except Exception:
        pass
        