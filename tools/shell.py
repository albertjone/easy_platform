import argparse
import encodeutils
import sys


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
        
    def get_config_parser(self, argv):
        parser = DawnArgumentParser(
            prog='dawn',
            description=__doc__.strip(),
            epilog='See "dawn help COMMAND" '
                   'for help on a specific command.',
            app_help=False,
            formatter_class=DawnHelpFormatter,
        )
        parser.add_argument(
            '--docker-build-dir',
            action='')
        
    def main(self, argv):
        parser = self.get_config_parser(argv)
        parser.
        
        

def main():
    try:
        argv = [for a in sys.argv[1:]]
        DawnShell().main(argv)
    except Exception as  exc:
        print(exc)
    except KeyboardInterrupt:
        print("...terminating dawn client", file=sys.stdout)
        sys.exit(130)
