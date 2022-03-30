pagesize 10x10cm

eval "pan=45;tilt=45"

repeat 8
    rect -l %_i+1% 0 0 10cm 10cm
    text -l %_i+1% -p 0.1cm 0.2cm -s 20 "layer %_i+1%"
end

pspread 2cm
ptranslate -l4,5,6 3cm 0 0
perspective -l 1,2,3,4,5,6,7,8 --pan %pan% --tilt %tilt% --hfov 10
lmove 1,2,3,7,8 9
lmove 4,5,6 10
text -l9 -p 6cm 14.5cm -s 25 -a left -- "ptranslate -l 4,5,6 3cm 0 0"
translate -l9,10 -- -20cm 0

repeat 8
    rect -l %_i+1% 0 0 10cm 10cm
    text -l %_i+1% -p 0.1cm 0.2cm -s 20 "layer %_i+1%"
end

pspread 2cm
ptranslate -l4,5,6 -a 3cm 0 0
perspective -l 1,2,3,4,5,6,7,8 --pan %pan% --tilt %tilt% --hfov 10
lmove 1,2,3,7,8 9
lmove 4,5,6 10
text -l9 -p 5cm 14.5cm -s 25 -a left -- "ptranslate -l 4,5,6 -a 3cm 0 0"

layout -l -m 0.3cm 8x16cm