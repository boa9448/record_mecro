from ctypes import c_char_p, windll, c_int32

from input_base import KeyState, MouseButton, MouseState


class ClassDD:
    def __del__(self) -> None:
        """FreeLibrary = windll.kernel32["FreeLibrary"]
        FreeLibrary.argtypes = (wintypes.HMODULE,)
        FreeLibrary(self._hModule._handle)"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(ClassDD, cls).__new__(cls)
            cls._instance.init(*args, **kwargs)
        return cls._instance

    def init(self, dll_path : str) -> None:
        #dd 라이브러리를 불러옴
        self._hModule = windll.LoadLibrary(dll_path)
        self._DD_key = self._hModule["DD_key"] #DD_key(DD키코드, 키상태)
        self._DD_key.argtypes = (c_int32, c_int32)
        self._DD_key.restype = c_int32

        self._DD_btn = self._hModule["DD_btn"] #DD_btn(DD클릭 코드)
        self._DD_btn.argtypes = (c_int32,)
        self._DD_btn.restype = c_int32

        self._DD_mov = self._hModule["DD_mov"] #DD_mov(x, y) *** 다중 모니터에선 dd자체 버그가 일어남 ***
        self._DD_mov.argtypes = (c_int32, c_int32)
        self._DD_mov.restype = c_int32

        self._DD_movR = self._hModule["DD_movR"] #DD_movR(상대 x, 상대 y) 지금 마우스의 위치에서 상대적으로 움직임
        self._DD_movR.argtypes = (c_int32, c_int32)
        self._DD_movR.restype = c_int32

        self._DD_whl = self._hModule["DD_whl"] #마우스 휠
        self._DD_whl.argtypes = (c_int32,)
        self._DD_whl.restype = c_int32

        self._DD_todc = self._hModule["DD_todc"] #ddCode = DD_todc(가상키코드) 가상키코드 -> DD코드로 변경
        self._DD_todc.argtypes = (c_int32,)
        self._DD_todc.restype = c_int32

        self._DD_str = self._hModule["DD_str"] #DD_str(입력할 문자열) 문자열은 영어 숫자로만 입력, 대부분의 경우 사용x
        self._DD_str.argtypes = (c_char_p,)
        self._DD_str.restype = c_int32

    def key(self, vk : int, status : KeyState) -> None:
        self._DD_key(self._DD_todc(vk), status)

    def key_press(self, vk : int) -> None:
        self.key(vk, KeyState.PRESS)

    def key_release(self, vk : int) -> None:
        self.key(vk, KeyState.RELEASE)

    def btn(self, code : MouseButton, status : MouseState) -> None:
        self._DD_btn(code << status)

    def btn_press(self, button_code : MouseButton) -> None:
        self.btn(button_code, MouseState.PRESS)

    def btn_release(self, button_code : MouseButton) -> None:
        self.btn(button_code, MouseState.RELEASE)

    def move(self, x: int, y: int, relative: bool) -> None:
        if not relative:
            self._DD_mov(x, y)
        else:
            self._DD_movR(x, y)