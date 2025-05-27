import tkinter as tk
import time

def _0xdeadbeef():
    global _0xb00bface
    if _0xb00bface:
        _0x12345678 = time.time() - _0xcafe1234
        _0xabcdef01 = int(_0x12345678)
        _0xf00baaar = _0xabcdef01 // 3600
        _0xbeefcafe = (_0xabcdef01 % 3600) // 60
        _0xbaadf00d = _0xabcdef01 % 60
        _0xfeedface.config(text=f"{_0xf00baaar:02d}:{_0xbeefcafe:02d}:{_0xbaadf00d:02d}")
    _0xfeedface.after(100, _0xdeadbeef)

def _0xfa5cafe():
    global _0xb00bface, _0xcafe1234
    _0xb00bface = True
    _0xcafe1234 = time.time()
    _0x1234face.config(state=tk.DISABLED)
    _0x5678babe.config(state=tk.NORMAL)
    _0x90abcdef.config(state=tk.NORMAL)

def _0xc0ffee():
    global _0xb00bface
    _0xb00bface = False
    _0x1234face.config(state=tk.NORMAL)
    _0x5678babe.config(state=tk.DISABLED)

def _0xbadc0ffe():
    global _0xb00bface
    _0xb00bface = False
    _0xfeedface.config(text="00:00:00")
    _0x1234face.config(state=tk.NORMAL)
    _0x5678babe.config(state=tk.DISABLED)
    _0x90abcdef.config(state=tk.DISABLED)

_0xroot = tk.Tk()
_0xroot.title("Time Utility")
_0xb00bface = False
_0xcafe1234 = 0

_0xfeedface = tk.Label(_0xroot, text="00:00:00", font=("Arial", 40))
_0xfeedface.pack(pady=20)

_0x1234face = tk.Button(_0xroot, text="Start", command=_0xfa5cafe, width=10)
_0x1234face.pack(side=tk.LEFT, padx=5)

_0x5678babe = tk.Button(_0xroot, text="Stop", command=_0xc0ffee, width=10, state=tk.DISABLED)
_0x5678babe.pack(side=tk.LEFT, padx=5)

_0x90abcdef = tk.Button(_0xroot, text="Reset", command=_0xbadc0ffe, width=10, state=tk.DISABLED)
_0x90abcdef.pack(side=tk.LEFT, padx=5)

def _0x2b84cafe():
    _0xnow = time.strftime("%H:%M:%S")
    _0xcurrent_time_label.config(text=_0xnow)
    _0xcurrent_time_label.after(1000, _0x2b84cafe)

_0xcurrent_time_label = tk.Label(_0xroot, text="", font=("Arial", 15))
_0xcurrent_time_label.pack(pady=10)
_0x2b84cafe()

_0xdeadbeef()
_0xroot.mainloop()
