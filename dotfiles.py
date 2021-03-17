import os.path

filenames = {
    'screenrc': '/home/arjuna/.screenrc',
    'vimrc': '/home/arjuna/.config/nvim/init.vim'
}

def find_dotfile(dotfile_name):
    if filenames.__contains__(dotfile_name):
        path = filenames[dotfile_name]
    else:
        path = '/home/arjuna/.%s' % dotfile_name

    try:
        return open(path).read()
    except IOError:
        return ''

print(repr(find_dotfile('screenrc')))
print(repr(find_dotfile('foobar')))

