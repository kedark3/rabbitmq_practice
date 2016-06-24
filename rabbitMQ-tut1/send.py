
import pika



connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()


channel.queue_declare(queue='helloRabbitMQ')

channel.basic_publish(exchange='',routing_key='helloRabbitMQ',body='Hello World!- from RabbitMQ')
print(" [x] Sent 'Hello World!'")

connection.close()