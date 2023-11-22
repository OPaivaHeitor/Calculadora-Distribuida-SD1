import socket

# Funções para realizar operações aritméticas


def add(numbers):
    return sum(numbers)


def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Erro: Divisão por zero"
        result /= num
    return result


# Configuração do servidor
HOST = '127.0.0.1'
PORT = 15000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(
    f"Servidor da calculadora distribuída aguardando conexões em {HOST}:{PORT}...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Conexão estabelecida com {client_address}")

    data = client_socket.recv(1024).decode('utf-8')

    if not data:
        break

    # Analisar a entrada do cliente
    parts = data.split()
    operation = parts[0].lower()
    numbers = [float(x) for x in parts[1:]]

    # Realizar a operação correspondente
    if operation == 'add':
        result = add(numbers)
    elif operation == 'subtract':
        result = subtract(numbers)
    elif operation == 'multiply':
        result = multiply(numbers)
    elif operation == 'divide':
        result = divide(numbers)
    else:
        result = "Operação inválida"

    # Enviar o resultado de volta ao cliente
    if(result):
        print("Resultado: ", result)
    client_socket.send(str(result).encode('utf-8'))
    client_socket.close()

server_socket.close()
