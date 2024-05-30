import csv
from riak import RiakClient

# Kết nối đến Riak
client = RiakClient(protocol='http', host='192.168.80.133', http_port=8098)

# Kiểm tra kết nối
if client.ping():
    print("Connected to Riak successfully.")
else:
    print("Failed to connect to Riak.")


choose = input("Nhập bucket muốn tạo: ")
nameFileInput = choose + ".csv"


with open(nameFileInput, 'r') as file:

    reader = csv.DictReader(file)

    listData = [row for row in reader]





name_bucket = client.bucket(choose)



for i in listData:
    id = choose.rstrip('s') + "_id"
    key = name_bucket.new(i[id], data=i)
    key.store()

print("insert " + choose + " success!!!")
