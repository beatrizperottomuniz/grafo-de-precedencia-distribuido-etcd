import etcd3
import time
import random

def main():
    client = etcd3.client(host='localhost', port=2379)

    # Lease de 60 segundos: as chaves expiram automaticamente
    # assim não precisamos limpar manualmente entre execuções
    lease = client.lease(60)

    limite = random.randint(10, 20)

    for i in range(1, limite + 1):
        print(i)
        time.sleep(1)

    print("Liberando B e C")
    client.put('ready/B', '1', lease=lease)
    client.put('ready/C', '1', lease=lease)
    print("Fim")

if __name__ == '__main__':
    main()
