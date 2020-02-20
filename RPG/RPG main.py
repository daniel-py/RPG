# from Classes.Game import person, bcolours
from Classes.Game import person, bcolours
from Classes.magic import Spell
from Classes.inventory import Item
import random

# Create black magic
fire= Spell("fire", 25, 600, "black")
thunder= Spell("thunder", 25, 600, "black")
blizzard= Spell("blizzard", 25, 600, "black")
meteor= Spell("meteor", 40, 1200, "black")
quake= Spell("quake", 14, 140, "black")


# Create white magic
cure = Spell("cure", 22, 620, "white")
cura = Spell("cura", 32, 1500, "white")
curaga = Spell("Curaga", 50, 6000, "white")


# Create new items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
hielixir = Item("MegaElixir", "elixir", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [fire, meteor, curaga]
player_items = [{"item": potion, "quantity" : 15}, {"item" : hipotion, "quantity" : 5}, {"item" : superpotion, "quantity" : 5}, 
                {"item" : elixir, "quantity" : 5}, {"item" : hielixir, "quantity" : 2}, {"item" : grenade, "quantity" : 5}]

# Instantiate people
player1= person("Valos:", 3260, 132, 300, 34, player_spells, player_items)
player2= person("Nick: ", 4160, 188, 311, 34, player_spells, player_items)
player3= person("Robot:", 3089, 174, 288, 34, player_spells, player_items)


enemy1 = person("Imp  ", 1250, 130, 560, 325, enemy_spells, [])
enemy2 = person("Magus", 18200, 701, 525, 25, enemy_spells, [])
enemy3 = person("Imp  ", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i= 0

print(bcolours.FAIL + bcolours.BOLD + "AN ENEMY ATTACKS!" + bcolours.ENDC)

while running:
    print("=========================================")
    
    print("\n\n")
    print("NAME                          HP                                 MP")

    for player in players:
        player.get_stats()
    print("\n")
    
    for enemy in enemies:
        enemy.get_enemy_stats()
    
    for player in players:
        player.choose_action()
        Choice = input("    Choose action: ")
        index = int(Choice) - 1

        if index== 0:
            dmg= player.generate_damage()
            enemy = player.choose_target(enemies)
            
            enemies[enemy].take_damage(dmg)
            print(f"You attacked {enemies[enemy].name.replace(' ', '')} for {dmg} points of damage.\nEnemy HP: {enemies[enemy].get_hp()}")

            if enemies[enemy].get_hp() == 0:
                print(f"{enemies[enemy].name} has died")
                del enemies[enemy]
                
        elif index == 1:
            player.choose_magic()
            magic_choice= int(input("    Choose magic ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(f"{bcolours.FAIL} \nNot enough MP {bcolours.ENDC}")
                continue 

            player.reduce_mp(spell.cost)


            if spell.type == "white":
                player.heal(magic_dmg)
                print(f"{bcolours.OKBLUE}\n{spell.name} heals for {str(magic_dmg)} HP {bcolours.ENDC}")

            elif spell.type == "black":
                enemy = player.choose_target(enemies)
            
                enemies[enemy].take_damage(magic_dmg)
                print(f"{bcolours.OKBLUE} \n{spell.name} deals {str(magic_dmg)} points of damage to {enemies[enemy].name.replace(' ', '')}.{bcolours.ENDC}")
                
                if enemies[enemy].get_hp() == 0:
                    print(f"{enemies[enemy].name.replace(' ', '')} has died")
                    del enemies[enemy]

        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] <= 0:
                print(f"{bcolours.FAIL} {item.name}none left... {bcolours.ENDC}")
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(f"{bcolours.OKGREEN}\n{item.name} heals for {item.prop} HP {bcolours.ENDC}")

            elif item.type == "elixir":
                
                if item.name == "MegaElixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(f"{bcolours.OKGREEN} \n{item.name} fully restores HP/MP{bcolours.ENDC}")

            elif item.type == "attack":
                enemy = player.choose_target(enemies)
            
                enemies[enemy].take_damage(item.prop)
                print(f"{bcolours.FAIL}\n{item.name} deals {item.prop} points of damage to {enemies[enemy].name.replace(' ', '')} {bcolours.ENDC}")

                if enemies[enemy].get_hp() == 0:
                    print(f"{enemies[enemy].name.replace(' ', '')} has died")
                    del enemies[enemy]
        
    

            
    if len(enemies) == 0:
        print(f"{bcolours.OKGREEN}You win!")
        running = False
            
    
        
    print("\n")
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
                          
        if enemy_choice == 0:
            if len(players) == 3:
                target = random.randrange(0, 3)
            elif len(players) == 2:
                target = random.randrange(0, 2)
            else:
                target = random.randrange(0, 1)
                          
            e_dmg= enemy.generate_damage()
            players[target].take_damage(e_dmg)
            print(f"{enemy.name.replace(' ', '')} attacks {players[target].name.replace(' ', '')} for {e_dmg} points.")
                  
            if players[target].get_hp() == 0:
                print(f"{players[target].name.replace(' ', '')} has died")
                del players[target]
                      
                      
        elif enemy_choice == 1:
                      
            if len(players) == 3:
                target = random.randrange(0, 3)
            elif len(players) == 2:
                target = random.randrange(0, 2)
            else:
                target = random.randrange(0, 1)
                      
            pct = (enemy.get_hp()/enemy.get_max_hp()) *  100
            
            if enemy.get_mp() < spell.cost or spell.type == "white" and pct > 50:
                spell = enemy.choose_enemy_spell
                magic = enemy.choose_enemy_spell
            else:
                spell, magic_dmg = enemy.choose_enemy_spell()
            
            enemy.reduce_mp(spell.cost)
                  
            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(f"{bcolours.OKBLUE}{spell.name} heals {enemy.name.replace(' ', '')} for {str(magic_dmg)} HP {bcolours.ENDC}")

            elif spell.type == "black":
            
                players[target].take_damage(magic_dmg)
                print(f"{bcolours.OKBLUE}{enemy.name.replace(' ', '')}\'s {spell.name} deals {str(magic_dmg)} points of damage to {players[target].name.replace(' ', '')}.{bcolours.ENDC}")
                
                if players[target].get_hp() == 0:
                    print(f"{players[target].name.replace(' ', '')} has died")
                    del players[target]
                          
        if len(players) == 0:
            print(f"{bcolours.FAIL}Your enemies have defeated you!")
            running = False   
                  
            
                  

    