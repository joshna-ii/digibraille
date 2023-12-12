#!/usr/bin/env python3
import serial
import time


def send_solenoids(combos):
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()

    combo_list = combos.split(" ")
    combo_list = ["5"] + combo_list + ["6"]

    combo_list = [j for i,j in enumerate(combo_list) if j!=""]

    with open("arduino_output.txt", "w") as f:
        f.writelines(f'{combo_list}\n')
    
    x_coord = 1
    y_coord = 1
    ready = False
    for i in range(len(combo_list)):
        combo =  combo_list[i]
        instruction = f"{combo} {x_coord} {y_coord}"
        with open("arduino_output.txt", "a") as f:
            f.writelines(f'{instruction}\n')

        while not ready:
            sending = bytes(instruction, 'utf-8')
            ser.write(sending)
            received = ser.readline().decode('utf-8')
            if received != "":
                with open("arduino_output.txt", "a") as f:
                    f.writelines(f'{received}\n')
            if "start" in received:
                ready = True
        ready = False

        while not ready:
            received = ser.readline().decode('utf-8')
            if received != "":
                with open("arduino_output.txt", "a") as f:
                    f.writelines(f'{received}\n')
            if "done" in received:
                ready = True
        ready = False

        if combo != "z":
            if i%12 == 0:
                x_coord = 1
                y_coord += 1
            else:
                x_coord += 1
    
    with open("arduino_output.txt", "a") as f:
        f.writelines(f'FINISHED\n')