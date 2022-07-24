# -*- mode: python -*-

# The below line may be necessary to run prior to building for the cefpython import.
# This appears to be unnecessary, but I'm leaving it in just in case we come up
# against problems later.
# set PATH=%PATH%;C:\Windows\System32\downlevel;
path_update = "C:\\Windows\\System32\\downlevel;"
import os
os.environ["PATH"] += os.pathsep + path_update

# Command to run
# python -m PyInstaller --debug all __main__.spec


block_cipher = None
name_app = "MyApplication"

a = Analysis(['..\\application\\main.py'],
             binaries=[],
             datas=[('..\\application\\interface\\static', 'interface\\static'),
                    ('..\\application\\interface\\templates', 'interface\\templates')
                   ],
             hiddenimports=['pywt._extensions._cwt'],
             # additional_hooks_dir=[''],
             hookspath=['.'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name=name_app,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          icon='..\\application\\interface\\static\\tea.ico',
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=name_app)
