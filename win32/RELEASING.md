Releasing a New Windows Installer
=================================

* Install the latest 32-bit Python 3.4.x
* Install dependencies with PIP

```
cd C:\Python34\Scripts
pip3 install cx_Freeze
pip3 install pypiwin32
```

* Install PyGObject all-in-one for Windows (pygi-aio)
    - GTK+ and GIR
* Install Inno Setup
* Test, build, test build

```
set PATH=C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem
C:\Python34\python.exe bin\nfoview
win32\build.bat
win32\test-build.bat
# If needed, enable a console window to see output:
# winsetup.py: s/base="Win32GUI"/base=None/
```

* Update version numbers in `win32/nfoview.iss` and compile with Inno Setup
* Install NFO Viewer and check that it works
