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
        self.key_listener.start()
        self.mouse_listener.start()

    def stop(self) -> None:
        self.key_listener.stop()
        self.mouse_listener.stop()

    def join(self) -> None:
        self.key_listener.join()

    def on_press_release_handler(self, key : keyboard.Key | keyboard.KeyCode
                                    , state : KeyState) -> bool | None:
        key_name = getattr(key, "char", None) or getattr(key, "name", None)
        key_vk = getattr(key, "vk", None)
        if key_vk is None:
            key_vk = key.value.vk

        event_time = time.time()
        return self.user_on_press_release_handler((RecordType.KEYBOARD, key_name, key_vk, state, event_time))

    def on_click_handler(self, x : int, y : int, button : str, pressed : bool) -> bool | None:
        state = MouseState.PRESS if pressed else MouseState.RELEASE
        button_code = MouseButton.from_string(button.name)
        
        event_time = time.time()
        return self.user_on_click_handler((RecordType.MOUSE, x, y, button_code, state, event_time))

    @staticmethod
    def save_record(record : list[tuple], file_path : str) -> None:
        with open(file_path, "w") as f:
            json.dump(record, f, indent = 4)

    @staticmethod
    def load_record(file_path : str) -> list[tuple]:
        with open(file_path, "r") as f:
            record = json.loads(f.read())

            converted_record = []
            for item in record:
                record_type, *args = item

                if record_type == RecordType.KEYBOARD:
                    key_name, key_vk, state, event_time = args
                    converted_record.append((RecordType.KEYBOARD
                                                , key_name
                                                , key_vk
                                                , KeyState(state)
                                                , event_time))

                elif record_type == RecordType.MOUSE:
                    x, y, button, state, event_time = args
                    converted_record.append((RecordType.MOUSE
                                                , x
                                                , y
                                                , MouseButton(button)
                                                , MouseState(state)
                                                , event_time))

            return converted_record


class Runner:
    def __init__(self, dd_obj : ClassDD) -> None:
        self.dd = dd_obj
        self.record_list = []
        self.random_delay_min_max = None

        self.random_delay = lambda : 0

        self.record_thread = None
        self.exit_event = Event()
        self.end_callback = None

    def add_record(self, record : list[tuple]) -> None:
        self.record_list.append(record)

    def add_record_list(self, record_list : list[list[tuple]]) -> None:
        for record in record_list:
            self.add_record(record)

    def clear_record(self) -> None:
        self.record_list.clear()

    def set_random_delay(self, min_delay : float, max_delay : float) -> None:
        if min_delay == 0 and max_delay == 0:
            self.random_delay = lambda : 0
            return

        if min_delay > max_delay:
            min_delay, max_delay = max_delay, min_delay

        self.random_delay_min_max = (min_delay, max_delay)
        self.random_delay = lambda : random.uniform(min_delay, max_delay)

    def set_end_callback(self, callback : Callable) -> None:
        self.end_callback = callback

    def start(self) -> None:
        if self.record_thread is not None:
            self.exit_event.set()
            self.record_thread.join()

        self.exit_event.clear()
        self.record_thread = Thread(target = self.run)
        self.record_thread.start()

    def exit(self) -> None:
        if self.record_thread is not None:
            self.exit_event.set()
            self.record_thread.join()

    def join(self) -> None:
        if self.record_thread is not None:
            self.record_thread.join()

    def is_exit(self) -> bool:
        return self.exit_event.is_set()

    def sleep(self, delay : float) -> None:
        self.exit_event.wait(delay)

    def run(self) -> None:
        record_list = self.record_list.copy()
        for record in record_list:
            if self.is_exit():
                break

            self.run_record(record)

        if self.end_callback is not None:
            self.end_callback()

    def run_record(self, record : list[tuple]) -> None:
        record = self.event_time_to_delay(record)
        for item in record:
            if self.is_exit():
                break

            record_type, *args = item

            if record_type == RecordType.KEYBOARD:
                key_name, key_vk, state, delay = args
                self.dd.key(key_vk, state)
                self.sleep(delay + self.random_delay())

            elif record_type == RecordType.MOUSE:
                x, y, button, state, delay = args
                self.dd.move(x, y, False)
                self.dd.btn(button, state)
                self.sleep(delay + self.random_delay())

    def event_time_to_delay(self, record : list[tuple]) -> list[tuple]:
        new_record = []
        count = len(record)

        for idx in range(count):
            *cur_args, cur_event_time = record[idx]
            if idx == count - 1:
                new_record.append((*cur_args, 0))
                break

            *next_args, next_event_time = record[idx + 1]

            delay = next_event_time - cur_event_time
            new_record.append((*cur_args, delay))

        return new_record