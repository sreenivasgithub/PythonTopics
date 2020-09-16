"""
'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', 'closerange',
'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2',
'environ', 'errno', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv',
'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode',
'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable',
'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin',
'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek',
'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep',
'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs',
'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep',
'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv',
'spawnve', 'st', 'startfile', 'stat', 'stat_float_times', 'stat_result',
'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd',
'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink',
'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask',
'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write'
"""

# Manipulating directories:
# os.mkdir('dirName'):  it will create a directory in your current directory
# os.makedirs('dirName/subdir'): it will create a dir and subdir at a time
# os.getcwd():          returns current working directory path
# os.listdir():         returns a list os directories in your current dir
# os.chdir('choosedir') : it will change your current dir
# os.rmdir('choosedir') : 1.removes your dir, 2.when you tried to delete the
#                         Parent directory which was having one more directory
#                         in it,it gives error “Directory not empty“
# os.removedirs('chooseParentdir'): it removes your parent dir also
# os.rename('dirname', 'dirrename'):  rename
# os.stat('fileName or dirName'): There is many things in the result,but we will
#                      focus on st_size,st_mtime. st_size is size of file in bytes
#                      and st_ctime is last modification time
# os.path.exists(folder/insideFolder): returns True if it is present, else False
# os.path.isfile(folder/insideFolder/a.txt):returns True if it is present, else False
# os.path.isdir(folder/insideFolder): returns True if it is present, else False
# os.path.abspath('a.txt'): returns absolute path of a file or a folder
# os.path.basename(folder/insideFolder/a.txt): returns base(last) file or a folder
# os.path.join(os.getcwd(), 'dirname'):
# os.walk():