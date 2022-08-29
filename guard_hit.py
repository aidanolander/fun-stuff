from random import randint

num_guards = int(input('Number of guards: '))

hit_counter = 0

for i in range (1, num_guards):
    att_roll = randint(1,20)
    if att_roll >= 7 :
        hit_counter+=1
        

damage_counter = 0
for i in range(1, hit_counter):
    dam_roll = randint(1,10)
    damage_counter+=dam_roll
    

print(damage_counter+hit_counter)
    
        
