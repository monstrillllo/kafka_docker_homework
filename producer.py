import os
import time
import random
from string import digits, ascii_letters
from kafka import KafkaProducer


def producer_send(value_type: str, value: str):
    producer = KafkaProducer(bootstrap_servers=f'{os.environ["KAFKA_IP"]}', value_serializer=str.encode, key_serializer=str.encode)
    producer.send(topic='course-topic', value=value, key=value_type)
    print(f'[->]send key: {value_type}, value: {value}')


def main():
    while True:
        choice = random.choice(['digits', 'letters'])
        len_ = random.randrange(2, 5)
        if choice == 'digits':
            value = ''
            for _ in range(len_):
                value += random.choice(digits)
        else:
            value = ''
            for _ in range(len_):
                value += random.choice(ascii_letters)
        producer_send(choice, value)
        time.sleep(10)


if __name__ == '__main__':
    main()
