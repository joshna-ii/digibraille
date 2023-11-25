#include <AccelStepper.h>


String command;

int s1 = 10; 
int s2 = 11; 
int s3 = 12; 
int s4 = 13; 

const int numPins = 4;
int pins[numPins] = {s1, s2, s3, s4};
int d = 250; 

int ind = 0;  // loop over this to represent indexing with RPi handler 


// DEFINING STEPPER MOTOR VARIABLES 
int n = ; //steps per revolution 
const float lead = ; //lead screw lead 
int steps = ; //number of steps per revolution 


const int STEP_PIN_x = 2; // A4988 "STEP" pin wired to Arduino pin 2 (you can change this)
const int DIR_PIN_x = 3; // A4988 "DIRECTION" pin wired to Arduino pin 3 (you can change this)

const int STEP_PIN_y = 2; // A4988 "STEP" pin wired to Arduino pin 2 (you can change this)
const int DIR_PIN_y = 3; // A4988 "DIRECTION" pin wired to Arduino pin 3 (you can change this)

// make an AccelStepper motor object. "myMotor" can be any name you'd like.
AccelStepper stepper_x(1, STEP_PIN_x, DIR_PIN_x);
AccelStepper stepper_y(1, STEP_PIN_y, DIR_PIN)_y;

int pos = 800; // variable to store motor position instruction



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
  myMotor.setMaxSpeed(1000); // measured in steps per second
  myMotor.setAcceleration(500); // measured in steps per second squared

  /*
      The following line will send an instruction to move the motor to position 10000,
      which would mean 50 full rotations if the motor has 200 steps/revolution
  */
  myMotor.moveTo(10000);

  /*
     To make the motor actually move, you must call the function myMotor.run()
     as often as possible. Here, I keep calling it over and over using a while()
     loop until the motor arrives at its destination
  */
  while (myMotor.distanceToGo() != 0) { // while there is still a distance to go,
    myMotor.run(); // make the motor run
    

  delay(2000);
  
}

void comb0(){
   
}

void comb1(){
    digitalWrite(s4, HIGH); 
    delay(d);
    digitalWrite(s4, LOW);   
    delay(d);
  
}

void comb2(){
    digitalWrite(s3, HIGH); 
    delay(d);
    digitalWrite(s3, LOW);   
    delay(d);
  
}
void comb3(){
    digitalWrite(s3, HIGH); 
    digitalWrite(s4, HIGH); 
    delay(d);
    digitalWrite(s3, LOW);   
    digitalWrite(s4, LOW);   
    delay(d);
  
}

void comb4(){
    digitalWrite(s2, HIGH); 
    delay(d);
    digitalWrite(s2, LOW);   
    delay(d);
  
}

void comb5(){
    digitalWrite(s2, HIGH); 
    digitalWrite(s4, HIGH); 
    delay(d);
    digitalWrite(s4, LOW);   
    digitalWrite(s2, LOW);   
    delay(d);
  
}

void comb6(){
    digitalWrite(s2, HIGH); 
    digitalWrite(s3, HIGH); 
    delay(d);
    digitalWrite(s3, LOW);   
    digitalWrite(s2, LOW);   
    delay(d);
    
}

void comb7(){
    digitalWrite(s2, HIGH); 
    digitalWrite(s3, HIGH); 
    digitalWrite(s4, HIGH); 
    delay(d);
    digitalWrite(s3, LOW);   
    digitalWrite(s2, LOW); 
    digitalWrite(s4, LOW);   
    delay(d);

}

void comb8(){
    digitalWrite(s1, HIGH); 
    delay(d);
    digitalWrite(s1, LOW); 
    delay(d);
  
}

void comb9(){
    digitalWrite(s1, HIGH); 
    digitalWrite(s4, HIGH); 
    delay(d);
    digitalWrite(s4, LOW);   
    digitalWrite(s1, LOW); 
    delay(d);
  
}

void comb10(){
    digitalWrite(s1, HIGH); 
    digitalWrite(s4, HIGH); 
    delay(d);
    digitalWrite(s4, LOW);   
    digitalWrite(s1, LOW); 
    delay(d);
  
}

void comb11(){
    digitalWrite(s1, HIGH); 
    digitalWrite(s4, HIGH); 
    digitalWrite(s3, HIGH); 
    delay(d);
    digitalWrite(s4, LOW);   
    digitalWrite(s1, LOW); 
    digitalWrite(s3, LOW); 
    delay(d);
  
}

void comb12(){
    digitalWrite(s1, HIGH); 
    digitalWrite(s2, HIGH); 
    delay(d);
    digitalWrite(s2, LOW);   
    digitalWrite(s1, LOW); 
    delay(d);
  
}

void comb13(){
    digitalWrite(s1, HIGH); 
    digitalWrite(s2, HIGH); 
    digitalWrite(s4, HIGH); 
    delay(d);
    digitalWrite(s2, LOW);   
    digitalWrite(s1, LOW); 
    digitalWrite(s4, LOW); 
    delay(d);
  
}

void comb14(){
    digitalWrite(s1, HIGH); 
    digitalWrite(s2, HIGH); 
    digitalWrite(s3, HIGH); 
    delay(d);
    digitalWrite(s2, LOW);   
    digitalWrite(s1, LOW); 
    digitalWrite(s3, LOW); 
    delay(d);
  
}

void comb15(){
    digitalWrite(s1, HIGH); 
    digitalWrite(s2, HIGH); 
    digitalWrite(s3, HIGH); 
    digitalWrite(s4, HIGH); 
    delay(d);
    digitalWrite(s2, LOW);   
    digitalWrite(s1, LOW); 
    digitalWrite(s3, LOW); 
    digitalWrite(s4, LOW); 
    delay(d);
  
}

void combinations(String s, int i){
   //solenoid combinations
   if (s.equals("1")){ comb1(); (i % 2 == 0) ? mov_in_cell() : mov_betw_cell();}
   if (s.equals("2")){ comb2(); (i % 2 == 0) ? mov_in_cell() : mov_betw_cell();}
   if (s.equals("3")){ comb3(); (i % 2 == 0) ? mov_in_cell() : mov_betw_cell();}
   if (s.equals("4")){ comb4(); (i % 2 == 0) ? mov_in_cell() : mov_betw_cell();}
   if (s.equals("5")){ comb5(); (i % 2 == 0) ? mov_in_cell() : mov_betw_cell();}
   if (s.equals("6")){ comb6(); (i % 2 == 0) ? mov_in_cell() : mov_betw_cell();}
   if (s.equals("7")){ comb7(); (i % 2 == 0) ? mov_in_cell() : mov_betw_cell();}
   if (s.equals("8")){ comb8(); (i % 2 == 0) ? mov_in_cell() : mov_betw_cell();}
   if (s.equals("9")){ comb9(); (i % 2 == 0) ? mov_in_cell() : mov_betw_cell();}
   if (s.equals("10")){ comb10(); (i % 2 == 0) ? mov_in_cellm1() : mov_betw_cell();}
   if (s.equals("11")){ comb11(); (i % 2 == 0) ? mov_in_cell() : mov_betw_cell();}
       
}

// FILL IN 
//function to move motor in cell (x direction) 
mov_in_cell(int n, const float lead){
  int d = 2.3; //2.3 mm between cells  
  int num_steps = (d/lead)*n; 
  stepper_x.moveTo(num_steps);

  // Move the motor until it reaches the target position
  while (stepper.distanceToGo() != 0) {
    stepper_x.run();
  }

  delay(500); // add delay? 
  
}

// FILL IN 
//function to move motor between cells (x direction) 
mov_betw_cell(int n, const float lead){
  int d = 3.7; //2.3 mm between cells  
  int num_steps = (d/lead)*n; 
  stepper_x.moveTo(num_steps);

  // Move the motor until it reaches the target position
  while (stepper.distanceToGo() != 0) {
    stepper.run();
  }

  delay(500); // add delay? 
}
  
  


// FILL IN 
//function to move motor in y direction 
mov_y(){
  int d = 5.4; //5.4 mm between lines  
  int num_steps = (d/lead)*n; 
  stepper_y.moveTo(num_steps);

  // Move the motor until it reaches the target position
  while (stepper.distanceToGo() != 0) {
    stepper_y.run();
  }

  delay(500); // add delay? 
  
}
  


void test(int i){
   //solenoid combinations
   int pos = 0;

   while (pos != -1){
    int nextPos = command.indexOf(' ', pos);
    if (nextPos == -1){
       String s = command.substring(pos, nextPos); 
       Serial.println(s);
       pos = nextPos; 
       combinations(s,i); 
    }
    if (nextPos != -1){
      String s = command.substring(pos, nextPos);
      Serial.println(s);
      pos = nextPos + 1; // Move the position to the character after the space
      combinations(s,i); // i = index of character in RPi string representation 
    }
    
   }
}

// the loop function runs over and over again forever
void loop() {
  if (Serial.available()){
    i += 1; 
    command = Serial.readStringUntil('\n');
    command.trim();
    if (i != 47){
      test(ind); 
    }
    else{
      move_y() //move x back to front 
      i = 0; 
    }
    //combinations(); 

  }
  

}
