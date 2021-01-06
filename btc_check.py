import requests, time

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

url='https://blockchain.info/tobtc'

while True:
	usd = requests.get(url = url, params = 'currency=USD&value=1000')
	eur = requests.get(url = url, params = 'currency=EUR&value=1000')


	tm=time.strftime("%H:%M:%S")
	usd=toFixed(1000/float(usd.text),2) # divide by 1000 because request returns price for 1000 usd
	eur=toFixed(1000/float(eur.text),2) # 2 - means left two digs after commma
	
	print(f'{tm}          1BTC = {usd} $      1BTC = {eur} €')

	time.sleep(10) #10 second cooldown

