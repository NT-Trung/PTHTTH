import socket

def main():
    server_ip = "127.0.0.1"  # Địa chỉ IP của máy chạy server
    server_port = 12345  # Port của server

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    while True:
        print("Danh sách dịch vụ:")
        print("1. Đảo ngược chuỗi và in hoa ký tự đầu của mỗi từ")
        print("2. Tính tổng chuỗi các số nguyên")
        print("3. Thoát")

        choice = input("Chọn dịch vụ (1/2/3): ")

        if choice == '1':
            client.send(choice.encode('utf-8'))
            input_string = input("Nhập chuỗi: ")
            client.send(input_string.encode('utf-8'))
            result = client.recv(1024).decode('utf-8')
            print(f"Kết quả: {result}")
        elif choice == '2':
            client.send(choice.encode('utf-8'))
            input_string = input("Nhập chuỗi các số nguyên (cách nhau bởi khoảng trắng): ")
            client.send(input_string.encode('utf-8'))
            result = client.recv(1024).decode('utf-8')
            print(f"Tổng các số nguyên: {result}")
        elif choice == '3':
            print("Kết thúc kết nối.")
            client.close()
            break
        else:
            print("Dịch vụ không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
