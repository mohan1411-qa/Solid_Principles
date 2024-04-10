class IPrinter:
    def print(self):
        pass

class IScan:
    def scan(self):
        pass

class IFax:
    def fax(self):
        pass

class Printer(IPrinter):
    def print(self):
        print("Printing....")

class Scanner(IScan):
    def scan(self):
        print("Scanning....")

class Fax(IFax):
    def fax(self):
        print("Fax....")