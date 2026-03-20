# extended_check.py
import serial
import RPi.GPIO as GPIO
import time

print("Setting up GPIO...")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT)  # M0
GPIO.setup(27, GPIO.OUT)  # M1

print("Putting module in config mode...")
GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.HIGH)
time.sleep(1)  # wait longer — 1 second

print("Opening serial port...")
try:
    ser = serial.Serial(
        port="/dev/ttyS0",
        baudrate=9600,
        timeout=2  # 2 second timeout
    )
    ser.flushInput()
    print("Serial opened OK")
except Exception as e:
    print(f"Serial open FAILED: {e}")
    GPIO.cleanup()
    exit()

# Try sending command 3 times
for attempt in range(3):
    print(f"\nAttempt {attempt + 1}...")
    ser.flushInput()
    ser.write(bytes([0xC1, 0x00, 0x09]))
    time.sleep(1)  # wait 1 full second

    waiting = ser.inWaiting()
    print(f"Bytes waiting: {waiting}")

    if waiting > 0:
        response = ser.read(waiting)
        print(f"Response HEX : {response.hex()}")
        print(f"Response RAW : {response}")
        print("SX1262 responding ")
        break
    else:
        print("No response yet...")
        time.sleep(1)

else:
    print("\nAll attempts failed ")
    print("Check connections and UART settings")

ser.close()
GPIO.cleanup()