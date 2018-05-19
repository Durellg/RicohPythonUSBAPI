import subprocess
import time

status = {}
status[0] = "Mode is 0, Ready for shooting"
status[1] = "Mode is 1, Continuous shooting in progress"

class RicohCapture:

    def __init__(self):
        self.getBatteryLevel()
        self.getCurrentStatus()
    def getBatteryLevel(self):
        subprocess.call("ptpcam --show-property=0x5001", shell=True)
    def checkCamInfo(self):
        subprocess.call("ptpcam -i", shell=True)
    def listFiles(self):
        subprocess.call("ptpcam -L", shell=True)
    def getLastFile(self):
        files = subprocess.check_output("ptpcam -L", shell=True)
        lines = files.splitlines()
        lastline = lines[(len(lines) - 2)]
        arr = lastline.split(":")
        fileHandler = arr[0]
        process = "ptpcam -g %s" % (fileHandler)
        subprocess.call(process, shell=True)
    def getCameraStatus(self):
        subprocess.call("ptpcam -s 0xD808", shell=True)
    def takePicture(self):
        subprocess.call("ptpcam -c", shell=True)
    def startVidCapture(self):
        subprocess.call("ptpcam -R 0x101c,0,0,1", shell=True)
    def stopVidCapture(self):
        subprocess.call("ptpcam -R 0x1018,0xFFFFFFFF", shell=True)
    def setProperty(self, propertyNumber, value):
        process = "ptpcam --set-property=%s --val=%s" % (propertyNumber, value)
        subprocess.call(process, shell=True)
    def setToPictureMode(self):
        self.setProperty("0x5013", "0x8001");
    def setToVideoMode(self):
        self.setProperty("0x5013", "0x8002");
    def getCurrentStatus(self):
        currentStatus = subprocess.check_output("ptpcam -s 0xD808", shell=True)
        modeNumber = int(filter(str.isdigit, currentMode))
        print status[modeNumber]
        
    def setCaptureTime(self):
        pass
        


# ptpcam -s 0x5001 is the same as ptpcam --show-property=0x5001
rc = RicohCapture()
#rc.listFile()
#Src.getLastFile()

#rc.startVidCapture()

#time.sleep(10)

#rc.stopVidCapture()
#python >>> execfile('RicohCapture.py)