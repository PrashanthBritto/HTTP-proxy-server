import requests
import sys

urls = 0

url_list = []
while urls!=4:
	urls +=1
	url = input("Enter the url of the site "+str(urls)+":"+"\n")
	url_list.append(url)


proxies = {
	"http": "http://127.0.0.1:8080", 
}

connection_number = 0
try:
	for url in url_list:
		connection_number +=1
		response = requests.get(url, proxies=proxies)
		print("Fetching the content for ......"+str(connection_number))
except KeyboardInterrupt:
	sys.exit(0)
finally:
	print("Successfully fetched the content")