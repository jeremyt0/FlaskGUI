from threading import Thread
import sys
from cefpython3 import cefpython as cef
import win32gui, win32con
import os

class GUIWindow(Thread):

    def init(self):
        super().__init__()
        # self.port = port

    def run(self):
        sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
        cef.Initialize()
        cef.CreateBrowserSync(url="http://localhost:2040",
                              window_title="My Application"
                              )
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    
        cef.MessageLoop()
    
        cef.Shutdown()
    
        os._exit(0)  # Exit program
