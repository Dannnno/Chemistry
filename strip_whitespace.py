import os
import io


four = '    '
two = '  '
_filetypes = ['py']
_visited = []


def get_files(dir_name=None):
    if dir_name is None:
        dir_name = os.path.dirname(os.path.abspath(__file__))
    for file_ in os.listdir(dir_name):
        if not file_.startswith('.'):
            if os.path.isdir(os.path.join(dir_name, file_)):
                for p in get_files(os.path.join(dir_name, file_)):
                    yield p
            else:
                f, _, suffix = file_.partition('.')
                if suffix in _filetypes and f not in _visited:
                    _visited.append(f)
                    yield os.path.join(dir_name, file_)


def clean_file(filename, size):
    if os.path.exists(filename) and not os.path.isdir(filename):
        with io.open(filename, mode='r', buffering=1) as f:
            file_ = []
            for line in f:
                file_.append(line.replace('\t', size).rstrip())

            for line in reversed(file_):
                if not line:
                    file_.pop(-1)
                else:
                    break

        with io.open(filename, mode='w') as f:
            f.write('\n'.join(file_))
            f.write(unicode('\n'))


def strip_whitespace(size=four):
    for file_ in get_files():
        clean_file(file_, size)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
                        description="Cleans up the whitespace of files")
    parser.add_argument('-f', '--filetypes', metavar='f', nargs='+', default=[],
                        help="file extensions of filetypes to be cleaned")
    parser.add_argument(
            '-s', '--size', default=four, action='store_const', const=two,
            help='Use if you want tabs replaced by 2 spaces not 4')

    args = parser.parse_args()
    if args.filetypes:
        _filetypes.extend(args.filetypes)
    strip_whitespace(size=args.size)
