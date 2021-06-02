import struct
import socket
import random
from st2common.runners.base_action import Action

class IpRandomAction(Action):
    def run(self):
        hosts = "192.168.89.50:9092"
        client = KafkaClient(hosts=hosts)
        key = "log.ts"
        key = bytes(key, encoding='utf8')
        topic = client.topics[key]
        consumer = topic.get_simple_consumer(auto_commit_enable=True)
        # consumer = topic.get_simple_consumer(consumer_group='test', auto_commit_enable=True, consumer_id='test')
        index = 0
        #start = time.time()
        for message in consumer:
            if message is not None:
                #end = time.time()
                print(message.value)
                # print(end - start)
                index += 1
                print('--------poll index is %s----------' % index)
        return index