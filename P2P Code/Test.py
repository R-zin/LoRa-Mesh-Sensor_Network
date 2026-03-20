import serial
import RPi.GPIO as GPIO
import time
def Simple_response_test():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.OUT)  # M0
    GPIO.setup(27, GPIO.OUT)  # M1

    # put in config mode
    GPIO.output(22, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)

    ser = serial.Serial("/dev/ttyS0", 9600)
    ser.write(bytes([0xC1, 0x00, 0x09]))  # request settings


    time.sleep(0.5)
    if ser.inWaiting() > 0:
        print("Waveshare SX1262 responding  :", ser.read(ser.inWaiting()).hex())
    else:
        print("No response — check connections ")