//Libraries for LoRa
#include <SPI.h>
#include <LoRa.h>
#include <WiFi.h>
//Libraries for OLED Display
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>


//define the pins used by the LoRa transceiver module
#define SCK 5
#define MISO 19
#define MOSI 27
#define SS 18
#define RST 14
#define DIO0 26
// Replace with the generated UUIDs
#define SERVICE_UUID    "B3888744-F2fB-460F-824A-1756AE5FE75A"
#define CHARACTERISTIC_UUID "DD93A5F9-11E8-43A0-A1EB-9DA17D7B16B4"


//433E6 for Asia
//866E6 for Europe
//915E6 for North America
#define BAND 866E6

//OLED pins
#define OLED_SDA 4
#define OLED_SCL 15 
#define OLED_RST 16
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RST);


BLECharacteristic *pCharacteristic;
bool deviceConnected = false;
BLEServer *pServer;

// Define the MyServerCallbacks class here
class MyServerCallbacks : public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) {
        deviceConnected = true;
    }

    void onDisconnect(BLEServer* pServer) {
        deviceConnected = false;
    }
};


void setup() {
  //initialize Serial Monitor
  Serial.begin(115200);

  //reset OLED display via software
  pinMode(OLED_RST, OUTPUT);
  digitalWrite(OLED_RST, LOW);
  delay(20);
  digitalWrite(OLED_RST, HIGH);

  //initialize OLED
  Wire.begin(OLED_SDA, OLED_SCL);
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3c, false, false)) { // Address 0x3C for 128x32
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever  
  }
display.clearDisplay();
  display.setTextColor(WHITE);
  display.setTextSize(1);
  display.setCursor(0,0);
  display.print("LORA SENDER ");
  display.display();
  
  Serial.println("LoRa Sender Test");

  //SPI LoRa pins
  SPI.begin(SCK, MISO, MOSI, SS);
  //setup LoRa transceiver module
  LoRa.setPins(SS, RST, DIO0);
  
  if (!LoRa.begin(BAND)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
  Serial.println("ESP32_BLE Activate");
  display.setCursor(0,10);
  display.print("ESP32_BLE Activate");
  display.display();
  delay(2000);

  BLEDevice::init("ESP32_LoRa_BLE");
  pServer = BLEDevice::createServer();
  pServer->setCallbacks(new MyServerCallbacks());
  BLEService *pService = pServer->createService(SERVICE_UUID);
  pCharacteristic = pService->createCharacteristic(
    CHARACTERISTIC_UUID,
    BLECharacteristic::PROPERTY_READ |
    BLECharacteristic::PROPERTY_WRITE
  );

  pCharacteristic->addDescriptor(new BLE2902());
  pService->start();

  BLEAdvertising *pAdvertising = pServer->getAdvertising();
  pAdvertising->start();  if (deviceConnected) {
    // Send data to the PC here
    String message = "Hello, PC!";
    pCharacteristic->setValue(message.c_str());
    pCharacteristic->notify();

    delay(1000); // Adjust the delay as needed
  }

}

void loop() {
  Serial.println("server started...");
     display.setCursor(0,20);
     display.setTextSize(0.5);
     display.print("server started...");
     display.display();
  

   if (deviceConnected) {
     Serial.println("client connected");
     display.setCursor(0,30);
     display.setTextSize(0.5);
     display.print("client connected");
     display.display();
    // Send data to the PC here
    String message = "Hello, PC!";
    pCharacteristic->setValue(message.c_str());
    pCharacteristic->notify();
    Serial.println("message sent..!");
    display.setCursor(0,40);
    display.setTextSize(0.5);
    display.print("message sent..!");
    display.display();
    

    delay(1000); // Adjust the delay as needed
    deviceConnected=false;
    Serial.println("client disconnected");
    display.setCursor(0,50);
    display.setTextSize(0.5);
    display.print("client disconnected");
    display.display();
    
  }
} 
