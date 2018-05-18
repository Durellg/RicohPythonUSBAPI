import subprocess


status = {}
status[0] = "Standby for shooting"
status[1] = "Continuous shooting in progress"

class RicohCapture:

    def __init__(self):
        subprocess.call("ptpcam --show-property=0x5001", shell=True)
    def checkCamInfo(self):
        subprocess.call("ptpcam -i", shell=True)
    def listFile(self):
        subprocess.call("ptpcam -L", shell=True)
    def getCameraStatus(self):
        subprocess.call("ptpcam -s 0xD808", shell=True)
    def takePicture(self):
        subprocess.call("ptpcam -c", shell=True)
    def startVidCapture(self):
        subprocess.call("ptpcam -R 0x101c, 0, 0, 1", shell=True)
    def stopVidCapture(self):
        subprocess.call("ptpcam -R 0x1018, 0xFFFFFFFF", shell=True)
    def setProperty(self, propertyNumber, value):
        process = "ptpcam --set-property=%s --val=%s" % (propertyNumber, value)
        subprocess.call(process, shell=True)
        pass
    def setToVideo(self):
        self.setProperty(0x5013, 0x8002);


# ptpcam -s 0x5001 is the same as ptpcam --show-property=0x5001
