import sys, time, os, subprocess, zlib, re
"""
Find git in possible path
"""
def git_detect():
    git_path_vars = ["git",
                    "c:\\cygwin\\git",
                    "c:\\cygwin64\\bin\\git",
                    "c:\\Program Files (x86)\\Git\\bin\\git",
                    "c:\\Program Files\\Git\\bin\\git"]
    git_path = None
    for g in git_path_vars:
        try:
            subprocess.call([g, '--version'])
            git_path = g
            print("Found git at: {}".format(git_path))
            break
        except OSError:
            pass
    if not git_path:
        sys.exit("Git not found. Please install it (http://git-scm.com/ or cygwin: \"apt-cyg install git\" or in other way)")
    return git_path
""
def count_sources_crc(file_types, ignore_lines):
    crc = 0
    for root, _, files in os.walk('.'):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in file_types:
                full_path = os.path.join(root, file)
                #print("Include in crc {}".format(full_path))
                for line in open(full_path).readlines():
                    ignore = False
                    for pat in ignore_lines:
                        if re.match(pat, line):
                            ignore = True
                            #print("Ignore line: {}".format(line))
                            break
                    if not ignore:
                        crc = zlib.crc32(bytes(line, 'UTF-8'), crc)
    return (crc & 0xFFFFFFFF)
def create_version_file(filename):
    git_path = git_detect()
    crc = count_sources_crc(['.py',],
                            ['COMMIT_REVISION = .+',
                             'COMMIT_HASH = .+',
                             'SOURCES_CRC = .+',
                             'BUILD_TIME = .+'])
    f = open(filename, 'w+')
    repo_rev = os.popen("\"{}\" rev-list --count HEAD".format(git_path)).read()[:8].rstrip()
    f.write("COMMIT_REVISION = {}\n\n".format(repo_rev))
    repo_hash = os.popen("\"{}\" rev-parse HEAD".format(git_path)).read()[:8].rstrip()
    f.write("COMMIT_HASH = 0x{}\n\n".format(repo_hash))
    f.write("SOURCES_CRC = 0x{:08x}\n\n".format(crc))
    f.write("BUILD_TIME = {}\n\n".format(time.time()))
    f.close()

if __name__ == '__main__':
    create_version_file("C:\\Python\\Repositories\\Robot\\version.txt")