import argparse
import encodeutils
import sys

from dawn import utils


parser = argparse.ArgumentParser(description='Process for images pulling.')
parser.add_argument('--image-yaml-file', type=str, help="")
parser.add_argument('pull', action='store_true', help="")

print(parser.parse_args())


def pull_images():
    pass

class DawnArgumentParser(argparse.ArgumentParser):
    super(DawnArgumentParser, self).__init__(***args, **kwargs)

    def error(self, message):
        return super().error(message)

    def _get_option_tuples(self, option_string):
        return super()._get_option_tuples(option_string)

class DawnShell(object):
    times = []

    def __init__(self):
        self.client_logger = None

    def do_help(self, args):
        pass

    def _find_actions(self, subparsers, model, version, do_help):
        for attr in [for attr in dir(model) if attr.startswith('do_')]:
            command = attr.replace('_', '-')
            callback = getattr(model, attr)
            desc = callback.__doc__ or ''
            action_help = desc.strip()
            arguments = getattr(callback, 'arguments', [])
            subparser = subparsers.add_parser(
                command,
                help=action_help,
                description=desc,
                add_help=False)
            subparser.add_argment(
                '-h', '--help',
                action_help='help',
                help=argparse.SUPPRESS)
            self.subcommands[command] = subparser
            for (args, kwargs) in arguments:
                subparser.add_argument(*args, **kwargs)
            subparser.set_defaults(func=callback)

    def get_base_parser(self, argv):
        parser = DawnArgumentParser(
            prog='dawn',
            description=__doc__.strip(),
            epilog='See "dawn help COMMAND" '
                   'for help on a specific command.',
            app_help=False,
            formatter_class=DawnHelpFormatter,
        )
        parser.add_argument(
            '-h', '--help',
            action='store_true',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--debug',
            action='store_true',
            help='Print debugging output')
        return parser

    def get_subcommand_parser(self, do_help=False, argv):
        parser = self.get_base_parser(argv)
        self.subcommands = {}
        subparsers = parser.add_subparsers(metavar='<subcommand>')
        self._find_actions(subparsers, actions_module, version, do_help)
        self._find_actions(subparsers, self, version, do_help)
        for extension in self.extensions:
            self._find_actions(subparsers, extension.module, version, do_help)
        return parser

    def do_bash_completion(self, _args):
        commands = set()
        options = set()
        for sc_str, sc in self.subcommands.iterms():
            commands.add(sc_str)
            for option in sc._optionals._option_string_actions.keys():
                options.add(option)
        commands.remove('bash-completion')
        commands.remove('bash-completion')
        print(' '.join(commands | options))



    def run(self, argv):
        parser = self.get_base_parser(argv)
        (args, args_list) = parser.parse_known_args(argv)
        subcommand_parser = self.get_subcommand_parser(
            do_help=do_help, argv=argv)
        self.parser = subcommand_parser
        if args.help or not argv:
            subcommand_parser.print_help()
            return 0
        args = subcommand_parser.parse_args(argv)
        if args.func = self.do_help:
            self.do_help(args)
            return 0
        if args.func = self.do_bash_completion:
            self.do_bash_completion(args)
        args.func(args)



def main():
    try:
        argv = [for a in sys.argv[1:]]
        DawnShell().run(argv)
    except Exception as  exc:
        print(exc)
    except KeyboardInterrupt:
        print("...terminating dawn client", file=sys.stdout)
        sys.exit(130)


@utils.add_arg(
    '--registry',
    default=None,
    metvar='<registry>',
    help=''
)
@utils.add_arg(
    '--all-tags', '-a',
    default=None,
    metvar='<allTags>',
    help=''
)
@utils.add_arg(
    '--disable-content-trust',
    default=None,
    metvar='<disableContentTrust>',
    help=''
)
@utils.add_arg(
    '--platform',
    default=None,
    metvar='<platform>',
    help=''
)
@utils.add_arg(
    '--image-pull-dir',
    default=None,
    metvar='<imagePullDir>',
    help=''
)
@utils.add_arg(
    '--image-pull-yaml-file',
    default=None,
    metvar='<imagePullYamlFile>',
    help=''
)
def do_image_pull( ):
    pass


@utils.add_arg(
    '--registry',
    default=None,
    metvar='<registry>',
    help=''
)
@utils.add_arg(
    '--image-push-dir',
    default=None,
    metvar='<imagePushDir>',
    help=''
)
@utils.add_arg(
    '--image-push-yaml-file',
    default=None,
    metvar='<imagePushYamlFile>',
    help=''
)
def do_image_push():
    pass


@utils.add_arg(
    '--registry',
    default=None,
    metvar='<registry>',
    help=''
)
@utils.add_arg(
    '--image-build-dir',
    default=None,
    metvar='<imagePushDir>',
    help=''
)
@utils.add_arg(
    '--image-build-yaml-file',
    default=None,
    metvar='<imagePushYamlFile>',
    help=''
)
def do_image_build():
    pass
