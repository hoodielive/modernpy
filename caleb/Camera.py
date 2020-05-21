class Camera:
    def __init__(self, serial_number, position, camera_type):
        self.serial_number = serial_number
        self.position = position
        self.camera_type = camera_type

    def log(self):
        print(self.serial_number, self.position, self.camera_type)

CameraType = Camera("3245235677", "4343", "Nikon")

CameraType.log()
