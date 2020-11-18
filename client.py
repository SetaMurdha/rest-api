import requests

server1 = "http://127.0.0.1:5000/"

#tampilkan data server 1
a = int(input("Data yang dikeluarkan"))
for i in range(a):
	response = requests.get(server1 + "food/"+str(i))
	print(response.json())

#tambah data server 1

input()

response = requests.delete(server1 + "food/"+str(3))

print(response.json())
