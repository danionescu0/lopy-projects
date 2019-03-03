from pytrack import Pytrack
#from pysense import Pysense

import pycom
import time

pycom.heartbeat(False)

py = Pytrack()
# py = Pysense()

# display the reset reason code and the sleep remaining in seconds
# possible values of wakeup reason are:
# WAKE_REASON_ACCELEROMETER = 1
# WAKE_REASON_PUSH_BUTTON = 2
# WAKE_REASON_TIMER = 4
# WAKE_REASON_INT_PIN = 8
print("Wakeup reason: " + str(py.get_wake_reason()) + "; Aproximate sleep remaining: " + str(py.get_sleep_remaining()) + " sec")
time.sleep(0.5)

# enable wakeup source from INT pin
py.setup_int_pin_wake_up(False)

# enable activity and also inactivity interrupts, using the default callback handler
py.setup_int_wake_up(True, True)

# enable the activity/inactivity interrupts
# set the accelereation threshold to 2000mG (2G) and the min duration to 200ms



time.sleep(0.1)

# go to sleep for 5 minutes maximum if no accelerometer interrupt happens
while True:
    print('sleeping')
    py.setup_sleep(5)
    py.go_to_sleep()
    time.sleep(5)
    print('normal mode')
