number = [1,5,7,9,6,3,2,1]
letters = ["a","g","s","b","y","a","s"]

val = min[number] # 1
val = max[number] # 9
val = max[letters] # g
val = min[letters] # a

val = number[3:6]
val = number[:3]
val = number[4:]

number[4] = 40

number.append(8)
number.insert(3,78) # 3.index yerine 78 ekler
number.insert(-1,52) # en sona ekler
number.pop() # son elemanı sıler
number.pop(0) # 0.index elemanı sıler
number.pop(-1) # son elemanı sıler
number.pop(3) # 3.index elemanı sıler
number.remove(7) # Listede arar ve siler
number.sort() # kucukten buyuge sıralar
letters.sort() # kucukten buyuge sıralar
number.reverse() # buyukten kucuge sıralar
letters.reverse() # buyukten kucuge sıralar
number.clear() # elemanları sıler



print(val)