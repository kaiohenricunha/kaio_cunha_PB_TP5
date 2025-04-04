import socket
import ssl

def tls_client(host='127.0.0.1', port=8443):

    # Cria um contexto SSL para o cliente
    context = ssl.create_default_context()
    # Como estamos usando um certificado autoassinado, desabilitamos a verificação do certificado
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # Cria uma conexão TCP e a envolve com SSL/TLS
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print("Cliente: conexão estabelecida")
            mensagem = "Olá, servidor TLS!"
            ssock.send(mensagem.encode('utf-8'))
            data = ssock.recv(1024)
            print("Cliente: recebido:", data.decode('utf-8'))

if __name__ == '__main__':
    tls_client()
