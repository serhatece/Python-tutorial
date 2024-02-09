import re

result = dir(re)

print(result)



#! re module

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

#? re.findall()
sonuc = re.findall("Python",str)
kacTane = len(sonuc)
print(kacTane)
print(sonuc)


#? re.split()
a = re.split(" ",str) # boslukları bolup dizi yapar
print(a) 


#? re.sub()
b = re.sub(" ","-",str) # Boşluk karakteri yerine '-' işareti koyar
print(b)


#? re.search()
c = re.search("Python",str) # index sırasını bulmaya yarar
d = c.span() # (0,6) index sırasını verır
print(c)
print(d)




#! regular expression


"""

    [] - Köşeli parantezler arasina yazilan bütün karakterler
         aranir.

         [abc] => a      : 1 match
                  ac     : 2 match 
                  Python : No matches

         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239]   

         [^abc] => abc dişindaki karakterler.
         [^0-9] => rakam olmayan karakterler.

"""
e = re.findall("[abc]",str)
e = re.findall("[sat]",str)
e = re.findall("[a-e]",str)
e = re.findall("[a-z]",str)
e = re.findall("[0-5]",str)
e = re.findall("[^abc]",str)
e = re.findall("[^0-9]",str)

print(e)



"""
    . - Her hangi bir tek karakteri belirtir.

        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches
"""
o = re.findall("...",str)
o = re.findall("py..on",str)

print(o)



"""
    ^ - Belirtilen string karakterlerle başliyor mu ?

    ^a => a:    1 match
          abc:  1 match
          bac:  No match

"""
l = re.findall("^P",str)
print(l)



"""
    $ - Belirtilen karakterle bitiyor mu ?

    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 

"""
ö = re.findall("t$",str)
ö = re.findall("saat$",str)
print(ö)



"""
     * - Bir karakterin sifir ya da daha fazla sayida olmasini 
         kontrol eder.

         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nin arkasina n gelmiyor.) 
"""
v = re.findall("sa*t",str)
print(v)



"""
     + - Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""
i = re.findall("sa+t",str)
print(i)



"""
    {} - Karakter sayisini kontrol eder.

        al{2}   => a karakterinin arkasina l karakteri 2 kez tekrarlamali.
        al{2,3} => a karakterinin arkasina l karakteri en az 2 en fazla 3 kez tekrarlamali.
        [0-9]{2,4} => en az 2 en çok 4 basamakli sayilar.
"""
u = re.findall("a{2}", str)
ü = re.findall("[0-9]{2}", str)
print(u)
print(ü)



"""
    () - gruplamak için kullanilir.

         (a|b|c)xz => a,b,c karakterlerinin arkasina xz gelmelidir.
"""



"""
    \ - Özel karakterleri aramamizi sağlar.
        \$a => $ karakterinin arkasina a karakterinin arar. Yani
               $ regular exp. engine tarafindan yorumlanmaz.

    \A - Belirtilen karakter string in başinda mi ?
         \Athe => the string in başindami

        result = re.findall("\APython", str)
        result = re.findall("saat\Z", str)

    \Z - Belirtilen karakter string in sonunda mi ?
         the\Z => the string in sonunda mi

    \b - Belirtilen karakter kelimenin in başinda ya da sonunda mi ?
         \bthe => the kelimenin in başinda mi?
         the\b => the kelimenin in sonunda mi?

    \B - Belirtilen karakter kelimenin in başinda ya da sonunda değil mi ?
         \Bthe => the kelimenin in başinda değil mi?
         the\B => the kelimenin in sonunda değil mi?
    
    \d - [0-9] ile ayni anlama gelir yani rakamlari arar.
         \d => 12abc34

    \D - [^0-9] ile ayni anlama gelir yani rakam olmayanlari arar.
         \D => 1ab44_50

    \s - Boşluk karakterlerini arar.  
    \S - Boşluk karakterleri dişindakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi
    
"""