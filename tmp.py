# 语音播报模块
import pyttsx3
import sys
import time
engine = pyttsx3.init()

while True:
    # 语音播报内容
    print("-----")
    lines = sys.stdin.readlines()
    # 输出文件格式
    outFile = 'out.aiff'
    # 设置要播报的Unicode字符串
    for i in lines:
        if i == "+?10":
            time.sleep(10)
            continue
        elif i == "+?5":
            time.sleep(5)
            continue
        elif i == "+?1":
            time.sleep(1)
            continue
        engine.say(i)
        # 等待语音播报完毕
        engine.runAndWait()
    # 将文件转换为mp3格式
    # AudioSegment.from_file(outFile).export("Python.mp3", format="mp3")
    break
