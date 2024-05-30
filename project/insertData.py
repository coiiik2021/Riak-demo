from riak import RiakClient

client = RiakClient(protocol= 'http', host = '192.168.80.132', http_port = 8098)

nameBucket = input("Nhập tên bucket muốn sử dụng: ")

bucket = client.bucket(nameBucket)



ms = input("Nhập mã số : ")

def dataOrder():
    customer_id = input("customer_id: ")
    bucketCustomer = client.bucket("customers")
    if bucketCustomer.get(customer_id).exists:
        order_status = input("order_status: ")
        order_date = input("order_date: ")
        required_date = input("required_date: ")
        shipped_date = input("shipped_date: ")
        new_data = {
            'customer_id': customer_id,
            'order_status': order_status,
            'order_date': order_date,
            'required_date': required_date,
            'shipped_date': shipped_date
        }
        return new_data
    print("Không tồn tại khách hàng đó mời bạn nhập lại!!!\n")
    return None
        
    


def dataCustomer():
    fname = input("first_name: ")
    lname = input("last_name: ")
    phone = input("phone: ")
    email = input("email: ")
    city = input("city: ")
    state = input("state: ")
    new_data = {
	'first_name': fname,
	'last_name': lname,
	'phone': phone,
	'email': email,
	'city': city,
	'state': state
    }
    return new_data
    


if bucket.get(ms).exists:

    print("Dữ liệu với mã số này đã tồn tại trong Riak.")

else:
    new_data = ""
    if nameBucket == "customers":
        new_data = dataCustomer()
    elif nameBucket == "orders":
        new_data = dataOrder()

    if new_data:
        key = bucket.new(ms, data=new_data)
        key.store()
        print("Dữ liệu đã được ghi vào Riak.")
    else:
        print("Không thể ghi dữ liệu vào Riak.")



