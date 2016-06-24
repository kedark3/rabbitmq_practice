import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

channel.basic_publish(exchange='logs',routing_key='',body=message)#routing key is ignored even if we specify one
#since we have a fanout exchange


print(" [x] Sent %r" % message)
connection.close()