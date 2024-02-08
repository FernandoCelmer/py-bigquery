import argparse

from py_bigquery.base.command import BaseCommand, Command
from py_bigquery.commands.test import Test


class CommandTest(Command):

    def execute(self):
        """Start"""
        Test(**self.arguments.__dict__)


class BuildCommand:

    base_command = BaseCommand

    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description='BigQueryORM')

        self.command = self.base_command(parser)
        self.core_commands()
        self.command.run()

    def core_commands(self):
        self.command.cmd_test.set_defaults(exec=CommandTest)
        self.setup()

    def setup(self) -> str:
        return "Method not Implemented"


def main():
    BuildCommand()


if __name__ == '__main__':
    main()
