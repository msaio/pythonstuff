# x // y better than int(x/y)
import time

start_time = time.time()

for x in range(1,10000):
    y = int(10000/x)

end_time = time.time()
print(end_time-start_time)

start_time = time.time()

for x in range(1,10000):
    y = 10000//x

end_time = time.time()
print(end_time-start_time)