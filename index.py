text = 'Clarusway'
print(text[3])
print(text[4:7])
print(text[6:])
print(text[0:6])
print(text[:6])
print(text[1:8])
print(text[1:8:2])
print(text[1::3])
print(text[::2])
print(text[5:1])
print(text[5:1:-1])
print(text[5:1:-2])
print(text[::-1])
print("python candir"[::-1])

text = 'kayak'
print(text == text[::-1])

yeni_text = 'abcdef'

print(yeni_text == yeni_text[::-1])

text = 'Clarusway'

print(text[-1])
print(text[8])
print(text[8]==text[-1])

animal ='hippopotamus'

print(animal[1:])
print(animal[:6])
print(animal[::2])
print(animal[1:7:2])
print(animal[-3:])
print(animal[::-1])

print(text[-3::-1])

print('a'+'b')

print(text[:4] + text[-3:] )

print(text[:5] + 'k' + text[-3:] )

print(len(text))

print(text[0] + text[len(text)//2] + text[-1])

print(text, 'kelimesinin uzunlugu', len(text), 'harften olusur')

print(*text)

a = 5 
a = a + 1
a += 1
print(a)

# %s string
# %d integer
# %f float

name = 'yasin'

print('Merhaba, %s' % name)

name = 'Ali'
age = 43
meslek = 'Content Creator'


print('Merhaba, ismin %s yasin %d meslegin ise %s' % (name,age,meslek))

name = 'Ali'
age = 43.5
meslek = 'Content Creator'

print('Merhaba, ismin %s yasin %f meslegin ise %s' % (name,age,meslek))

name = 'Ali'
age = 43
meslek = 'Content Creator'

print('Merhaba, ismin {} yasin {} meslegin ise {}'.format(name,age,meslek))

print('Merhaba, ismin {} yasin {} meslegin ise {}'.format(age,meslek,name))

print('Merhaba, ismin {2} yasin {0} meslegin ise {1}'.format(age,meslek,name))

print('Merhaba, ismin {a} yasin {b} meslegin ise {c}'.format(b=age,c=meslek,a=name))


print('Merhaba, ismin {} yasin {b} meslegin ise {c}'.format(name,c=meslek,b =age))

taban = 6
yukseklik = 4
print('burada hesaplama gosterecegim {}'.format(taban*yukseklik/2))


name = 'Ali'
age = 43
meslek = 'Content Creator'
print(f'merhaba benim adim {name} yasim {age} meslegim {meslek}')


print(f"burada hesaplama yapiyor {taban*yukseklik/2}")

name = "MARIAM"

print(f"My name is {name.capitalize()}")

print(f"saga hizalama {name:>20}")
print(f"saga hizalama {name:<20}")
print(f"saga hizalama {name:^20}")
print(f"saga hizalama {name:*^20}")

