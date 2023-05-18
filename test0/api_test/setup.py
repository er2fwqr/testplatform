import sys
from cx_Freeze import setup, Executable

# 判断操作系统
if sys.platform == 'win32':
    base = 'Win32GUI'

build_exe_options = {
    'packages': ['unittest', 'html_test_runner'],  # 需要包含的Python包
}

# 执行文件路径和名称
executable = [Executable('main.py', base=base)]

setup(
    name='ApiTest',  # 打包后的程序名称
    version='1.0',  # 程序版本号
    description='Test Program',  # 程序描述
    options={
        'build_exe': build_exe_options,
    },
    executables=executable,
)
