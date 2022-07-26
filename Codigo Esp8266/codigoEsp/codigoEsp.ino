#include <DHT.h>
#include <DHT_U.h>
DHT dht(D1, DHT11);

#include <SoftwareSerial.h>
#include <ArduinoJson.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>
const char* ssid = "HOME-56EE";
const char* password =  "72346192FBB98FDF";

const int ligthpin =D0;
const int Sensorhumidity=A0;
void setup() {
  Serial.begin(115200);
  pinMode(ligthpin,INPUT);
  Serial.println("DHT11 Output!");
  dht.begin();
  while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

}

void loop() {
  int ligth=digitalRead(ligthpin);
  int humidityS = analogRead(Sensorhumidity);
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  Serial.print("Recieved ligth:  ");
  Serial.print(ligth);
  Serial.print("Recieved Humidity:  ");
  Serial.println(humidityS);  
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" *C");   
  delay(3000);

  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status

      HTTPClient http;
      String datos_a_enviar = "temperature=" + String(temperature) +"&humidityA=" + String(humidity) +"&humidityS=" + String(humidityS) +"&light=" + String(ligth) ;

      http.begin("http://proyectoalcoholimetrohost.000webhostapp.com/insertarDatos.php");        //Indicamos el destino
      http.addHeader("Content-Type", "application/x-www-form-urlencoded"); //Preparamos el header text/plain si solo vamos a enviar texto plano sin un paradigma llave:valor.

      int codigo_respuesta = http.POST(datos_a_enviar);   //Enviamos el post pasándole, los datos que queremos enviar. (esta función nos devuelve un código que guardamos en un int)

      if (codigo_respuesta > 0) {
        Serial.println("Código HTTP ► " + String(codigo_respuesta));   //Print return code

        if (codigo_respuesta == 200) {
          String cuerpo_respuesta = http.getString();
          Serial.println("El servidor respondió ▼ ");
          Serial.println(cuerpo_respuesta);}
        else {

        Serial.print("Error enviando POST, código: ");
        Serial.println(codigo_respuesta);

      }

      http.end();  //libero recursos

      } 
    else {

      Serial.println("Error en la conexión WIFI");

    }

    delay(2000);        
  
}}
