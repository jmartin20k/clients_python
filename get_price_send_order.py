#Import the libraries 
from bs4 import BeautifulSoup 
import requests 
import time
import exbitron

client = exbitron.Client()

client = exbitron.Client(
    access_key="b92bd389a14c07ad",
    secret_key="64aa928c952dbf2c05f03618b6007f31"
)

#Create a function to get the price of a cryptocurrency
def get_crypto_price(coin):
#Get the URL
    url = "https://www.google.com/search?q="+coin+"+price+dolar"
    
    #Make a request to the website
    HTML = requests.get(url) 
  
    #Parse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser') 
  
    #Find the current price 
    #text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
#Return the text 
    return text
    
    
#Create a main function to consistently show the price of the cryptocurrency
def main():
  #Set the last price to negative one
  last_price = -1
  #Create an infinite loop to continuously show the price
  while True:
  #Choose the cryptocurrency that you want to get the price of (e.g. bitcoin, litecoin)
    crypto = 'bitcoin' 
  #Get the price of the crypto currency
    price = get_crypto_price(crypto)
    price2 = price.split(" ", 1)
  #print(price)
  #Check if  the price changed
  #if price2 != last_price:
  #print(crypto+' price: ', price2[0]) #Print the price
    params = {"ethusd", "buy", 0.001, price2[0]}
    f = open("price_now.txt", "w")
    f.write(price2[0])
    f.close()
  #print(price2[0])
    print(client.postorder("/api/v2/peatio/market/orders/"), params)
  #print(client.postorder("/api/v2/peatio/market/orders/"), params)
  #print(client.postorder("/api/v2/peatio/market/orders/"), price2)
    last_price = price2 #Update the last price
    time.sleep(10) #Suspend execution for 3 seconds.
    
main()
