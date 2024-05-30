from riak import RiakClient


client = RiakClient(protocol= 'http', host = '192.168.80.132', http_port = 8098)

nameBucket = input("Nhập tên bucket: ")

bucket = client.bucket(nameBucket)

obj_id = input("Nhập mã số cần cập nhật: ")

key = bucket.get(obj_id)



if key.exists:
    obj = key.data

    print("Thông tin hiện tại của obj:")
    print(obj)

    if nameBucket == "customers":
        first_name = input("Nhập tên mới của khách hàng: ")
        last_name = input("Nhập họ mới của khách hàng: ")
        phone = input("Nhập số điện thoại mới của khách hàng: ")  
        email = input("Nhập email mới của khách hàng: ")
        city = input("Nhập thành phố mới của khách hàng: ")
        state = input("Nhập bang mới của khách hàng: ")


        obj['first_name'] = first_name
        obj['last_name'] = last_name
        obj['phone'] = phone
        obj['email'] = email
        obj['city'] = city
        obj['state'] = state
    elif nameBucket == "orders":
        while True:
            customer_id = input("customer_id: ")
            bucketCustomer = client.bucket("customers")
            customer = bucketCustomer.get(customer_id)
            if customer.exists:
                order_status = input("order_status: ")
                order_date = input("order_date: ")
                required_date = input("required_date: ")
                shipped_date = input("shipped_date: ")
            
                obj['customer_id'] = customer_id
                obj['order_status'] = order_status
                obj['order_date'] = order_date
                obj['required_date'] = required_date
                obj['shipped_date'] = shipped_date
                break;
            else:
                print("customer_id không tồn tại mời nhập lại!!!\n")
            
            
            


    key.data = obj
    key.store()

    print("Thông tin của customer đã được cập nhật thành công.")
else:
    print("Không tìm thấy dữ liệu cho mã số ", obj_id, "trong Riak.")
