
import enum
from ctypes import windll, wintypes
from typing import Callable, Union


user32 = windll.user32
kernel32 = windll.kernel32

RegisterHotKey = user32["RegisterHotKey"]
RegisterHotKey.argtypes = (wintypes.HWND, wintypes.INT, wintypes.UINT, wintypes.UINT)
RegisterHotKey.restype = wintypes.BOOL

UnregisterHotKey = user32["UnregisterHotKey"]
UnregisterHotKey.argtypes = (wintypes.HWND, wintypes.INT)
UnregisterHotKey.restype = wintypes.BOOL

GetLastError = kernel32["GetLastError"]
GetLastError.argtypes = tuple()
GetLastError.restype = wintypes.DWORD

WM_HOTKEY = 0x0312
VK_OEM_5 = 0xDC
VK_OEM_PLUS = 0xBB


class ModFilter(enum.IntFlag):
    MOD_NONE        = 0x0000
    MOD_ALT         = 0x0001
    MOD_CONTROL     = 0x0002
    MOD_NOREPEAT    = 0x4000
    MOD_SHIFT       = 0x0004
    MOD_WIN         = 0x0008


def register_hotkey(window_handle : int, id_ : int, vk : int, filter : ModFilter = ModFilter.MOD_NONE) -> bool:
    success = RegisterHotKey(window_handle, id_, filter, vk)
    return bool(success)


def unregister_hotkey(window_handle : int, id_ : int) -> bool:
    success = UnregisterHotKey(window_handle, id_)
    return bool(success)