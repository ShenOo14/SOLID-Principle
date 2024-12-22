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


# Example usage
report = Report("Monthly Report", "This is the content of the monthly report.")
printer = ReportPrinter(report)
printer.print_report()