from riak import RiakClient
import json

client = RiakClient(protocol= 'http', host = '192.168.80.132', http_port = 8098)

nameBucket = input("Nhập nameBucket: ")

bucket = client.bucket(nameBucket)


for key in bucket.get_keys():

    obj = bucket.get(key)

    data = obj.data

    formatted_data = json.dumps(obj.data, indent=4, ensure_ascii=False)

    print(formatted_data)
