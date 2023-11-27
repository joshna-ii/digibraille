#include <AccelStepper.h>


String command;

int s1 = 10; 
int s2 = 11; 
int s3 = 12; 
int s4 = 9; 

const int numPins = 4;
int pins[numPins] = {s1, s2, s3, s4};
int d = 250; 

int ind = 20;  // loop over this to represent indexing with RPi handler 


// DEFINING STEPPER MOTOR VARIABLES 


const int STEP_PIN_x = 2; // A4988 "STEP" pin wired to Arduino pin 2 (you can change this)
const int DIR_PIN_x = 3; // A4988 "DIRECTION" pin wired to Arduino pin 3 (you can change this)

const int STEP_PIN_y = 4; // A4988 "STEP" pin wired to Arduino pin 2 (you can change this)
const int DIR_PIN_y = 5; // A4988 "DIRECTION" pin wired to Arduino pin 3 (you can change this)

// make an AccelStepper motor object. "myMotor" can be any name you'd like.
AccelStepper stepper_x(1, STEP_PIN_x, DIR_PIN_x);
AccelStepper stepper_y(1, STEP_PIN_y, DIR_PIN_y);

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
  stepper_x.setMaxSpeed(1000); // measured in steps per second
  stepper_x.setAcceleration(500); // measured in steps per second squared

  stepper_y.setMaxSpeed(1000); // measured in steps per second
  stepper_y.setAcceleration(500); // measured in steps per second squared

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
    digitalWrite(s4, HIGH); 
    delay(d);
    digitalWrite(s4, LOW);   
    delay(d);
    Serial.println("arduino sent: 1");
}

void comb2(){
    digitalWrite(s3, HIGH); 
    delay(d);
    digitalWrite(s3, LOW);   
    delay(d);
    Serial.println("arduino sent: 2");
}

void comb3(){
    digitalWrite(s3, HIGH); 
    digitalWrite(s4, HIGH); 
    delay(d);
    digitalWrite(s3, LOW);   
    digitalWrite(s4, LOW);   
    delay(d);
    Serial.println("arduino sent: 3");
}

void comb4(){
    digitalWrite(s2, HIGH); 
    delay(d);
    digitalWrite(s2, LOW);   
    delay(d);
    Serial.println("arduino sent: 4");
}

void comb5(){
    digitalWrite(s2, HIGH); 
    digitalWrite(s4, HIGH); 
    delay(d);
    digitalWrite(s4, LOW);   
    digitalWrite(s2, LOW);   
    delay(d);
    Serial.println("arduino sent: 5");
}

void comb6(){
    digitalWrite(s2, HIGH); 
    digitalWrite(s3, HIGH); 
    delay(d);
    digitalWrite(s3, LOW);   
    digitalWrite(s2, LOW);   
    delay(d);
    Serial.println("arduino sent: 6");
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
    Serial.println("arduino sent: 7");
}

void comb8(){
    digitalWrite(s1, HIGH); 
    delay(d);
    digitalWrite(s1, LOW); 
    delay(d);
    Serial.println("arduino sent: 8");
}

void comb9(){
    digitalWrite(s1, HIGH); 
    digitalWrite(s4, HIGH); 
    delay(d);
    digitalWrite(s4, LOW);   
    digitalWrite(s1, LOW); 
    delay(d);
    Serial.println("arduino sent: 9");
}

void comb10(){
    digitalWrite(s1, HIGH); 
    digitalWrite(s4, HIGH); 
    delay(d);
    digitalWrite(s4, LOW);   
    digitalWrite(s1, LOW); 
    delay(d);
    Serial.println("arduino sent: 10");
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
    Serial.println("arduino sent: 11");
}

void comb12(){
    digitalWrite(s1, HIGH); 
    digitalWrite(s2, HIGH); 
    delay(d);
    digitalWrite(s2, LOW);   
    digitalWrite(s1, LOW); 
    delay(d);
    Serial.println("arduino sent: 12");
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
    Serial.println("arduino sent: 13");
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
    Serial.println("arduino sent: 14");
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
    Serial.println("arduino sent: 15");
}

void combinations(String s, int i){
   //solenoid combinations
   if (s.equals("1")){ comb1(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
   if (s.equals("2")){ comb2(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
   if (s.equals("3")){ comb3(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
   if (s.equals("4")){ comb4(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
   if (s.equals("5")){ comb5(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
   if (s.equals("6")){ comb6(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
   if (s.equals("7")){ comb7(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
   if (s.equals("8")){ comb8(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
   if (s.equals("9")){ comb9(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
   if (s.equals("10")){ comb10(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
   if (s.equals("11")){ comb11(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
   if (s.equals("12")){ comb12(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
   if (s.equals("13")){ comb13(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
   if (s.equals("14")){ comb14(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
   if (s.equals("15")){ comb15(); (i % 2 == 0) ? mov_betw_cell() : mov_in_cell();}
       
}

// FILL IN 
//function to move motor in cell (x direction) 
void mov_in_cell(){
  Serial.println("move in cell");
  int dis = 2.3; //2.3 mm between cells  
  int num_steps = dis/(0.009906);
  stepper_x.moveTo(num_steps);

  // Move the motor until it reaches the target position
  while (stepper_x.distanceToGo() != 0) {
    stepper_x.run();
  }

  delay(500); // add delay? 
  
}

// FILL IN 
//function to move motor between cells (x direction) 
void mov_betw_cell(){
  Serial.println("move between cell");
  int dis = 3.7; //2.3 mm between cells  
  int num_steps = dis/(0.009906);  //may need to be cm?
  stepper_x.moveTo(num_steps);

  // Move the motor until it reaches the target position
  while (stepper_x.distanceToGo() != 0) {
    stepper_x.run();
  }

  delay(500); // add delay? 
}
  
  
void mov_to_front(){
  Serial.println("move to front");
  int dis = 55; //2.3 mm between cells  
  int num_steps = dis/(0.009906);  //may need to be cm?
  stepper_x.moveTo(num_steps);

  // Move the motor until it reaches the target position
  while (stepper_x.distanceToGo() != 0) {
    stepper_x.run();
  }

  delay(500); // add delay? 
  ind = 0;
}
  
  

// FILL IN 
//function to move motor in y direction 
void mov_y(){
  int dis = 5.4; //5.4 mm between lines  
  int num_steps = dis/(.009906); 
  stepper_y.moveTo(num_steps);

  // Move the motor until it reaches the target position
  while (stepper_y.distanceToGo() != 0) {
    stepper_y.run();
  }

  delay(500); // add delay? 
  
}
  


void test(){
   //solenoid combinations
   int pos = 0;

   while (pos != -1){
    ind += 1; 
    if (ind != 24){ 
      Serial.println("HERE");
      Serial.print("ind: ");
      Serial.println(ind); 
      int nextPos = command.indexOf(' ', pos);
      if (nextPos == -1){
         String s = command.substring(pos, nextPos); 
     //    Serial.println(s);
         pos = nextPos; 
         combinations(s,ind); 
      }
      if (nextPos != -1){
        String s = command.substring(pos, nextPos);
       // Serial.println(s);
        pos = nextPos + 1; // Move the position to the character after the space
        combinations(s,ind); // i = index of character in RPi string representation 
      }
    }
    else{
      Serial.println("INDEX RESET");
        mov_to_front();
        mov_y(); //move x back to front 
        ind = 0; 
      
    
    }
    
   }
}


// the loop function runs over and over again forever
void loop() {
  if (Serial.available()){
    ind = 20;
    command = Serial.readStringUntil('\n');
    command.trim();    
        
   
    test(); 
  
    //combinations(); 

  }
  

}
