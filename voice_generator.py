# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:30:16 2020

@author: tsutitire
"""
import subprocess
import re
import os

rep1 = ["DONDOKODON","w"]
rep2 = ["どんどこどん","わら"]

path = os.getcwd().replace('\\','/')
# remove_custom_emoji
# 絵文字IDは読み上げない
def remove_custom_emoji(text):
    pattern = r'<:[a-zA-Z0-9_]+:[0-9]+>'    # カスタム絵文字のパターン
    return re.sub(pattern,'',text)   # 置換処理

# urlAbb
# URLなら省略
def urlAbb(text):
    pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    return re.sub(pattern,'URLは省略',text)   # 置換処理
def urlabb2(text):
    pattern = "http?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    return re.sub(pattern,'URLは省略',text)   # 置換処理
def mention(text):   
    pattern = "@![0123456789]+"
    return re.sub(pattern,'メンションは置換されました',text)   # 置換処理
def replace(text,text2,text3):
    return text.replace(text2,text3)
# creat_WAV
# message.contentをテキストファイルに書き込み
def creat_WAV(inputText,ids):
        # message.contentをテキストファイルに書き込み

    inputText = remove_custom_emoji(inputText)   # 絵文字IDは読み上げない
    inputText = urlAbb(inputText)   # URLなら省略
    inputText = urlabb2(inputText)
    inputText = mention(inputText)
    for i in range(len(rep1)):
        inputText = replace(inputText,rep1[i],rep2[i])
    input_file = 'files/input.txt'

    with open(input_file,'w',encoding='shift_jis') as file:
        file.write(inputText)

    command = path + '/open_jtalk' + ' -x {x} -m {m} -r {r} -ow {ow} {input_file}'
    
    #辞書のPath
    x = path + '/apps/dic'
    m = path + '/apps/mei/mei_happy.htsvoice'
    m1 = path + '/apps/mei/mei_happy.htsvoice'
    m2 = path + '/apps/mei/mei_angry.htsvoice'
    m3 = path + '/apps/mei/mei_bashful.htsvoice'
    m4 = path + '/apps/mei/mei_normal.htsvoice'
    m5 = path + '/apps/mei/mei_sad.htsvoice'
    #m5 = path + '/futures/cmu_us_arctic_slt.htsvoice'
    
    input_file = 'files/userdata-v.txt'
    with open(input_file,'r',encoding='utf-8') as file:
        lists = file.read()
    listu = lists.split()
    
    if str(ids) in listu:
        index = listu.index(str(ids))
        print(listu[index + 1])
        if listu[index + 1] == "1":
            m = m1
        if listu[index + 1] == "2":
            m = m2
        if listu[index + 1] == "3":
            m = m3
        if listu[index + 1] == "4":
            m = m4
        if listu[index + 1] == "5":
            m = m5
    
    
    input_file = 'files/input.txt'
    
    
    #発声のスピード
    r = '1.0'

    #音量
    g = '10.0'
    
    #出力ファイル名　and　Path
    ow = 'files/output.wav'

    args= {'x':x, 'm':m, 'r':r, 'ow':ow, 'g':g, 'input_file':input_file}

    cmd= command.format(**args)
    print(cmd)

    subprocess.run(cmd)
    return True

if __name__ == '__main__':
    creat_WAV('テスト')