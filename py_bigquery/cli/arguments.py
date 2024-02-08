"""
Module Arguments
"""


from py_bigquery import __version__
    

class Arguments:

    def __init__(self, parser, arguments) -> None:
        self.parser = parser
        self.arguments = arguments
        self.execute()

    def execute(self) -> str:
        return "Method not Implemented"
