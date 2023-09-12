import socket
import grpc
import pygatt

# MQTT gRPC library
import mqtt_pb2
import mqtt_pb2_grpc

# Tools
#from utils import log_info
import logging 
logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(message)s')
# Replace with the MAC address of your ESP32 LoRa module
device_mac = "78:21:84:92:E2:AE"

# Replace with the generated UUIDs
service_uuid = "B3888744-F2fB-460F-824A-1756AE5FE75A"
characteristic_uuid = "DD93A5F9-11E8-43A0-A1EB-9DA17D7B16B4"

adapter = pygatt.GATTToolBackend()

try:
    adapter.start()

    device = adapter.connect(device_mac)

    while True:
        # Read data from the ESP32
        data_received = device.char_read(characteristic_uuid).decode('utf-8')
        print("Received from ESP32:", data_received)
        break
finally:
    adapter.stop()

def run():
    """Main modbus client method"""
    with grpc.insecure_channel('0.0.0.0:50051') as mqtt_channel:
        mqtt_stub = mqtt_pb2_grpc.MQTTManagerStub(mqtt_channel)
        Acknowledgment= mqtt_stub.PublishMessages(mqtt_pb2.ComingData(Payload=str(data_received), Topic="BLE"))
        print(Acknowledgment)



#logging.info('Configuration Parameters are {}:{}'.format(server_host1, server_port1))

if __name__ == '__main__':
    try:
       run()
    except KeyboardInterrupt:
        logging.info("[BLE_Client] Shutting down ..")













