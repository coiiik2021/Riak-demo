from riak import RiakClient
import json

client = RiakClient(protocol= 'http', host = '192.168.80.133', http_port = 8098)

nameBucket = input("Nhập bucket cần muốn kiếm: ")


bucket = client.bucket(nameBucket)


ms = input("Nhập mã số cần tìm kiếm: ")


obj = bucket.get(ms)


if obj.exists:
    formatted_data = json.dumps(obj.data, indent=4, ensure_ascii=False)
    print("Dữ liệu cho mã số datalà:\n", formatted_data)
else:
    print("Không tìm thấy dữ liệu cho mã số " , ms)
