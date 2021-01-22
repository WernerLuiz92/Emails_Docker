import redis
import json
import os
from time import sleep
from random import randint

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    r = redis.Redis(host=redis_host, port=6379, db=0)
    print('Aguardando mensagens ...')

    while True:
        sleeptime = randint(15, 45)

        mensagem = json.loads(r.blpop('sender')[1])
        # Simulando o envio de e-mail...
        print('Mandando a mensagem:', mensagem['assunto'], 'em aprox. ', sleeptime, 'segundos.')
        sleep(sleeptime) # Cria um delay para simular o tempo de envio de emails, através de um sleep entre 15 e 45s
        print('Mensagem', mensagem['assunto'], 'enviada!', sleeptime, 'segundos.')