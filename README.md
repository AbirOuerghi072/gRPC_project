### gRPC_project

#### This is a Multiprotocol platform that can handle different types of protocols as a gateway.


This platform primarily relies on gRPC to ensure secure communication and data transfer between servers and clients. 

It also serves as a Gateway capable of managing various distinct protocols, including:

```
 1.MQTT
 2.ModBus TCP
 3.ModBus RTU 
 4.wIFI
 5.ZigBee
 6.LoRa
 7.BLE


```

In this project, we will develop an IoT platform capable of supporting four protocols, namely:

•MQTT protocol

•Modbus TCP protocol

•Wi-Fi protocol

•BLE protocol


The actors involved in this platform are: a client (Modbus TCP, Wi-Fi, BLE), a server (Modbus
TCP, Wi-Fi, BLE), an MQTT server, and the Mosquitto Broker.

Before starting communication, each client must connect with specific port and IP address.
Then each client will connect with the associated parameters, and the data exchange begins.
The (Modbus TCP, Wi-Fi, BLE) servers will hold the data, making it the starting point of
communication within the platform. The clients (Modbus TCP, Wi-Fi, BLE), connect to the
Modbus TCP server, read the data, and then send it to the MQTT server. The MQTT server,
with its associated parameters, connects to the Mosquitto Broker and retrieves the data,
publishing it to the Mosquitto Broker.
It should be noted that the Mosquitto Broker is the main MQTT server, based on the concept of
publish/subscribe. 
The MQTT server will remain connected and listen to receive any incoming data from the
clients, and then publish it to the broker.

![Screenshot from 2023-09-12 16-05-12](https://github.com/AbirOuerghi072/gRPC_project/assets/144790093/a8214096-dcee-4ba5-89e2-bc27e4b3c878)
