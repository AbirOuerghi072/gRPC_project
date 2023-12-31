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

![Capture d’écran 2023-09-12 160111](https://github.com/AbirOuerghi072/gRPC_project/assets/144790093/8e4dcffb-eae1-4f8d-ba93-c850f4cd8319)

### Creating code for a Wi-Fi server and BLE (Bluetooth Low Energy) server

To begin, we initiate by configuring the ESP32 as both a Wi-Fi server and a BLE server within the Arduino IDE. 
#### For the Wi-Fi server:
We set up the appropriate network credentials and establish a server instance to handle incoming client requests, allowing seamless communication between devices over Wi-Fi.

<img src="https://github.com/AbirOuerghi072/gRPC_project/assets/144790093/f317cd5e-ed00-4b3f-a494-7faf86db8e3d" width="600" height="500">

 
#### For the BLE server:
We configure the ESP32 to advertise its services and characteristics, enabling other BLE devices to discover and interact with it. 

<img src="https://github.com/AbirOuerghi072/gRPC_project/assets/144790093/000c97bf-15e5-443b-9dfd-f00cba159b5a" width="600" height="500">


