from kafka import KafkaConsumer
import csv
import os


def consumer_get():
    consumer = KafkaConsumer('course-topic', bootstrap_servers=f'{os.environ["kafka_ip"]}',
                             key_deserializer=lambda v: bytes.decode(v, encoding='utf-8'),
                             value_deserializer=lambda v: bytes.decode(v, encoding='utf-8'))
    for msg in consumer:
        with open('./data/received.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([msg.topic,
                             msg.partition,
                             msg.key,
                             msg.value
                             ])
        print(f'[<-]received {msg.topic}, {msg.partition}, {msg.key}, {msg.value}')


def main():
    consumer_get()


if __name__ == '__main__':
    main()
