from time import sleep
import time
import pigpio


def Alarm(alarmday: int, alarmhour: int, alarmmin: int, openclose: str) -> int:
    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

    print(named_tuple.tm_hour)
    kk = 1
    z = 0

    while kk == 1:
        named_tuple = time.localtime()  # get struct_time
        if (named_tuple.tm_min == alarmmin) & (named_tuple.tm_hour == alarmhour) & (named_tuple.tm_mday == alarmday):
            pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
            pi.set_PWM_frequency(STEP, 500)
            if openClose == "open":
                pi.write(DIR, pi.read(SWITCH))  # Set to open, otherwise stays in close
            for z in range(10):
                sleep(.1)
                print("hi")
            if z == 9:
                kk = 0

        sleep(1)

    return z
