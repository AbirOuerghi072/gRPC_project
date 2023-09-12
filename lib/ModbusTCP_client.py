# Modbus library
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import grpc

# MQTT gRPC library
import mqtt_pb2
import mqtt_pb2_grpc

# Tools
#from utils import log_info
import logging 
logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(message)s')
# Default modbus server
MODBUS_SERVER_HOST = "192.168.62.226"
MODBUS_SERVER_PORT = 5020



MODBUS_CLIENT = ModbusClient(MODBUS_SERVER_HOST, port=MODBUS_SERVER_PORT)
MODBUS_CLIENT.connect()



UNIT = 0x1

def run():
    """Main modbus client method"""
    with grpc.insecure_channel('0.0.0.0:50051') as mqtt_channel:
        mqtt_stub = mqtt_pb2_grpc.MQTTManagerStub(mqtt_channel)
        modbus_data = MODBUS_CLIENT.read_holding_registers(0, 1, unit=UNIT)
        for mdata in modbus_data.registers:
            Acknowledgment= mqtt_stub.PublishMessages(mqtt_pb2.ComingData(Payload=str(mdata), Topic="modbustcp"))
            print(Acknowledgment)



#logging.info('Configuration Parameters are {}:{}'.format(server_host1, server_port1))

if __name__ == '__main__':
    try:
       run()
    except KeyboardInterrupt:
        logging.info("[ModbusClient] Shutting down ..")
