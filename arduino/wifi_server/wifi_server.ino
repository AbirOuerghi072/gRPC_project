//Libraries for LoRa
#include <SPI.h>
#include <LoRa.h>
#include <WiFi.h>
//Libraries for OLED Display
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

//define the pins used by the LoRa transceiver module
#define SCK 5
#define MISO 19
#define MOSI 27
#define SS 18
#define RST 14
#define DIO0 26

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


WiFiClient client;
const char *ssid = "Redmi Note 10";
const char *password = "07234236";
const char* pcIpAddress = "127.0.0.1";
WiFiServer server(12345); // Create a TCP server on port 80

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
  Serial.println("LoRa Initializing OK!");
  display.setCursor(0,10);
  display.print("LoRa Initializing OK!");
  display.display();
  delay(2000); 

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  display.clearDisplay();
      display.setCursor(0,0);
      display.setTextSize(0.5);      
      display.println("LORA SENDER");
      display.setCursor(0,10);
      display.setTextSize(1);
      display.print("Connected to Wi-Fi");
      display.display(); 
        delay(100);
      Serial.print("wifi local ip: ");
      Serial.println(WiFi.localIP());
      /*display.setCursor(0,60);
      display.setTextSize(0.1);
      display.print(WiFi.localIP());
      display.display();*/
             

  server.begin(); // Start the server
  display.setCursor(0,20);
      display.setTextSize(0.5);
      display.print("Server started");
      display.display();
}

void loop() {
  WiFiClient client = server.available();

  if (client) {
    Serial.println("New client connected");
    display.setCursor(0,30);
      display.setTextSize(0.5);
      display.print("client connected");
      display.display();
    delay(1000);
    
    // Send data to the PC client
    client.println("Hello from ESP32!");
    display.setCursor(0,40);
      display.setTextSize(0.5);
      display.print("Hello from ESP32!");
      display.display();
    delay(1000);

    // Close the connection
    client.stop();
    Serial.println("Client disconnected");
display.setCursor(0,50);
      display.setTextSize(0.5);
      display.print("client disconnected");
      display.display();
    delay(1000);    
  }
  
  
 
}
