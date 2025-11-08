#!/usr/bin/env python3
import platform
import sys
import os
import socket
import struct
import locale
import getpass
import tempfile
import sysconfig
from pathlib import Path

print("=" * 70)
print("PYTHON PLATFORM INFORMATION COLLECTOR")
print("=" * 70)

# Python Interpreter Information
print("\n### PYTHON INTERPRETER ###")
print(f"Python Version: {sys.version}")
print(f"Python Version (short): {platform.python_version()}")
print(f"Python Implementation: {platform.python_implementation()}")
print(f"Python Build: {platform.python_build()}")
print(f"Python Compiler: {platform.python_compiler()}")
print(f"Python Branch: {platform.python_branch()}")
print(f"Python Revision: {platform.python_revision()}")
print(f"Executable Path: {sys.executable}")
print(f"Prefix: {sys.prefix}")
print(f"Base Prefix: {sys.base_prefix}")
print(f"Exec Prefix: {sys.exec_prefix}")
print(f"Platform String: {sys.platform}")
print(f"API Version: {sys.api_version}")
print(f"Max Unicode: {sys.maxunicode}")
print(f"Max Size: {sys.maxsize}")
print(f"Byte Order: {sys.byteorder}")
print(f"Default Encoding: {sys.getdefaultencoding()}")
print(f"Filesystem Encoding: {sys.getfilesystemencoding()}")

# Operating System Information
print("\n### OPERATING SYSTEM ###")
print(f"System: {platform.system()}")
print(f"Release: {platform.release()}")
print(f"Version: {platform.version()}")
print(f"Platform: {platform.platform()}")
print(f"OS Name: {os.name}")
if hasattr(os, 'uname'):
    uname = os.uname()
    print(f"Uname sysname: {uname.sysname}")
    print(f"Uname nodename: {uname.nodename}")
    print(f"Uname release: {uname.release}")
    print(f"Uname version: {uname.version}")
    print(f"Uname machine: {uname.machine}")

# Hardware Information
print("\n### HARDWARE ###")
print(f"Machine Type: {platform.machine()}")
print(f"Processor: {platform.processor()}")
print(f"Architecture: {platform.architecture()}")
print(f"CPU Count: {os.cpu_count()}")
print(f"Pointer Size: {struct.calcsize('P') * 8} bits")

# Network Information
print("\n### NETWORK ###")
print(f"Hostname: {socket.gethostname()}")
print(f"Platform Node: {platform.node()}")
try:
    print(f"FQDN: {socket.getfqdn()}")
    print(f"IP Address(es): {socket.gethostbyname_ex(socket.gethostname())[2]}")
except:
    print("Could not retrieve full network info")

# User and Locale Information
print("\n### USER & LOCALE ###")
print(f"User: {getpass.getuser()}")
print(f"Current Working Directory: {os.getcwd()}")
print(f"Home Directory: {Path.home()}")
print(f"Temp Directory: {tempfile.gettempdir()}")
print(f"Locale: {locale.getlocale()}")
print(f"Default Locale: {locale.getdefaultlocale()}")
print(f"Preferred Encoding: {locale.getpreferredencoding()}")

# Process Information
print("\n### PROCESS ###")
print(f"Process ID: {os.getpid()}")
if hasattr(os, 'getppid'):
    print(f"Parent Process ID: {os.getppid()}")
if hasattr(os, 'getuid'):
    print(f"User ID: {os.getuid()}")
    print(f"Effective User ID: {os.geteuid()}")
if hasattr(os, 'getgid'):
    print(f"Group ID: {os.getgid()}")
    print(f"Effective Group ID: {os.getegid()}")
if hasattr(os, 'getgroups'):
    print(f"Group IDs: {os.getgroups()}")

# Environment Variables
print("\n### ENVIRONMENT VARIABLES ###")
important_vars = ['PATH', 'HOME', 'USER', 'SHELL', 'LANG', 'PYTHONPATH',
                  'VIRTUAL_ENV', 'TERM', 'EDITOR', 'PWD']
for var in important_vars:
    value = os.environ.get(var)
    if value:
        # Truncate PATH as it can be very long
        if var == 'PATH':
            print(f"{var}: {value[:100]}...")
        else:
            print(f"{var}: {value}")

print(f"\nTotal Environment Variables: {len(os.environ)}")

# Python Configuration
print("\n### PYTHON CONFIGURATION ###")
print(f"Config Var Platform: {sysconfig.get_platform()}")
print(f"Python Path: {sysconfig.get_path('stdlib')}")
paths = sysconfig.get_paths()
print(f"Site-packages: {paths.get('purelib')}")

# System Path
print("\n### PYTHON SYSTEM PATH ###")
for i, path in enumerate(sys.path[:10]):
    print(f"{i}: {path}")
if len(sys.path) > 10:
    print(f"... and {len(sys.path) - 10} more paths")

print("\n" + "=" * 70)
print("END OF REPORT")
print("=" * 70)
