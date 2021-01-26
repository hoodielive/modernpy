def registerHere(f): return f 
@registerHere
def startRegistration():
    return 'Registration is now closed.'

register = registerHere(startRegistration())
print(register)

class RegistrateProphets:
    def __init__(self, name, dateTime, registration):
        self._name = name
        self._dateTime = dateTime
        self._registration = registration

    def createRegistration():
        @registerHere
        return registerHere



