from distutils.core import setup
import py2exe

from distutils.filelist import findall
import matplotlib

setup(
    console=['PlotMemInfo.py'],

    options={
        'py2exe': {
            'packages': ['matplotlib'],
            'dll_excludes': ['libgdk-win32-2.0-0.dll',
                             'libgobject-2.0-0.dll',
                             'libgdk_pixbuf-2.0-0.dll']
        }
    },
    data_files=matplotlib.get_py2exe_datafiles()
)