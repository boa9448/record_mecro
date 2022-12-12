pyinstaller src\main.py ^
--uac-admin ^
--add-data "src\3rdparty;3rdparty" ^
--add-data "src\translations;translations" ^
--name "record_macro_demo.exe" ^
--windowed ^
--onefile