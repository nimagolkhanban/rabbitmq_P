import pika


def on_message_received(ch, method, properties, body):
    print(f'received new message  {body}')


connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

chanel1 = connection.channel()

chanel1.queue_declare(queue='letterbox')

chanel1.basic_consume(queue='letterbox', auto_ack=True,on_message_callback=on_message_received)

chanel1.start_consuming()

