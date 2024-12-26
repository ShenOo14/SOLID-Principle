#violate the single responsibility principle
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def print_report(self):
        print(f"Title: {self.get_title()}")
        print(f"Content: {self.get_content()}")


report = Report("Monthly Report", " content for the monthly report.")
report.print_report()

#achieving single responsibility principle
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content


class ReportPrinter:
    def __init__(self, report):
        self.report = report

    def print_report(self):
        print(f"Title: {self.report.get_title()}")
        print(f"Content: {self.report.get_content()}")



report = Report("Monthly Report", " content for the monthly report.")
printer = ReportPrinter(report)
printer.print_report()
