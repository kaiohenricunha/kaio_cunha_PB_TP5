import socket
import ssl

# Salva as implementações originais de send() e recv()
original_send = ssl.SSLSocket.send
original_recv = ssl.SSLSocket.recv

def patched_send(self, data, *args, **kwargs):
    """
    Método substituto para send que intercepta e loga os dados enviados.
    """
    print("Interceptado (envio):", data)
    return original_send(self, data, *args, **kwargs)

def patched_recv(self, bufsize, *args, **kwargs):
    """
    Método substituto para recv que intercepta e loga os dados recebidos.
    """
    result = original_recv(self, bufsize, *args, **kwargs)
    print("Interceptado (recebido):", result)
    return result

# Monkey patch: substitui os métodos send e recv da classe SSLSocket
ssl.SSLSocket.send = patched_send
ssl.SSLSocket.recv = patched_recv

def tls_client_with_logging(host='127.0.0.1', port=8443):
    """
    Cria um cliente TLS que se conecta a um servidor, envia uma mensagem e recebe a resposta,
    exibindo logs interceptando os dados enviados e recebidos.
    """
    # Cria um contexto TLS para o cliente
    context = ssl.create_default_context()
    # Desabilita a verificação do certificado (útil para certificados autoassinados)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # Estabelece a conexão TCP e envolve com TLS
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print("Cliente: conexão estabelecida")
            mensagem = "Mensagem segura com logging de pacotes"
            ssock.send(mensagem.encode('utf-8'))
            data = ssock.recv(1024)
            print("Cliente: recebido:", data.decode('utf-8'))

if __name__ == '__main__':
    tls_client_with_logging()
