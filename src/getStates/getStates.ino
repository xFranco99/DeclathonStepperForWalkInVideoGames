#define CONT 8

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(CONT, INPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  
  digitalWrite(CONT, HIGH);

  //get value of current state readed from the sensor
  int valCONT = digitalRead(CONT);
  
  Serial.println(valCONT); //write it in serial
  delay(200); //delay to be sure that python can read values from serial
}
