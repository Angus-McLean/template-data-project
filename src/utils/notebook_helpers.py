#@title Create Cell Magic writefile_and_run
from IPython.core import magic_arguments
from IPython.core.magic import register_cell_magic

import sys, os

@magic_arguments.magic_arguments()
@magic_arguments.argument(
    '-a', '--append', action='store_true', default=False,
    help='Append contents of the cell to an existing file. '
          'The file will be created if it does not exist.'
)
@magic_arguments.argument(
    'filename', type=str,
    help='file to write'
)
@register_cell_magic
def writefile_and_run(line, cell):
    """Write the contents of the cell to a file.
    
    The file will be overwritten unless the -a (--append) flag is specified.
    """
    args = magic_arguments.parse_argstring(writefile_and_run, line)
    filename = os.path.expanduser(args.filename)

    if os.path.exists(filename):
        if args.append:
            print("Appending to %s" % filename)
        else:
            print("Overwriting %s" % filename)
    else:
        print("Writing %s" % filename)
    
    mode = 'a' if args.append else 'w'
    # print(filename, mode, 'utf-8', cell)
    with open(filename, mode, encoding='utf-8') as f:
        f.write(cell+"\n\n")

    code = compile(cell, line, 'exec')
    exec(code, globals())