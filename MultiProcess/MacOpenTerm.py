import subprocess
import sys
import pathlib
import platform

if platform.system() == "Darwin":
    import osascript

TEST = 98

if TEST == 0:
    print(pathlib.Path().absolute())
    for p in sys.path:
        print(p)

if TEST == 1:
    process = subprocess.Popen(["grep", "hello"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.stdin.write(b"hello\nhello world\nhella")
    print(process.communicate()[0])
    process.stdin.close()

if TEST == 2:
    try:
        output = subprocess.check_output(["open", "-F", "-a", "Terminal"])
        print(output)
    except subprocess.CalledProcessError:
        pass

my_tail = "/Users/louislietaer/conf.py"
code, out, err = osascript.run('tell application "Terminal" to do script "tail -n 1000 -f ' + my_tail + '"')

print(code,"+", out,"+", err)
with open(my_tail, "a") as my_file:
    my_file.write("#appended 2nd text\n")

input('yes')
with open(my_tail, "a") as my_file:
    my_file.write("#appended 3nd text\n")

