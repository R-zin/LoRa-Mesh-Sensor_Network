import serial
import RPi.GPIO as GPIO
import time
def Extended_response_test():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(22, GPIO.OUT)  # M0
    GPIO.setup(27, GPIO.OUT)  # M1

    print("Resetting module...")
    # Step 1 - reset to normal mode first
    GPIO.output(22, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    time.sleep(1)  # wait 1 second in normal mode

    # Step 2 - now switch to config mode
    print("Entering config mode...")
    GPIO.output(22, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(2)  # wait 2 full seconds — longer than before

    print("Opening serial...")
    ser = serial.Serial(
        port="/dev/ttyS0",
        baudrate=9600,
        timeout=2
    )
    ser.flushInput()
    time.sleep(0.5)  # flush and wait

    # Step 3 - send read command
    print("Sending read command...")
    ser.write(bytes([0xC1, 0x00, 0x09]))
    time.sleep(1)

    if ser.inWaiting() > 0:
        response = ser.read(ser.inWaiting())
        print(f"Bytes      : {len(response)}")
        print(f"HEX        : {response.hex()}")

        if response[0] == 0xC1 and len(response) == 12:
            print("✅ Config read successful!")
            print(f"Address    : {(response[3] << 8) + response[4]}")
            print(f"Frequency  : {response[8] + 850}MHz")
            print(f"Air Speed  : {response[6] & 0x07}")
            print(f"Power      : {response[7] & 0x03}")
        else:
            print(f"❌ Unexpected response: {response.hex()}")
    else:
        print("❌ No response")

    ser.close()
    GPIO.cleanup()
def baud_rate_test():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)

    # Reset first
    GPIO.output(22, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    time.sleep(1)

    # Config mode
    GPIO.output(22, GPIO.LOW)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(2)

    BAUD_RATES = [115200, 57600, 38400, 19200, 9600, 4800, 2400, 1200]

    for baud in BAUD_RATES:
        print(f"\nTrying: {baud}")
        try:
            ser = serial.Serial(
                port="/dev/ttyS0",
                baudrate=baud,
                timeout=2
            )
            ser.flushInput()
            time.sleep(0.5)

            ser.write(bytes([0xC1, 0x00, 0x09]))
            time.sleep(1)

            if ser.inWaiting() > 0:
                response = ser.read(ser.inWaiting())
                print(f"HEX : {response.hex()}")
                print(f"RAW : {list(response)}")

                if response[0] == 0xC1 and len(response) == 12:
                    print(f"✅ FOUND! Correct baud rate: {baud}")
                    break
                else:
                    print(f"❌ Wrong at {baud}")
            else:
                print(f"❌ No response at {baud}")

            ser.close()
            time.sleep(0.5)

        except Exception as e:
            print(f"Error: {e}")

    GPIO.cleanup()
