

import yaml

from confluent_kafka import Consumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer
from confluent_kafka.serialization import SerializationContext, MessageField


with open("conf.yaml", "conf") as file:
    config = yaml.safe_load(file)

# Extract configurations
schema_registry_conf = config["schema_registry_conf"]
consumer_conf = config["consumer_conf"]

# Create Schema Registry client and Avro deserializer
schema_registry_client = SchemaRegistryClient(schema_registry_conf)
avro_deserializer = AvroDeserializer(schema_registry_client)

# Kafka Consumer config


# Create Kafka consumer
consumer = Consumer(consumer_conf)
consumer.subscribe(['JP.UAT.ODS.OMNE.LIFEJ.dbo.TAXFPF'])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue
        # Deserialize Avro message
        value = avro_deserializer(msg.value(), SerializationContext(msg.topic(),MessageField.VALUE))
        effdate = value['data']['EFFDATE']

        print(f"Received message: {value['data']['EFFDATE']} , {value['data']['CHDRNUM']}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
