from time import sleep
import pigpio
import time

DIR = 20     # Direction GPIO Pin
STEP = 21    # Step GPIO Pin
SWITCH = 16  # GPIO pin of switch

# Connect to pigpiod daemon
pi = pigpio.pi()

# Set up pins as an output
pi.set_mode(DIR, pigpio.OUTPUT)
pi.set_mode(STEP, pigpio.OUTPUT)

# Set up input switch
pi.set_mode(SWITCH, pigpio.INPUT)
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)

MODE = (14, 15, 8)   # Microstep Resolution GPIO Pins
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
for i in range(3):
    pi.write(MODE[i], RESOLUTION['Full'][i])

# Set duty cycle and frequency
# 500 pulses per second


named_tuple = time.localtime()  # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(named_tuple.tm_hour)
kk = 1
jj = 1
z = 0
print(kk)
alarmHour = 16
alarmMin = 11

while kk == 1:
    named_tuple = time.localtime()  # get struct_time
    if (named_tuple.tm_min == alarmMin) & (named_tuple.tm_hour == alarmHour):
        pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
        pi.set_PWM_frequency(STEP, 500)
        pi.write(DIR, pi.read(SWITCH))  # Set direction
        
        for z in range(10):
            sleep(.1)
            print("hi")
        if z == 9:
            kk = 0

    sleep(1)

pi.set_PWM_dutycycle(STEP, 0)  # PWM off
pi.stop()