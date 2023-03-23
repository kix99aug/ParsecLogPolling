# ParsecLogPolling
Poll the Parsec log and take action when someone connects to the host.
The procedure I need to execute involves changing the DPI of the Parsec virtual monitor depending on whether the connection is from Windows or Mac.

# Prerequisite
Python 3 should be installed and added to the system path.

# Installation
1. Clone this repository to your local machine.
2. From the command prompt, navigate to the directory cloned and run the following commands:
```./ParsecLogPollingService.exe install && ./ParsecLogPollingService.exe start```

# Uninstallation
From the command prompt, navigate to the directory cloned and run the following commands:
```./ParsecLogPollingService.exe stop && ./ParsecLogPollingService.exe uninstall```

# Related Repository
SetDPI.exe from https://github.com/imniko/SetDPI
Service wrapper from https://github.com/winsw/winsw

# License
MIT
