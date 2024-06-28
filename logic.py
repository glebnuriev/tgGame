from random import randint
import requests
from datetime import datetime, deltatime

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(50,100)
        self.power = randint(10,20)
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']["other"]['official-artwork']["front_default"])
        else:
            return "https://www.google.com/imgres?q=pikachu&imgurl=http%3A%2F%2Fwww.smashbros.com%2Fimages%2Fog%2Fpikachu.jpg&imgrefurl=https%3A%2F%2Fwww.smashbros.com%2Fwiiu-3ds%2Fsp%2Fru%2Fcharacters%2Fpikachu.html&docid=pLVFifdpovS1oM&tbnid=fSNivuU-JUDe4M&vet=12ahUKEwjnvKvN8MmGAxWSFRAIHaGLABMQM3oECBQQAA..i&w=1500&h=1500&hcb=2&ved=2ahUKEwjnvKvN8MmGAxWSFRAIHaGLABMQM3oECBQQAA"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
    
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.current()  
        delta_time = timedelete(hours=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"  
            
    


    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
Здоровье покемона: {self.hp}
Сила покемона: {self.power}"""

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img


    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1,5)
            if chance == 1:
                return "покемон волшебник применил щит"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
    


class Wizard(Pokemon):
    def info(self):
        return "у тебя покемон волшебник " + super().info()
class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"Боец применил супер атаку силой {super_power}"
    

    def info(self):
        return "у тебя покемон боец " + super().info()

if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))