import pika
conn = pika.BlockingConnection()
ch = conn.channel()
ch.queue_declare(queue="billing-tasks")
ch.basic_consume(queue="billing-tasks", on_message_callback=lambda *a: None, auto_ack=True)
ch.start_consuming()
