"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem
import logging
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def get_planets(update, context):
    list_planets = []
    for name in ephem._libastro.builtin_planets():
        if name[1] == 'Planet':
            list_planets.append(name[2])
    if context.args:
        user_message = context.args[0]
        print(user_message)
        if user_message in list_planets:
            print(f'{user_message} в списке есть.')
            planet = getattr(ephem, user_message)
            planet = planet(date.today())
            planet_constellation = ephem.constellation(planet)
            return update.message.reply_text(f'Планета {user_message} находится в созвездии {planet_constellation}')
        else:
            return update.message.reply_text('Такой планеты не найдено')
    else:
        return update.message.reply_text(list_planets)


def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather",  use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planets", get_planets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
