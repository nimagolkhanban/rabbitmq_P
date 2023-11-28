import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

chanel1 = connection.channel()

chanel1.queue_declare(queue='letterbox')

message = "hello this is my first message"

chanel1.basic_publish(exchange='', routing_key='letterbox',body=message)
print(f'sent message : {message}')

connection.close()