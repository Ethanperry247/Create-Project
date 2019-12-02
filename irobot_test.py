import serial
import time
import keyboard

class Robot():

    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate=57600)
        print("Serial Port Name:", self.ser.name)
        print("Baudrate:", self.ser.baudrate)
        print ("Use Key Controls (WASD) to move and E to exit.")
        self.safe_start()

    def __del__(self):
        self.ser.close()

    def run(self):
            if (keyboard.is_pressed('w')):
                self.move(200,200)
            elif (keyboard.is_pressed('s')):
                self.move(-200,200)
            elif (keyboard.is_pressed('a')):
                self.turn(True)
            elif (keyboard.is_pressed('d')):
                self.turn(False)
            elif (keyboard.is_pressed('e')):
                pass

    def run(self, code):
            if (code == 0x02):
                self.move(200,200)
            elif (code == 0x03):
                self.move(-200,200)
            elif (code == 0x04):
                self.turn(True)
            elif (code == 0x05):
                self.turn(False)
            else:
                pass

    #Starts the robot up in safe mode to prevent overheating, crashes, etc. Gives the robot time to sleep before operation.
    def safe_start(self):
        ser = self.ser
        ser.write(b'\x80')
        ser.write(b'\x84')
        time.sleep(3)

    #Takes in a distance and a speed to move the robot. Distance can be positive or negative. Speed should be positive.
    def move(self, distance, speed):
        ser = self.ser
        array = bytearray()
        start_code = 145

        seconds = 0.0
        seconds = distance/speed
        seconds = abs(seconds)

        if (distance > 0):
            speed = speed
            low_byte = 0
            high_byte = speed

        if (distance < 0):
            temp1 = 0xFF
            temp2 = speed
            temp3 = temp2 ^ temp1 
            temp3 = temp3 + 0x01
            low_byte = 255
            high_byte = int(temp3)
            # print(hex(low_byte))
            # print(hex(high_byte))
        
        array.append(start_code)
        array.append(low_byte)
        array.append(high_byte)
        array.append(low_byte)
        array.append(high_byte)
        # print(array)
        ser.write(array)
        # print (seconds)
        time.sleep(seconds)
        ser.write(b'\x89\x00\x00\x00\x00')

    #True is left, false is right. Turns 90 degrees.
    def turn(self, left_right):
        ser = self.ser
        array = bytearray()
        array.append(137)
        if (left_right):
            array.append(0)
            array.append(200)
        else:
            array.append(255)
            array.append(55)
        array.append(0)
        array.append(0)

        ser.write(array)
        time.sleep(1.1)
        ser.write(b'\x89\x00\x00\x00\x00')

class RobotMessenger():

    def run(self):
            if (keyboard.is_pressed('w')):
                return 0x02
            elif (keyboard.is_pressed('s')):
                return 0x03
            elif (keyboard.is_pressed('a')):
                return 0x04
            elif (keyboard.is_pressed('d')):
                return 0x05
            elif (keyboard.is_pressed('e')):
                pass

    






