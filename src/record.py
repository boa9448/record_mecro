import time
import json
import random
from typing import Callable
from threading import Thread, Event

from pynput import keyboard, mouse

from input_base import RecordType, KeyState, MouseButton, MouseState
from class_dd import ClassDD


class Recorder:
    def __init__(self, on_press_release_handler, on_click_handler) -> None:
        self.user_on_press_release_handler = on_press_release_handler
        self.user_on_click_handler = on_click_handler

        self.key_listener = keyboard.Listener(on_press = lambda key : self.on_press_release_handler(key, KeyState.PRESS)
                                            , on_release = lambda key : self.on_press_release_handler(key, KeyState.RELEASE))
        self.mouse_listener = mouse.Listener(on_click = self.on_click_handler)
                                            #, on_move = self.on_mouse_scroll_handler)

    def start(self) -> None:
        self.last_time = None

        self.key_listener.start()
        self.mouse_listener.start()

    def stop(self) -> None:
        self.key_listener.stop()
        self.mouse_listener.stop()

    def join(self) -> None:
        self.key_listener.join()

    def get_delay(self) -> float:
        if self.last_time is None:
            self.last_time = time.time()
            return 0
        else:
            cur_time = time.time()
            delay = cur_time - self.last_time
            self.last_time = cur_time
            return delay

    def on_press_release_handler(self, key : keyboard.Key | keyboard.KeyCode
                                    , state : KeyState) -> bool | None:
        key_name = getattr(key, "char", None) or getattr(key, "name", None)
        key_vk = getattr(key, "vk", None)
        if key_vk is None:
            key_vk = key.value.vk

        delay = self.get_delay()
        return self.user_on_press_release_handler((RecordType.KEYBOARD, key_name, key_vk, state, delay))

    def on_click_handler(self, x : int, y : int, button : str, pressed : bool) -> bool | None:
        state = MouseState.PRESS if pressed else MouseState.RELEASE
        button_code = MouseButton.from_string(button.name)
        
        delay = self.get_delay()
        return self.user_on_click_handler((RecordType.MOUSE, x, y, button_code, state, delay))

    @staticmethod
    def save_record(record_list : list[tuple], file_path : str) -> None:
        with open(file_path, "w") as f:
            json.dump(record_list, f, indent = 4)

    @staticmethod
    def load_record(file_path : str) -> list[tuple]:
        with open(file_path, "r") as f:
            record_list = json.loads(f.read())

            converted_record_list = []
            for item in record_list:
                record_type, *args = item

                if record_type == RecordType.KEYBOARD:
                    key_name, key_vk, state, delay = args
                    converted_record_list.append((RecordType.KEYBOARD
                                                , key_name
                                                , key_vk
                                                , KeyState(state)
                                                , delay))

                elif record_type == RecordType.MOUSE:
                    x, y, button, state, delay = args
                    converted_record_list.append((RecordType.MOUSE
                                                , x
                                                , y
                                                , MouseButton(button)
                                                , MouseState(state)
                                                , delay))

            return converted_record_list


class Runner:
    def __init__(self, dd_obj : ClassDD
                    , record_list : list[tuple]
                    , random_delay_min_max : tuple[float, float] | None = None) -> None:
        self.dd = dd_obj
        self.record_list = record_list
        self.random_delay_min_max = random_delay_min_max

        if random_delay_min_max is None:
            self.random_delay = lambda : 0
        else:
            min_delay, max_delay = random_delay_min_max
            self.random_delay = lambda : random.uniform(min_delay, max_delay)

        self.record_thread = None
        self.exit_event = Event()
        self.end_callback = None

    def start(self) -> None:
        if self.record_thread is not None:
            self.exit_event.set()
            self.record_thread.join()

        self.exit_event.clear()
        self.record_thread = Thread(target = self.work)
        self.record_thread.start()

    def stop(self) -> None:
        if self.record_thread is not None:
            self.exit_event.set()
            self.record_thread.join()

    def sleep(self, delay : float) -> None:
        self.exit_event.wait(delay)

    def work(self) -> None:
        for record in self.record_list:
            if self.exit_event.is_set():
                break

            record_type, *args = record

            if record_type == RecordType.KEYBOARD:
                key_name, key_vk, state, delay = args
                self.dd.key(key_vk, state)
                self.sleep(delay + self.random_delay())

            elif record_type == RecordType.MOUSE:
                x, y, button, state, delay = args
                self.dd.move(x, y, False)
                self.dd.btn(button, state)
                self.sleep(delay + self.random_delay())

        if self.end_callback is not None:
            self.end_callback()