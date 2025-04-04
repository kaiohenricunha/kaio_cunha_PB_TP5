import dns.resolver

def coletar_registros_dns(dominio):
    """
    Consulta e exibe os registros DNS do domínio especificado, incluindo os registros A, MX e NS.
    
    Parâmetros:
    - dominio: string contendo o domínio a ser consultado (ex.: "example.com").
    """
    try:
        # Consulta registros A
        respostas_a = dns.resolver.resolve(dominio, 'A')
        print("Registros A:")
        for resposta in respostas_a:
            print(resposta.to_text())
    except Exception as e:
        print("Erro ao consultar registros A:", e)
    
    try:
        # Consulta registros MX
        respostas_mx = dns.resolver.resolve(dominio, 'MX')
        print("\nRegistros MX:")
        for resposta in respostas_mx:
            # Cada resposta MX possui um valor de preferência e o servidor de e-mail (exchange)
            print(f"{resposta.preference} {resposta.exchange.to_text()}")
    except Exception as e:
        print("Erro ao consultar registros MX:", e)
    
    try:
        # Consulta registros NS
        respostas_ns = dns.resolver.resolve(dominio, 'NS')
        print("\nRegistros NS:")
        for resposta in respostas_ns:
            print(resposta.to_text())
    except Exception as e:
        print("Erro ao consultar registros NS:", e)

if __name__ == '__main__':
    dominio = "example.com"
    print("Coletando registros DNS para o domínio:", dominio)
    coletar_registros_dns(dominio)
