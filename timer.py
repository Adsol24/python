import time
seconds = int(input("how many seconds: "))
for timer in range(seconds, 0, -1):
    print(timer)
    time.sleep(1)
print("time is up")

