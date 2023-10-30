import socket

# Função para se conectar ao servidor e realizar operações


def perform_operation():
    print("Operações disponíveis: add, subtract, multiply, divide")
    operation = input("Escolha uma operação: ").strip().lower()

    if operation not in ('add', 'subtract', 'multiply', 'divide'):
        print("Operação inválida.")
        return

    numbers = input("Digite os números separados por espaço: ")

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        client_socket.send(f"{operation} {numbers}".encode('utf-8'))

        result = client_socket.recv(1024).decode('utf-8')
        print(f"Resultado: {result}")

        client_socket.close()
    except Exception as e:
        print(f"Erro ao conectar ao servidor: {e}")


# Configuração do cliente
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 15000

while True:
    perform_operation()
    another = input("Deseja realizar outra operação? (S/N): ").strip().lower()
    if another != 's':
        break
