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
for event in longpoll.listen():
    if event.to_me:
        time.sleep(1)
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
            day = event.text
            match day:
                case 'Понедельник':
                    if int(week_number)%2 == 1:
                        vk.messages.send(
                                        user_id=event.user_id,
                                        message='Понедельник: Числитель\n'+
                                        "I: Эконом. предприятия лекц. 1-205\n"+
                                        "II: Эконом. предприятия упр. 1-205\n"+
                                        'III: Осн. проек. реж. инструмент. лекц. 1-209\n'+
                                        'IV: Техн. инструмент. произв. упр. 1-210\n'+ main_time,
                                        random_id=0,
                                        keyboard=keyboard.get_keyboard()
                                        )
                    else:
                        vk.messages.send(
                                        user_id=event.user_id,
                                        message='Понедельник: Знаменатель\n'+
                                        "I: Эконом. предприятия лекц. 1-205\n"+
                                        "II: Прог. упр. автом. оборуд. лаб 3-203\n"+
                                        'III: Осн. проек. реж. инструмент. лекц. 1-209\n'+
                                        'IV: Техн. инструмент. произв. упр. 1-210\n'+ main_time,
                                        random_id=0,
                                        keyboard=keyboard.get_keyboard()
                                        )
                case 'Вторник':
                    if int(week_number)%2 == 1:
                        vk.messages.send(
                                        user_id=event.user_id,
                                        message='Вторник: Числитель\n'+
                                        "I: Полный и спокойный сон\n"+
                                        "II: Прекрасный чилаут\n"+
                                        'III: Расслабон\n'+ main_time,
                                        random_id=0,
                                        keyboard=keyboard.get_keyboard()
                                        )
                    else:
                        vk.messages.send(
                                        user_id=event.user_id,
                                        message='Вторник: Знаменатель\n'+
                                        "I: Полный и спокойный сон\n"+
                                        "II: Прекрасный чилаут\n"+
                                        'III: Расслабон\n'+ main_time,
                                        random_id=0,
                                        keyboard=keyboard.get_keyboard()
                                        )
                case 'Среда':
                    if int(week_number)%2 == 1:
                        vk.messages.send(
                                        user_id=event.user_id,
                                        message='Среда: Числитель\n'+
                                        "I: ОКП лаб. 3-210\n"+
                                        "II: Прог. упр. автом. оборуд. лекц. 1-218\n"+
                                        'III: Станк. инстр. производ. лекц. 1-218\n'+
                                        'IV: Техн. инструмент. произв. упр. 1-105\n'+ main_time,
                                        random_id=0,
                                        keyboard=keyboard.get_keyboard()
                                        )
                    else:
                        vk.messages.send(
                                        user_id=event.user_id,
                                        message='Среда: Знаменатель\n'+
                                        "I: Полный и спокойный сон\n"+
                                        "II: Прог. упр. автом. оборуд. лекц. 1-218\n"+
                                        'III: Станк. инстр. производ. лекц. 1-218\n'+
                                        'IV: Техн. инструмент. произв. упр. 1-105\n'+ main_time,
                                        random_id=0,
                                        keyboard=keyboard.get_keyboard()
                                        )
                case 'Четверг':
                    if int(week_number)%2 == 1:
                        vk.messages.send(
                                        user_id=event.user_id,
                                        message='Четверг: Числитель\n'+
                                        "I: Осн. проек. реж. инструмент. упр. 1-209\n"+
                                        "II: ОКП лекц. 1-107\n"+
                                        'III: Русс. яз 1-205\n'+
                                        'IV: НИР к.1\n'+ main_time,
                                        random_id=0,
                                        keyboard=keyboard.get_keyboard()
                                        )
                    else:
                        vk.messages.send(
                                        user_id=event.user_id,
                                        message='Четверг: Знаменатель\n'+
                                        "I: Осн. проек. реж. инструмент. упр. 1-209\n"+
                                        "II: ОКП упр. 1-107\n"+
                                        'III: НИР к.1\n'+ main_time,
                                        random_id=0,
                                        keyboard=keyboard.get_keyboard()
                                        )
                case 'Пятница':
                    if int(week_number)%2 == 1:
                        vk.messages.send(
                                        user_id=event.user_id,
                                        message='Пятница: Числитель\n'+
                                        "I: Чиллаут\n"+
                                        "II: Техн. инструмент. произв. лекц 1-210\n"+
                                        'III: Осн. проек. реж. инструмент. лаб. 1-105\n'+
                                        'IV: Курсач к.1\n'+ main_time,
                                        random_id=0,
                                        keyboard=keyboard.get_keyboard()
                                        )
                    else:
                        vk.messages.send(
                                        user_id=event.user_id,
                                        message='Пятница: Знаменатель\n'+
                                        "I: Осн. проек. реж. инструмент. лекц. 1-209\n"+
                                        "II: Техн. инструмент. произв. лекц 1-210\n"+
                                        'III: Осн. проек. реж. инструмент. лаб. 1-105\n'+
                                        'IV: Курсач к.1\n'+ main_time,
                                        random_id=0,
                                        keyboard=keyboard.get_keyboard()
                                        )
                case 'Суббота':
                    if int(week_number)%2 == 1:
                        vk.messages.send(
                                        user_id=event.user_id,
                                        message='Суббота: Числитель\n'+
                                        "I: Чиллаут\n"+
                                        "II: Станк. инстр. производ. упр. 1-209\n"+
                                        'III: Станк. инстр. производ. лаб. 1-106\n'+ main_time,
                                        random_id=0,
                                        keyboard=keyboard.get_keyboard()
                                        )
                    else:
                        vk.messages.send(
                                        user_id=event.user_id,
                                        message='Суббота: Знаменатель\n'+
                                        "I: Чиллаут\n"+
                                        "II: Спокойный сон\n"+
                                        'III: Станк. инстр. производ. лаб. 1-106\n'+ main_time,
                                        random_id=0,
                                        keyboard=keyboard.get_keyboard()
                                        )
                case 'Сегодня':
                    if int(week_number)%2 == 1:
                        vk.messages.send(
                                        user_id=event.user_id,
                                        message='Вот тебе время!\n'+main_time
                                        +'\n'+'Остальное не готово, но сегодня ЧИСЛИТЕЛЬ',
                                        random_id=0,
                                        keyboard=keyboard.get_keyboard()
                                        )
                    else:
                        vk.messages.send(
                                        user_id=event.user_id,
                                        message='Вот тебе время!\n'+main_time
                                        +'\n'+'Остальное не готово, но сегодня ЗНАМЕНАТЕЛЬ',
                                        random_id=0,
                                        keyboard=keyboard.get_keyboard()
                                        )