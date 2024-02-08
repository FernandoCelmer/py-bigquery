import argparse

from py_bigquery.cli.arguments import Arguments
from py_bigquery.cli.commands import Commands
from py_bigquery.cli.handlers.test import Test
from py_bigquery.cli.handlers.table import Table


class CommandTest(Arguments):

    def execute(self):
        """Start"""
        Test(**self.arguments.__dict__)


class CommandTable(Arguments):

    def execute(self):
        """Start"""
        Table(**self.arguments.__dict__)


class BuildCommand:

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()

        command = Commands(self.parser)
        command.cmd_test.set_defaults(exec=CommandTest)
        command.cmd_table.set_defaults(exec=CommandTable)
    
        self.execute()

    def execute(self):
        try:
            arguments = self.parser.parse_args()
            if hasattr(arguments, 'exec'):
                arguments.exec(parser=self.parser, arguments=arguments)
            else:
                print(f"Py-BigQuery v{__version__}")

        except Exception as error:
            print(error)


def main():
    BuildCommand()


if __name__ == '__main__':
    main()
