from fs.memoryfs import MemoryFS
from fs.expose import fuse
from os import system
mem_fs = MemoryFS()
mnt_pt = fuse.mount("mem_fs", "/home/todor/workspace/myRam/tst", True, True, True)
system("unzip sublime.zip -d /home/todor/workspace/myRam/tst/")
system("chown -R todor /home/todor/workspace/myRam/tst")
system("chmod -r 775 /home/todor/workspace/myRam/tst")
system("./home/todor/workspace/myRam/tst/sublime_text")