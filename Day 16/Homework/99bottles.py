cifri1 = 99
cifri2 = 98
text = "bottles of beer on the wall, bottles of beer. Take one down and pass it around, bottles of beer on the wall."

while cifri1 > 1:
    
    print(cifri1,"bottles of beer on the wall,",cifri1 , "bottles of beer. Take one down and pass it around,",cifri2, "bottles of beer on the wall.")
    cifri1-=1
    cifri2-=1
    
    if cifri1 == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.Take one down and pass it around, no more bottles of beer on the wall.")

print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")