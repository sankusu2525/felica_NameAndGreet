# -*- coding: utf-8 -*-

from __future__ import print_function
from ctypes import *

#https://qiita.com/t114/items/819a9cdfe90ea98dd4d3
def functionPasori():
    # libpafe.hの77行目で定義
    FELICA_POLLING_ANY = 0xffff
    libpafe = cdll.LoadLibrary("/usr/local/lib/libpafe.so")

    libpafe.pasori_open.restype = c_void_p
    pasori = libpafe.pasori_open()

    libpafe.pasori_init(pasori)

    libpafe.felica_polling.restype = c_void_p
    felica = libpafe.felica_polling(pasori, FELICA_POLLING_ANY, 0, 0)

    idm = c_ulonglong() #←16桁受けとるために変更
    libpafe.felica_get_idm.restype = c_void_p
    libpafe.felica_get_idm(felica, byref(idm))

    # IDmは16進表記
    print("funcpasori:%016X" % idm.value) #←16桁表示させるために変更

    # READMEより、felica_polling()使用後はfree()を使う
    # なお、freeは自動的にライブラリに入っているもよう
    libpafe.free(felica)

    libpafe.pasori_close(pasori)
    return "%016X" % idm.value

import json

json_open =open('userfile.json','r')
json_load = json.load(json_open)

def idIsName(str):
    ret ="No Registration"
    ret2 =""
    for v in json_load.values():
        if v["number"] == str:
            ret =v["name"]
            ret2 =v["greet"]
            #print(v)
            break
    return ret,ret2

import signal
import time
import subprocess
idI_old=""
if __name__ == "__main__":
#    global idI_old
    while True:
        #print("SC:%f" % (time.time()))
        idI = functionPasori()
        #print("SC:%s" % idI)
        name,greet = idIsName(idI)
        print("SC:%s" % name)

        if idI_old != idI and "0000000000000000" != idI:
            #print(name + "さん")
            args3 = ['./jsay.sh', name+ "さん " +greet]
            cp = subprocess.run(args3)
            print(cp)
            print("Call_vo:%s" % name)
        idI_old =idI
        time.sleep(1)
