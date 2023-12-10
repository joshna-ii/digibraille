#include <Stepper.h>
#include "pitches.h"


String command;

int s1 = 2; 
int s2 = 3; 
int s3 = 12; 
int s4 = 13; 

const int numPins = 4;
int pins[numPins] = {s1, s2, s3, s4};
int d = 250; 

int ind = 1;  // loop over this to represent indexing with RPi handler 

int y_ind = 0;

// DEFINING STEPPER MOTOR VARIABLES 

const int d_step = 500;  

const int stepsperrev_y = 200;
const int stepsperrev_x = 200;

int melody[] = {

  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
};

// note durations: 4 = quarter note, 8 = eighth note, etc.:
int noteDurations[] = {

  4, 8, 8, 4, 4, 4, 4, 4
};


void play_tone() {
  Serial.println("IN TONE");

  // iterate over the notes of the melody:

  for (int thisNote = 0; thisNote < 8; thisNote++) {

    // to calculate the note duration, take one second divided by the note type.

    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.

    int noteDuration = 1000 / noteDurations[thisNote];

    tone(12, melody[thisNote], noteDuration);

    // to distinguish the notes, set a minimum time between them.

    // the note's duration + 30% seems to work well:

    int pauseBetweenNotes = noteDuration * 1.30;

    delay(pauseBetweenNotes);

    // stop the tone playing:

    noTone(12);

  }
}

// make an AccelStepper motor object. "myMotor" can be any name you'd like.
Stepper stepper_x(stepsperrev_x, 4,5,6,7);
Stepper stepper_y(stepsperrev_y,8,9,10,11);

int pos = 0; // variable to store motor position instruction

//LDR values
int ldr_value =0;
int threshold = 668; 
bool paper_in = false;

void setup() {
  Serial.begin(9600);
 
  pinMode(s1, OUTPUT);  
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(s4, OUTPUT);


  
  digitalWrite(s1, LOW);  
  digitalWrite(s2, LOW);  
  digitalWrite(s3, LOW);  
  digitalWrite(s4, LOW);  

  // you can change the below values as you'd like
  stepper_x.setSpeed(200); // measured in steps per second
 // stepper_x.setAcceleration(500); // measured in steps per second squared

  stepper_y.setSpeed(200); // measured in steps per second
 // stepper_y.setAcceleration(250); // measured in steps per second squared

  /*
      The following line will send an instruction to move the motor to position 10000,
      which would mean 50 full rotations if the motor has 200 steps/revolution
  */
  /* stepper_x.moveTo(10000);
  stepper_y.moveTo(10000);

  while (stepper_x.distanceToGo() != 0) { // while there is still a distance to go,
    stepper_x.run(); // make the motor run
  }

  while (stepper_y.distanceToGo() != 0) { // while there is still a distance to go,
    stepper_y.run(); // make the motor run
  }*/

  delay(2000);
  
}



void comb0(){
   Serial.println("arduino sent: 0");
}

void comb1(){
    digitalWrite(s1, HIGH); 
    delay(d);
    digitalWrite(s1, LOW);   
    delay(d);
    digitalWrite(s1, HIGH); 
    delay(d);
    digitalWrite(s1, LOW);   
    delay(d);
    Serial.println("arduino sent: 1");
}

void comb2(){
    digitalWrite(s2, HIGH); 
    delay(d);
    digitalWrite(s2, LOW);   
    delay(d);
    digitalWrite(s2, HIGH); 
    delay(d);
    digitalWrite(s2, LOW);   
    delay(d);
    Serial.println("arduino sent: 2");
}

void comb3(){
    digitalWrite(s1, HIGH); 
    digitalWrite(s2, HIGH); 
    delay(d);
    digitalWrite(s1, LOW);   
    digitalWrite(s2, LOW);   
    delay(d);
    digitalWrite(s1, HIGH); 
    digitalWrite(s2, HIGH); 
    delay(d);
    digitalWrite(s1, LOW);   
    digitalWrite(s2, LOW);   
    delay(d);
    Serial.println("arduino sent: 3");
}



void combinations(String s, int i){
   //solenoid combinations
   if (s.equals("0")){ 
      comb0();
    
      if (i % 2 == 0) 
      {
        if ( i % 6 == 0)
        {
          reset_x(i); 
        }
        else
        {
          mov_betw_cell();
        }

      } 
      else {
        mov_in_cell();
      }
      }
   if (s.equals("1")){ 
    
      comb1();
    
      if (i % 2 == 0) 
      {
        if ( i % 6 == 0)
        {
          reset_x(i); 
        }
        else
        {
          mov_betw_cell();
        }

      } 
      else {
        mov_in_cell();
      }
      }
   if (s.equals("2")){ 
      comb2();
    
      if (i % 2 == 0) 
      {
        if ( i % 6== 0)
        {
          reset_x(i); 
        }
        else
        {
          mov_betw_cell();
        }
      } 
      else {
        mov_in_cell();
      }
      }
   if (s.equals("3")){ 
      comb3();
      if (i % 2 == 0) 
      {
        if ( i % 6 == 0)
        {
          reset_x(i); 
        }
        else
        {
          mov_betw_cell();
        }
      } 
      else {
        mov_in_cell();
      }
      }
   
       
}

// FILL IN 
//function to move motor in cell (x direction) 
void mov_in_cell(){
  //digitalWrite(DIR_PIN_x, HIGH);  
  Serial.println("move in cell");
  int dis = 2.3; //2.3 mm between cells  
  int num_steps = dis/(0.039);
  
  stepper_x.step(80);
  
  //Serial.println(stepper_x.currentPosition());

  // Move the motor until it reaches the target position
//  while (stepper_x.distanceToGo() != 0) {
  //  stepper_x.run();
  //}

  delay(d_step); // add delay? 
  
}

// FILL IN 
//function to move motor between cells (x direction) 
void mov_betw_cell(){
  //digitalWrite(DIR_PIN_x, HIGH);  
  Serial.println("move between cell");
  int dis = 3.7; //2.3 mm between cells  
  int num_steps = dis/(0.039);  //may need to be cm?
  
  stepper_x.step(129);
  
 // Serial.println(stepper_x.currentPosition());

  // Move the motor until it reaches the target position
 // while (stepper_x.distanceToGo() != 0) {
   // stepper_x.run();
  //}

  delay(d_step); // add delay? 
}

void reset_x(int ind){
  //digitalWrite(DIR_PIN_x, HIGH);  
  Serial.println("move between cell");
  int dis = 3.7; //2.3 mm between cells  
  int num_steps = dis/(0.039);  //may need to be cm?
  
  stepper_x.step(900);
  
 // Serial.println(stepper_x.currentPosition());

  // Move the motor until it reaches the target position
 // while (stepper_x.distanceToGo() != 0) {
   // stepper_x.run();
  //}

  delay(d_step); // add delay? 
}
  
  
void mov_to_front(int init_pos){
  int dis = 55; //2.3 mm between cells  
  int num_steps = dis/(0.0039);  //may need to be cm?
  
  //digitalWrite(DIR_PIN_x, LOW);
  //delay(100);

  Serial.println(pos);
  stepper_x.step(-2800); //2800

  // Move the motor until it reaches the target position
 // while (stepper_x.distanceToGo() != 0) {
 //   stepper_x.run();
 // }

  
  delay(d_step); // add delay? 
  ind = 0;
}
  
  

// FILL IN 
//function to move motor in y direction 
void mov_y(){
  Serial.println("Moving y");
  int dis = 5.4; //5.4 mm between lines  
  int num_steps = dis/(0.0039); 
  
  stepper_y.step(-15);

  // Move the motor until it reaches the target position
 // while (stepper_y.distanceToGo() != 0) {
  //  stepper_y.run();
  //}

  delay(d_step); // add delay? 
  
}
  

// FILL IN 
//function to move motor in y direction 
void mov_y_cell(){
  Serial.println("Moving y in cell");
  int dis = 5.4; //5.4 mm between lines  
  int num_steps = dis/(0.0039); 
  
  stepper_y.step(-45);

  // Move the motor until it reaches the target position
 // while (stepper_y.distanceToGo() != 0) {
  //  stepper_y.run();
  //}

  delay(d_step); // add delay? 
  
}
  

void test(int init_pos){
   //solenoid combinations
   int pos = 0;

   while (pos != -1){
    Serial.println("pos: ");
    Serial.println(pos);
        
    ind += 1; 
    if (ind != 13){ 
      Serial.println("HERE");
      Serial.print("ind: ");
      Serial.println(ind); 
  
    
      int nextPos = command.indexOf(' ', pos);
      if (nextPos == -1){
         String s = command.substring(pos, nextPos); 
     //    Serial.println(s);
         pos = nextPos; 
         combinations(s,ind);
         Serial.println("Command in loop: ");
         Serial.println(s); 
      }
      if (nextPos != -1){
        String s = command.substring(pos, nextPos);
       // Serial.println(s);
        pos = nextPos + 1; // Move the position to the character after the space
        combinations(s,ind); // i = index of character in RPi string representation 
      }
      
    }
    else{
      y_ind += 1; 
      Serial.println("INDEX RESET");
        mov_to_front(init_pos);
        if (y_ind % 3 == 0){
          mov_y_cell();
        }
        else{
          mov_y();
        }
        ind = 0; 
      
    
    }
    
   }
}


// the loop function runs over and over again forever
void loop() {
  
  

  /*
     To make the motor actually move, you must call the function myMotor.run()
     as often as possible. Here, I keep calling it over and over using a while()
     loop until the motor arrives at its destination
  */

//  if (Serial.available()){
//    
//    }
    ldr_value = analogRead(A5); 
      
    if(ldr_value < threshold){    
          stepper_y.step(-5);
          
      }
    else{
        
      if (Serial.available()){
        play_tone();
        Serial.println(command);
        
        stepper_y.step(120);
        ind = 0;
        int init_pos = 0;
        command = Serial.readString();
        //command.trim(); 
        Serial.println(command);
        
            
       
        test(init_pos);
        delay(1000);
        
        
        Serial.println("done");
        play_tone();
      }
      
    
      
    }

     


    //combinations(); 

  }
  
