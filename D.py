import etcd3
import time
import random

def esperar_chave(client, chave):
    """Aguarda uma chave aparecer no etcd.
    Se já existir quando D iniciar, retorna imediatamente sem watch."""
    valor, _ = client.get(chave)
    if valor is not None:
        return

    # watch_once bloqueia até receber exatamente um evento na chave
    client.watch_once(chave)

def main():
    client = etcd3.client(host='localhost', port=2379)

    print("Aguardando")

    esperar_chave(client, 'done/B')
    esperar_chave(client, 'done/C')

    limite = random.randint(10, 20)

    for i in range(1, limite + 1):
        print(i)
        time.sleep(1)

    print("Fim")

if __name__ == '__main__':
    main()
