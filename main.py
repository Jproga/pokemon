import telebot 
from config import token
from random import randint

from logic import Pokemon
from logic import Wizard
from logic import Fighter

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, pokemon.info_hp())
        bot.send_message(message.chat.id, pokemon.info_attack())
        bot.send_message(message.chat.id, pokemon.info_defense())
        bot.send_message(message.chat.id, pokemon.info_speed())
        bot.send_message(message.chat.id, pokemon.info_mana())  
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info())
        bot.send_photo(message.chat.id, pok.show_img())
        bot.send_message(message.chat.id, pok.info_hp())
        bot.send_message(message.chat.id, pok.info_attack())
        bot.send_message(message.chat.id, pok.info_defense())
        bot.send_message(message.chat.id, pok.info_speed())
        bot.send_message(message.chat.id, pok.info_mana()) 



bot.infinity_polling(none_stop=True)

