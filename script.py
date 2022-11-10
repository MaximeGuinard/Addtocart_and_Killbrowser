#!/usr/bin/env python
# -*- coding: utf-8 -*-
from helium import * #module hélium
import time #module du temps
import random #module random                            https://python.sdv.univ-paris-diderot.fr/08_modules/
from selenium.webdriver import ChromeOptions #module pour google option et pour le web
options = ChromeOptions()
options.add_argument('--start-maximized')

var1 = random.randint(1,5) # scroll selector           #génére un nombre aléatoire

clicNewIn = random.choice(['', 'Samsung – Galaxy A10e with 32GB','Samsung – Galaxy S10 with 128GB','Google – Pixel 3a – 64GB'])
#Un choix random entre les produits ecrits

def productInteraction():  #fonction interaction avec le produit
	time.sleep(random.uniform(1, 2))  #Pause de 1 a 2s
	if var1 < 5 :  #génére un nombre aléatoire inferieur a 5
		scroll_down(num_pixels=200) #scroll en bas
		time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
		if var4 > 20 :                                        #génére un nombre aléatoire supérieur a 20                                         
			print ('add to cart')  #console add to cart
			clicAddToCart() # ajoute au panier 
	if var3 == 2 :                                          #génére un nombre aléatoire inferieur a 5 ?? ?? 
		time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
		click(clicMenu)    #redirige au menu

def productInteractionRandom(): # Interaction avec un produit random
	time.sleep(random.uniform(1, 2))  #Pause de 1 a 2s
	if var1 < 5 :                  #génére un nombre aléatoire inferieur a 5
		scroll_down(num_pixels=200) #scroll en bas
		time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
		if random.randint(1, 5) == 1 :                ## random entre 1 a 5
			print ('add to cart') #ecrit en console add to cart
			clicAddToCart() #clic sur ajouter un produit au panier
	if var1 < 3 :                                                             #génére un nombre aléatoire inferieur a 3     
		scroll_up(num_pixels=600) #scroll en haut
		time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
	if var3 == 1 :
		hover(S('/html/body/div[3]/div[1]/div[1]/div[1]/div/div/div/nav/a[2]'))      # ??
		time.sleep(random.uniform(1, 2))  #Pause de 1 a 2s
	if var3 == 2 :
		click(clicMenu) #clic sur le menu
	
def clicAddToCart(): #function panier
	hover('Add to cart') #ajoute au panier
	time.sleep(random.uniform(1, 2))  #Pause de 1 a 2s
	click('Add to cart') #click sur ajouter au panier

def goCart():
	time.sleep(random.uniform(1, 2))  #Pause de 1 a 2s
	hover(S('//*[@id="header"]/div[1]/div[2]/div/div/div/div[3]/div/div[2]/a'))

def goCheckout(): # function check    https://gyazo.com/883336b7110badd7ed2e36eab1036300
	scroll_down(num_pixels=200) #scroll en bas
	hover('Proceed to checkout') #Passer à la caisse
	time.sleep(random.uniform(1, 2))  #Pause de 1 a 2s

def checkout(): #function verifie
	scroll_down(num_pixels=200) #scroll en bas
	if var8 < 98 :
		scroll_down(num_pixels=200) #scroll en bas
		time.sleep(random.uniform(1, 2))  #Pause de 1 a 2s
		write("75001" , into="Postcode / ZIP") # remplie le code postal    https://gyazo.com/365838d009f1c57efa446c5b58e34faf
		time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
	if var8 < 98 :
		time.sleep(random.uniform(1, 2))  #Pause de 1 a 2s
		if Text('we ship in 3 days').exists():
			hover('Town / City')
			time.sleep(random.uniform(1, 2))  #Pause de 1 a 2s
		else : # continue
			write("Paris" , into="Town / City")		# remplie l'emplacement town / city    https://gyazo.com/a8d888ff883a7c2027d9d764b7f389c2
		time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s

	if var8 < 98 :
		write("francois.castets@contentsquare.com" , into="Email address")	# ecrit a l'emplacement email adress	https://gyazo.com/8777d12e556d685c1d7fe0c35819015a
		time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
		scroll_down(num_pixels=200) #scroll en bas
	time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
	if Text('Place order').exists():     #Check si ca existe ?         https://gyazo.com/6e1b86c3290fc137dc46e238987d84a4
		hover("Place order")   # Passer la commande
		time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
		click("Place order") # clique sur passer la commande
	else : #ensuite 
		scroll_up(num_pixels=600) #scroll en haut
		hover("Place order") #selectionne place order
		time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
		click("Place order") #clique sur place order
	time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s

start_chrome("http://csretail.pre-sales.fr/" , options=options) #ouvre chrome ici http://csretail.pre-sales.fr/

time.sleep(random.uniform(1, 2))  #Pause de 1 a 2s
click('Ok') # clique sur ok
time.sleep(random.uniform(1, 2))  #Pause de 1 a 2s
scroll_down(num_pixels=200) #scroll en bas

if var9 in range (81, 100) :
	hover(S('//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[4]/div[1]/div[1]/div[4]/div[1]/div[1]'))
	# selectionne le menu déroulant 
	time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
	click(S('//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div[4]/div[1]/div[1]/div[4]/div[1]/div[1]'))
    # clique sur menu déroulant 
time.sleep(random.uniform(3, 4)) # Pause de 3 a 4s

scroll_down(num_pixels=200) # scroll de 200
time.sleep(random.uniform(1, 2)) # Pause de 1 a 2s

#add to cart push product
clicAddToCart() #cliquez sur Ajouter au panier

scroll_up(num_pixels=200) #scroll en haut 
if Text('Computer').exists(): #check si ca existe 
	hover('Computer') #selectionne computer
	time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
	click('Computer') # clique sur computer
	if random.randint(1, 100) < 50 : 
		time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
		hover('Apple – MacBook Air 13.3')
		time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
		click('Apple – MacBook Air 13.3')
		time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
		if random.randint(1, 5) < 4:
			clicAddToCart()                 #Ajoute au panier
		time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
		hover('Computer')             #sellectione computer
		time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
		click('Computer')      #click sur computer

goCart()   #redirige au panier
time.sleep(random.uniform(1, 2)) #Pause de 1 a 2s
if random.randint(1, 5) < 4 :
	goCheckout() #Check si tout va bien

time.sleep(random.uniform(2, 4)) #Pause de 2 a 4s
kill_browser() #Ferme tout les navigateurs