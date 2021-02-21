#include "DHT.h"
#include <Bridge.h>

#define DHTPIN 2

#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  Bridge.begin();
  dht.begin();
}

void loop()
{
  delay(2000);
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  String dataString = String(humidity) + "/" + String(temperature);
  Bridge.put("TH_DATA", dataString);
}
