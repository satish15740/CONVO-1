import os

def uptime():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            return uptime_seconds
    except Exception as e:
        print("Error:", e)
        return None

def format_uptime(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:0>2}:{:0>2}:{:0>2}".format(int(hours), int(minutes), int(seconds))

if __name__ == "__main__":
    uptime_seconds = uptime()
    if uptime_seconds:
        print("System uptime:", format_uptime(uptime_seconds)
