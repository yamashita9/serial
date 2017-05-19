#define LED 13

void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
 pinMode(LED,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
 if(Serial.available() > 0){
 char data = Serial.read();
 if(data == '1'){
 digitalWrite(LED,HIGH);
 }else{
 digitalWrite(LED,LOW);
 }
 }
}
