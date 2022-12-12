import os
import sys

cur_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(cur_dir)
src_dir = os.path.join(root_dir, 'src')
dll_path = os.path.join(src_dir, "3rdparty", "DD64.dll")

sys.path.append(root_dir)
sys.path.append(src_dir)

#모듈 가져오기
from src.recorder import Recorder, Runner, RecordType, KeyState, MouseState, MouseButton
from src.class_dd import ClassDD


key_mouse_record = [] #키보드 마우스 정보가 저장될 리스트

#키보드 이벤트가 발생하면 호출되는 함수
def on_press_release(data : tuple[RecordType, str, int, KeyState, float]) -> bool | None:
    record_type, name, vk, state, event_time = data
    print("on_press_release", record_type, name, vk, state, event_time)

    if name == "f1" and state == KeyState.PRESS:
        return False

    key_mouse_record.append(data)


#마우스 이벤트가 발생하면 호출되는 함수
def on_click(data : tuple[RecordType, int, int, MouseButton, MouseState, float]) -> bool | None:
    record_type, x, y, button, state, event_time = data
    print("on_click", record_type, x, y, button, state, event_time)

    key_mouse_record.append(data)


#키보드, 마우스 이벤트를 받아들이는 객체 생성
recorder = Recorder(on_press_release, on_click)
recorder.start()
recorder.join()

#필요시 파일로 저장
Recorder.save_record(key_mouse_record, "key_mouse_record.json")
#필요시 파일에서 불러오기
key_mouse_record = Recorder.load_record("key_mouse_record.json")


#classDD 객체 생성
dd = ClassDD(dll_path)

#키보드, 마우스 이벤트를 실행시키는 객체 생성
runner = Runner(dd)
runner.add_record(key_mouse_record)
runner.set_random_delay(0.02, 0.05)
runner.start()
runner.join()
runner.exit()