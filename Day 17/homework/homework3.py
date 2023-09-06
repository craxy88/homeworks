# #ვისი სახელიც "ი"-ზე მთავრდება, დაუპრინტეთ გვერდით "cool"

import random

squad=["dato mgeladze","vano motiashvili","davit janashia","aleqsandre katsarava","lasha wamalaidze","ilia wiklauri","nini nozadze","nika chochia","gabriel gogadze","sandro bochorishvili","dato jachvadze","giorgi gelashvili","muhammedali mamedov","sandro oqropiridze","erekle gochitashvili"]

randomizer1 = random.choice(squad)
randomizer2 = random.choice(squad)
randomizer3 = random.choice(squad)
        
if randomizer1[-1] == "i":
    print(randomizer1 , "cool")

if randomizer2[-1] == "i":
    print(randomizer2 , "cool")

if randomizer3[-1] == "i":
    print(randomizer3 , "cool")

if randomizer1[-1] != "i":
    print(randomizer1)

if randomizer2[-1] != "i":
    print(randomizer2)

if randomizer3[-1] != "i":
    print(randomizer3)


    
