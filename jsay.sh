#!/bin/bash
TMP=/tmp/jsay2.wav
#JTALK_Path=/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice
#JTALK_Path=/usr/share/hts-voice/mei/mei_angry.htsvoice
JTALK_Path=/usr/share/hts-voice/mei/mei_happy.htsvoice
#JTALK_Path=/usr/share/hts-voice/mei/mei_sad.htsvoice
#JTALK_Path=/usr/share/hts-voice/mei/mei_bashful.htsvoice
#JTALK_Path=/usr/share/hts-voice/mei/mei_normal.htsvoice

echo "$1" | open_jtalk -r 0.6 -fm 3 -m $JTALK_Path  -x /var/lib/mecab/dic/open-jtalk/naist-jdic -ow $TMP && aplay --quiet $TMP
rm -f $TMP

