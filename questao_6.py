import socket
import ssl

def tls_echo_server(host='127.0.0.1', port=8443, certfile='server.crt', keyfile='server.key'):
    # Cria um contexto SSL configurado para o servidor
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)

    # Cria e configura o socket do servidor
    bindsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bindsocket.bind((host, port))
    bindsocket.listen(5)
    print(f"Servidor TLS escutando em {host}:{port}")

    while True:
        # Aceita uma conexão
        newsocket, fromaddr = bindsocket.accept()
        print("Conexão estabelecida com", fromaddr)

        # Envolve o socket aceito com o contexto TLS
        try:
            conn = context.wrap_socket(newsocket, server_side=True)
            data = conn.recv(1024)
            if data:
                mensagem = data.decode('utf-8')
                print("Recebido:", mensagem)
                # Ecoa os dados de volta para o cliente
                conn.send(data)
        except Exception as e:
            print("Erro:", e)
        finally:
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()

if __name__ == '__main__':
    tls_echo_server()
