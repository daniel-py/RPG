class bcolours:
    HEADER= '\033[95m'
    OKBLUE= '\033[94m'
    OKGREEN= '\033[92m'
    WARNING= '\033[93m'
    FAIL= '\033[91m'
    ENDC= '\033[0m'
    BOLD= '\033[1m'
    UNDERLINE= '\033[4m'

import random


class person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp= hp
        self.hp= hp
        self.maxmp= mp
        self.mp= mp
        self.atkl= atk -10
        self.atkh= atk +10
        self.df= df
        self.magic= magic
        self.items = items
        self.actions= ["Attack", "Magic", "Items"]
        self.name = name
        
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
  
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp= 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self. maxhp
    
    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxmp
    
    def reduce_mp(self, cost):
        self.mp -= cost
    
    def choose_action(self):
        i= 1
        print(f"\n    {bcolours.BOLD}{self.name}{bcolours.ENDC}")
        print(f"{bcolours.OKBLUE}{bcolours.BOLD}    ACTIONS{bcolours.ENDC}")
        for item in self.actions:
            print("        "+str(i), ":", item)
            i += 1
            
    def choose_magic(self):
        i = 1
        print(f"\n{bcolours.OKBLUE}{bcolours.BOLD}    MAGIC{bcolours.ENDC}")
        for spell in self.magic:
            print("        "+str(i) + ".", spell.name, "(Cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print(f"\n{bcolours.OKGREEN}{bcolours.BOLD}    ITEMS{bcolours.ENDC}")
        for item in self.items:
            print(f"         {str(i)}. {item['item'].name} : {item['item'].description} (x{item['quantity']})")  
            i +=1

    def choose_target(self, enemies):
        i = 1
        print(f"\n{bcolours.FAIL}{bcolours.BOLD}    TARGET:{bcolours.ENDC}")
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print(f"        {str(i)}. {enemy.name}")
                i += 1
        choice = int(input("    Choose target: ")) - 1
        return choice
    
    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp/self.maxhp) * 50
        
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = f"{self.hp}/{self.maxhp}"
        while len(hp_string) < 11:
            hp_string += " "

        print("                           __________________________________________________")
        print(f"{bcolours.BOLD}{self.name}         {hp_string} {bcolours.FAIL}|{hp_bar}|{bcolours.ENDC}")


    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp/self.maxhp) * 25

        mp_bar = ""
        mp_ticks = (self.mp/self.maxmp) * 10


        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "
            
        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "
        
        hp_string = f"{self.hp}/{self.maxhp}"
        while len(hp_string) < 9:
            hp_string += " "

        mp_string = f"{self.mp}/{self.maxmp}"
        while len(mp_string) < 7:
            mp_string += " "


        print("                              _________________________            __________")
        print(f"{bcolours.BOLD}{self.name}             {hp_string} {bcolours.OKGREEN}|{hp_bar}|{bcolours.ENDC}   {bcolours.BOLD}{mp_string}{bcolours.OKBLUE}|{mp_bar}|{bcolours.ENDC}")


    def choose_enemy_spell(self):
        e_magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[e_magic_choice]
        magic_dmg = spell.generate_damage()
                  
        pct = self.hp/self.maxhp *  100
        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg


















