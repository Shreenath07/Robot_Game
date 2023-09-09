import os
import threading as t
import motor_test as a
import contours as b
import time

t1 = t.Thread(target = b.m1)
t2 = t.Thread(target = a.m2)

t1.start()
time.sleep(3)
t2.start()
#t2.join()

print('finished')