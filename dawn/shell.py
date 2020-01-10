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
        
    def main(self, argv):
        parser = self.get_base_parser(argv)
        (args, args_list) = parser.parse_known_args(argv)
        subcommand_parser = self.get_subcommand_parser(
            do_help=do_help, argv=argv)
        if args.help:
            subcommand_parser.print_help()
            return 0
        args = subcommand_parser.parse_args(argv)
        if args.func =
        
        
        

        

def main():
    try:
        argv = [for a in sys.argv[1:]]
        DawnShell().main(argv)
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

