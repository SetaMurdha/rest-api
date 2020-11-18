import requests

server1 = "http://127.0.0.1:5000/"

data = [{"name":"Kubis", "jenis":"Sayuran", "harga":3000},
		{"name":"Singkong", "jenis":"Umbi", "harga":2000},
		{"name":"Cumi-cumi", "jenis":"Seafood", "harga":7000}]

for i in range(len(data)):
	response=requests.put(server1+"food/"+ str(i), data[i])
	print(response.json())

# response = requests.put(server1 + "food/1",{"name":"Enak", "jenis":"daging", "harga":10000})
# print(response.json())

input()

response = requests.get(server1 + "food/2")
print(response.json())

