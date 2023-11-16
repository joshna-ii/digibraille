String command;

int s1 = 10; 
int s2 = 11; 
int s3 = 12; 
int s4 = 13; 

const int numPins = 4;
int pins[numPins] = {s1, s2, s3, s4};
int d = 250; 

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

void combinations(String s){
   //solenoid combinations
   if (s.equals("0")){ comb0();}
   if (s.equals("1")){ comb1();}
   if (s.equals("2")){ comb2();}
   if (s.equals("3")){ comb3();}
   if (s.equals("4")){ comb4();}
   if (s.equals("5")){ comb5();}
   if (s.equals("6")){ comb6();}
   if (s.equals("7")){ comb7();}
   if (s.equals("8")){ comb8();}
   if (s.equals("9")){ comb9();}
   if (s.equals("10")){ comb10();}
   if (s.equals("11")){ comb11();}
   if (s.equals("12")){ comb12();}
   if (s.equals("13")){ comb13();}
   if (s.equals("14")){ comb14();}
   if (s.equals("15")){ comb15();}      
}

void test(){
   //solenoid combinations
   int pos = 0;
   //combinations(command);
   while (pos != -1){
    int nextPos = command.indexOf(' ', pos);
    if (nextPos == -1){
       String s = command.substring(pos, nextPos); 
       pos = nextPos; 
       combinations(s); 
    }
    if (nextPos != -1){
       String s = command.substring(pos, nextPos);
       pos = nextPos + 1; // Move the position to the character after the space
       combinations(s); 
    }
   }
}

// the loop function runs over and over again forever
void loop() {
  if (Serial.available()){
    command = Serial.readStringUntil('\n'); //this should be the combo that the rpi sends over
    Serial.print("arduino recieved: ");
    Serial.println(command);
    command.trim();
    if (command.equals("s1_on")){
      digitalWrite(s1, HIGH);  
      delay(d);
      digitalWrite(s1, LOW);  
      delay(d);
    }
    if (command.equals("s1_off")){
      digitalWrite(s1, LOW);  
    }

    if (command.equals("s2_on")){
      digitalWrite(s2, HIGH); 
      delay(d);
      digitalWrite(s2, LOW);   
      delay(d);
    }
    if (command.equals("s2_off")){
      digitalWrite(s2, LOW);  
    }
    
    if (command.equals("s3_on")){
      digitalWrite(s3, HIGH); 
      delay(d);
      digitalWrite(s3, LOW);  
      delay(d); 
    }
    if (command.equals("s3_off")){
      digitalWrite(s3, LOW);  
    }
    
    if (command.equals("s4_on")){
      digitalWrite(s4, HIGH); 
      delay(d);
      digitalWrite(s4, LOW);  
      delay(d); 
    }
    if (command.equals("s4_off")){
      digitalWrite(s4, LOW);  
    }
    
    test(); 
    //combinations(); 
  }
  

}
