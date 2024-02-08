"""
Module Command
"""


from py_bigquery import __version__
    

class Command:

    list_option = [
        'id',
        'module',
        'tag',
        'item',
        'sudo',
        'debug',
        'group',
        'field',
        'print',
        'args'
    ]

    def __init__(self, parser, arguments) -> None:
        self.parser = parser
        self.arguments = arguments

        self.setup_options()
        self.execute()

    def setup_options(self):
        for option in self.list_option:
            if hasattr(self.arguments, option):
                setattr(self, option, getattr(self.arguments, option))
            else:
                setattr(self, option, None)


class BaseCommand:

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

    def setup_test(self):
        self.cmd_test = self.subparsers.add_parser('test')
        self.cmd_test = self.cmd_test.add_argument_group('Usage: bigquery test [OPTIONS]')

    def run(self):
        try:
            arguments = self.parser.parse_args()
            if hasattr(arguments, 'exec'):
                arguments.exec(parser=self.parser, arguments=arguments)
            else:
                print(f"BigQueryORM v{__version__}")

        except Exception as error:
            print(error)
