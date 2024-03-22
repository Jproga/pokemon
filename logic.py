from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = self.get_hp()
        self.power = self.get_attack()
        self.defense = self.get_defense()
        self.speed = self.get_speed()
        self.mana = self.get_mana()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_shiny'])
        else:
            return "Изображения нет"

    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    # метод для получения информацции о информации через api
    def get_hp(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][0]['base_stat'])
        else:
            return "Информации о хп нет"
    def get_attack(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][1]['base_stat'])
        else:
            return "Информации о атаке нет"   
    def get_defense(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][2]['base_stat'])
        else:
            return "Информации о защите нет"
    def get_speed(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][5]['base_stat'])
        else:
            return "Информации о скорости нет"  

    def get_mana(self):
        get_mana2 = randint(1, 125)
        return get_mana2
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        


    # Метод класса для получения информации
    def info(self):
            return f"Имя твоего покеомона: {self.name}."
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    def info_hp(self):
        return f"хп покемона: {self.hp}."
    def info_attack(self):
        return f"атака покемона: {self.power}."
    # Метод класса для получения картинки покемона
    def info_defense(self):
        return f"защита покемона: {self.defense}."
    def info_speed(self):
        return f"скорость покемона: {self.speed}."
    def info_mana(self):
        return f"мана покемона: {self.mana}."
    

class Wizard(Pokemon):
    def attack(self, enemy):
        super_attack = randint(5, 15)
        self.power += super_attack
        result = super().attack(enemy)
        self.power -= super_attack
        return f"{result}\nБоец применил супер-атаку: {super_attack}"
        
class Fighter(Pokemon):
    def attack(self, enemy):
        super_attack = randint(5, 15)
        self.power += super_attack
        result = super().attack(enemy)
        self.power -= super_attack
        return f"{result}\nБоец применил супер-атаку: {super_attack}"
    
if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))
