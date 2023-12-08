#!/usr/bin/env python3
import serial
import time


def send_solenoids(combo):
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    
    combo_list = [combo]
    length = len(combo_list)
    combo_list = ["x"] + combo_list
    count = 0
    for combo in combo_list:
        line = b''
        while line == b'':
            ser.write(bytes(f"{combo} ", 'utf-8'))
            line = ser.readline()
        if line[8:12].decode('utf-8') == "sent":
            count += 1
        time.sleep(1)