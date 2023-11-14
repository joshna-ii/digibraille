#!/usr/bin/env python3
import serial
import time

#make this work so that the webapp can send a direction TODO

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        combo = b"3\n"
        ser.write(combo)
        line = ser.readline()
        if type(line) != str:
            line = line.decode('utf-8').rstrip()
        print(line)
        time.sleep(1)
    '''
    while True:
        #ser.read to check sensor
        combo = '3'
        print(f'Sending combo {combo} to Arduino.')
        ser.write(str(combo).encode('utf-8')) #writes combo to serial'''


def send_solenoids(combo_list):
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    for combo in combo_list:
        #ser.read to check sensor
        print(f'Sending combo {combo} to Arduino.')
        ser.write(str(combo).encode('utf-8')) #writes combo to serial