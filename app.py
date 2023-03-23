import os
import sys
import time
import re
import time


def log(msg, err=False):
    print(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) +
          msg, file=sys.stderr if err else sys.stdout)


log("Parsec Log Polling - DPI Switcher")


logPath = os.path.expandvars(r"%programdata%\Parsec\log.txt")
logPath = logPath if os.path.exists(
    logPath) else os.path.expandvars(r"%appdata%\Parsec\log.txt")
if not os.path.exists(logPath):
    log("Shutting down, log.txt not found.", err=True)
    exit(1)

lastSize = 0


def processLines(lines):
    for line in lines:
        if "encode_x" in line:
            regex = re.compile(r"encode_x      = (\d+)")
            match = regex.search(line)
            if match:
                xRes = int(match.group(1))
                if xRes == 1920:
                    log("Switching to 125% DPI")
                    os.system("C:\\SetDpi.exe 125 1")
                elif xRes == 2560:
                    log("Switching to 200% DPI")
                    os.system("C:\\SetDpi.exe 200 1")


while True:
    size = os.path.getsize(logPath)
    if lastSize == 0:
        lastSize = size
    if size > lastSize:
        with open(logPath, "r") as f:
            f.seek(lastSize)
            lastSize = size
            lines = f.readlines()
            processLines(lines)
    time.sleep(1)
