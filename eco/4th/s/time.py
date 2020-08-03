import datetime
import time

try:
    while True:
        now = datetime.datetime.now()
        nowTime = now.strftime('%H:%M:%S')
        print(nowTime)
        time.sleep(1)

except KeyboardInterrupt:
    print("done")
