import time

class TimerTool:
    def run(self):
        seconds = int(input("Enter seconds: "))
        print("Timer started...")
        time.sleep(seconds)
        print("⏰ Time's up!")
