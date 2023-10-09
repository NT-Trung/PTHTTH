import socket
import threading

def Daonguocchuoi(input_string):
    words = input_string.split()
    reversed_words = [word[::-1].capitalize() for word in words]
    result = ' '.join(reversed_words)
    return result

def Tongsonguyen(input_string):
    numbers = [int(num) for num in input_string.split() if num.isdigit()]
    return sum(numbers)

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8').strip()
    if request == '1':
        client_socket.send("Nhập chuỗi: ".encode('utf-8'))
        input_string = client_socket.recv(1024).decode('utf-8').strip()
        result = Daonguocchuoi(input_string)
        client_socket.send(result.encode('utf-8'))
    elif request == '2':
        client_socket.send("Nhập chuỗi các số nguyên (cách nhau bởi khoảng trắng): ".encode('utf-8'))
        input_string = client_socket.recv(1024).decode('utf-8').strip()
        result = str(Tongsonguyen(input_string))
        client_socket.send(result.encode('utf-8'))
    else:
        client_socket.send("Dịch vụ không hợp lệ. Kết thúc kết nối.".encode('utf-8'))
    
    client_socket.close()

def main():
    server_ip = "127.0.0.1"  # Địa chỉ IP của máy chạy server
    server_port = 12345  # Port để lắng nghe kết nối

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)

    print(f"Server đang lắng nghe trên {server_ip}:{server_port}...")

    while True:
        client_socket, client_addr = server.accept()
        print(f"Kết nối mới từ {client_addr[0]}:{client_addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
