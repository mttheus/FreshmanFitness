/*!
 2 * @file DFRobot_Heartrate.h
 3 * @brief DFRobot_Heartrate.h detailed description for Heartrate
.cpp
 4 *
 5 * This is written for the heart rate sensor the company librar
y. Mainly used for real
 6 * time measurement of blood oxygen saturation, based on measur
ed values calculate heart rate values.
 7 *
 8 * @author linfeng(Musk.lin@dfrobot.com)
 9 * @version V1.1
10 * @date 2016-8-16
11 * @version V1.0
12 * @date 2015-12-24
13 */
const uint8_t heartratePin = A0; 
#include "DFRobot_Heartrate.h"
const int buzzer = 9; //buzzer to arduino pin 9
const int HR_THRESHOLD = 100; // Heart rate threshold for buzzer activation

DFRobot_Heartrate heartrate(ANALOG_MODE); ///< ANALOG_MODE or Digital Mode

void setup() {
 Serial.begin(115200);
 //Serial.println("Test");
 pinMode(12, OUTPUT);
 }

 void loop() {
 uint8_t rateValue;
 heartrate.getValue(heartratePin); ///< A1 foot sampled values
 rateValue = heartrate.getRate(); ///< Get heart rate value
 if(rateValue) {
  //Serial.print("Heart Rate: ");
  Serial.println(rateValue);
  if (rateValue > 140) {
    digitalWrite(12, HIGH);
  } else {
    digitalWrite(12, LOW);
  }
 }


 delay(20);
 }
