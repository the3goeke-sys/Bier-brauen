#include <Wire.h>
#include <SparkFun_Qwiic_Scale_NAU7802_Arduino_Library.h>
#include <SparkFun_TMAG5273_Arduino_Library.h>

NAU7802 scale;
TMAG5273 mag;

void setup() {
  Serial.begin(115200);
  delay(1000);

  Wire.begin(); // ESP32 I2C Start

  Serial.println("Starte Sensoren...");

  // -------- Gewichtssensor --------
  if (!scale.begin()) {
    Serial.println("❌ Gewichtssensor NICHT gefunden!");
  } else {
    Serial.println("✔ Gewichtssensor OK");
  }

  // -------- Magnetfeldsensor --------
  if (mag.begin() != 0) {
    Serial.println("❌ Magnetfeldsensor NICHT gefunden!");
  } else {
    Serial.println("✔ Magnetfeldsensor OK");
  }

  Serial.println("Setup fertig");
}

void loop() {

  // -------- Gewicht --------
  long gewicht = 0;
  if (scale.available()) {
    gewicht = scale.getReading();
  }
  if (gewicht > 1000) {
  digitalWrite(LED_BUILTIN, HIGH); // Alarm an
} else {
  digitalWrite(LED_BUILTIN, LOW);  // aus
}

  // -------- Magnetfeld --------
  float mx = mag.getXData();
  float my = mag.getYData();
  float mz = mag.getZData();

if (mx > 0.5) {
  Serial.println("Magnet erkannt!");
  digitalWrite(LED_BUILTIN, HIGH);
}
  // -------- Ausgabe --------
  Serial.print("Gewicht: ");
  Serial.print(gewicht);

  Serial.print(" | Magnet X: ");
  Serial.print(mx);

  Serial.print(" Y: ");
  Serial.print(my);

  Serial.print(" Z: ");
  Serial.println(mz);

  delay(500);
}
