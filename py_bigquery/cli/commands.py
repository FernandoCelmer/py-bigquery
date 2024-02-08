"""
Module Commands
"""

from py_bigquery import __version__


class Commands:

    def __init__(self, parser):
        self.parser = parser
        self.subparsers = self.parser.add_subparsers()

        self.parser._positionals.title = 'Commands'
        self.parser._optionals.title = 'Default Options'
        self.parser.add_argument(
            '-v',
            '--version',
            action='version',
            version=f"biguqery_orm=={__version__}",
            help="Show program's version number and exit.")

        self.setup_test()
        self.setup_table()

    def setup_test(self):
        self.cmd_test = self.subparsers.add_parser('test')
        self.cmd_test = self.cmd_test.add_argument_group('Usage: bigquery test [OPTIONS]')

    def setup_table(self):
        self.cmd_table = self.subparsers.add_parser('table')
        self.cmd_table = self.cmd_table.add_argument_group('Usage: bigquery table [OPTIONS]')

        self.cmd_table.add_argument('--generate-dataclass')
        self.cmd_table.add_argument('--generate-pydantic')
        self.cmd_table.add_argument('--generate-sqlalchemy')
