import subprocess
import sys

def scan_ports(host):
    """
    Realiza uma varredura de portas utilizando o Nmap para o host especificado,
    identificando as portas abertas e os serviços com suas versões.

    Parâmetros:
    - host: string representando o endereço IP ou hostname alvo.
    """
    # Monta o comando Nmap com a opção -sV para detecção de versões dos serviços
    comando = ['nmap', '-sV', host]
    
    try:
        # Executa o comando e captura a saída (stdout) em formato de texto
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        print("Resultado da varredura:")
        print(resultado.stdout)
    except subprocess.CalledProcessError as erro:
        print("Erro ao executar o Nmap:")
        print(erro)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python group5_exercicio2.py <host>")
        sys.exit(1)
    
    host_alvo = sys.argv[1]
    scan_ports(host_alvo)
