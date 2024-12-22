from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax_document(self, document):
        pass

class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self, document):
        print(f"Scanning: {document}")

    def fax_document(self, document):
        print(f"Faxing: {document}")

class SimplePrinter(Printer):
    def print_document(self, document):
        print(f"Printing: {document}")


document = "SOLID Design Principles"
simple_document = "Simple SOLID Design Principles"

##################################################

printer_obj = SimplePrinter()
printer_obj.print_document(simple_document)

print("-" * 30)

multi_function_printer_obj = MultiFunctionPrinter()
multi_function_printer_obj.print_document(document)
multi_function_printer_obj.scan_document(document)
multi_function_printer_obj.fax_document(document)