#Python Ogrenmeye yeni baslayan biri olarak oylesine paylasdim.Yakinda python ile ilgili daha iyi projeler paylasicam
import matplotlib.pyplot as plt

def carpma(n1,n2):
    sonuc = float(n1*n2)
    return f'{n1}*{n2} = {sonuc}'

def bolme(n1,n2):
    sonuc = float(n1/n2)
    return f'{n1}/{n2} = {sonuc}'

def toplama(n1,n2):
    sonuc = float(n1+n2)
    return f'{n1}+{n2} = {sonuc}'

def cikarma(n1,n2):
    sonuc = float(n1-n2)
    return f'{n1}-{n2} = {sonuc}'

def ustBulma(n1,n2):
    sonuc = n1**n2
    return f'{sonuc}'

def kalan(n1,n2):
    sonuc = float(n1%n2)
    return f'{n1}/{n2}{sonuc}'



def fonksiyon(x,y):
    plt.plot(x,y)
    plt.show()

#x,y'e noktalari girin
fonksiyon(x=[-2.0, -0.8, 0.0 , 0.8],y=[8.0, 0.25, 0.0, 0.25])

print(carpma(5.2,3))


#print("""Secim:
#1 >> carpma
#2 >> bolme
#3 >> toplama
#4 >> ust bulma
#5 >> kalani bulma""")

"""
def secim(s=input('Secim >> ')):
    if s == '1':
        print(carpma(3,4))
    elif s == '2':
        print(bolme())
    elif s == '3':
        print(toplama())
    elif s == '4':
        print(ustBulma(3,4))
    elif s == '5':
        print(kalan())
"""


