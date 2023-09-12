#Importing the gRPC library
import grpc
import mqtt_pb2
import mqtt_pb2_grpc

#Importing the MQTT library 
import paho.mqtt.client as mqtt

from concurrent import futures
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(message)s')

#A Variable that contains the return code of the connection
#status
connack_rc=-1


# The Callback function that determines if the client connected or not 
# to the Mosquitto Broker and returns the Return Code(rc)
def onconnect(client,userdata,flag,rc):
    global connack_rc
    if  rc==0:
        logging.info('Client Connnected OK ')
        connack_rc=rc
        
    elif rc==1:
        logging.info('Connection Refused :incorrect protocol version ')
        connack_rc=rc
    elif rc==2:
        logging.info('Connection refused:bad client id')
        connack_rc=rc
    elif rc==3:
        logging.info('Connection refused:Server unvailable')
        connack_rc=rc
    elif rc==4:
        logging.info('Connection refused:bad username or password')
        connack_rc=rc
    else :
        logging.info('Connection refused:not authorized')
        connack_rc=rc
    return(rc)


#This Side implements the MQTT Server as a Server for
## the Clients (ModBusClient_wifi)
class MQTTManagerServicer(mqtt_pb2_grpc.MQTTManagerServicer):
    def PublishMessages(self,request,context):
        topic1=request.Topic
        payload1=request.Payload
        qos1=request.Qos
       
        if connack_rc==0:

            Mqttclient.publish(topic=topic1,payload=payload1)
            status=Mqttclient.publish(topic=topic1,payload=payload1)
            if status.rc==0:
                logging.info("Publish Success")
                ACKK=mqtt_pb2.Publish_Success     
                
            else:
                logging.info("Publish Failed")
                ACKK=mqtt_pb2.PublishFailed
                
               
        elif connack_rc==1:
            logging.info('Connection Refused :incorrect protocol version ')
            ACKK=mqtt_pb2.Incorrect_Proto_Version

        elif connack_rc==2:
            logging.info('Connection refused:bad client id')
            ACKK=mqtt_pb2.Bad_Client_ID

        elif connack_rc==3:
            logging.info('Connection refused:Server unvailable')
            ACKK=mqtt_pb2.Server_Unvailable

        elif connack_rc==4:
            logging.info('Connection refused:bad username or password')
            ACKK=mqtt_pb2.Bad_User_Pw

        else :
            logging.info('Connection refused:not authorized')
            ACKK=mqtt_pb2.Not_AUTH
            
            
              
        logging.info("The server is still waiting for Upcoming Data ")
        return mqtt_pb2.ReturnType(Acknowledgment=ACKK)
   
 
# Main Function of the MQTT Server
def main_Mqtt():

    server =grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    mqtt_pb2_grpc.add_MQTTManagerServicer_to_server(MQTTManagerServicer(),server)
    logging.info("The server is Starting !")
    logging.info('Connecting to the Mosquitto Broker .....')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

broker ="localhost"
port =1883

#Creating the MqttClient and starting the process of connection   

Mqttclient= mqtt.Client("grpc",clean_session=False)
Mqttclient.on_connect=onconnect
Mqttclient.connect(broker,port)
Mqttclient.loop_start()




#Calling the Mqtt Server   


main_Mqtt()
   
    
