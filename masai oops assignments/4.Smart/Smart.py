class Appliance:
    def status(self):
        print("This is a smart appliance.")

class Fan(Appliance):
    def status(self):
        print("Fan is ON.")

class Light(Appliance):
    def status(self):
        print("Light is OFF.")

class AC(Appliance):
    def status(self):
        print("AC is set to 24°C.")

# Usage
devices = [Fan(), Light(), AC()]
for device in devices:
    device.status()
