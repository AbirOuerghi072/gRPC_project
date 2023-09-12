import socket
import grpc

# MQTT gRPC library
import mqtt_pb2
import mqtt_pb2_grpc

# Tools
#from utils import log_info
import logging 
logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(message)s')
# Default wifi server
esp32_ip = "192.168.62.61"  # Replace with the ESP32's IP address
port = 12345  # Use the same port as in the ESP32 server code


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((esp32_ip, port))
    data = client_socket.recv(1024)  # Receive data (adjust buffer size as needed)
    print(f"Received data from ESP32: {data.decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")
finally:
    client_socket.close()

def run():
    """Main modbus client method"""
    with grpc.insecure_channel('0.0.0.0:50051') as mqtt_channel:
        mqtt_stub = mqtt_pb2_grpc.MQTTManagerStub(mqtt_channel)
        Acknowledgment= mqtt_stub.PublishMessages(mqtt_pb2.ComingData(Payload=str(data), Topic="Wi-Fi"))
        print(Acknowledgment)



#logging.info('Configuration Parameters are {}:{}'.format(server_host1, server_port1))

if __name__ == '__main__':
    try:
       run()
    except KeyboardInterrupt:
        logging.info("[Wi-FiClient] Shutting down ..")
