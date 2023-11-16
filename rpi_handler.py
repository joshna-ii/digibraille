#!/usr/bin/env python3
import serial
import time


def send_solenoids(combo_list):
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    
    length = len(combo_list)
    combo_list = ["x"] + combo_list
    count = 0
    while count < length:
        for combo in combo_list:
            if count < length:
                line = b''
                while line == b'':
                    ser.write(bytes(f"{combo} ", 'utf-8'))
                    line = ser.readline()
                with open("arduino_output.txt", "a") as f:
                    f.writelines(f"{line.decode('utf-8').rstrip()}\n")
                if line[8:12].decode('utf-8') == "sent":
                    count += 1
                time.sleep(1)


#send_solenoids([str(8), str(2), str(3), str(5), str(8), str(0), str(9), str(11), str(15)])