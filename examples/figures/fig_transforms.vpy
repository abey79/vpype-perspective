pagesize 10x10cm

eval "pan=45;tilt=45"

repeat 8
    rect -l %_i+1% 0 0 10cm 10cm
    text -l %_i+1% -p 0.1cm 0.2cm -s 20 "layer %_i+1%"
end

pspread 2cm
ptranslate -l 4,5,6 -- -5cm 0 0
perspective -l 1,2,3,4,5,6,7,8 --pan %pan% --tilt %tilt% --hfov 10
lmove 1,2,3,7,8 9
lmove 4,5,6 10
text -l9 -p 6cm 11cm -s 27 -a left -- "ptranslate -l 4,5,6 -- -5cm 0 0"
translate -l9,10 -- -20cm 0

repeat 8
    rect -l %_i+1% 0 0 10cm 10cm
    text -l %_i+1% -p 0.1cm 0.2cm -s 20 "layer %_i+1%"
end

pspread 2cm
ptranslate -l 4,5,6 -- -5cm 0 0
protate -l4,5,6 y 20
perspective -l 1,2,3,4,5,6,7,8 --pan %pan% --tilt %tilt% --hfov 10
lmove 1,2,3,7,8 9
lmove 4,5,6 10
text -l9 -p 6cm 11cm -s 27 -a left -- "ptranslate -l 4,5,6 -- -5cm 0 0"
text -l9 -p 6cm 12cm -s 27 -a left -- "protate -l 4,5,6 y 20"
translate -l9,10 -- -20cm 0

repeat 8
    rect -l %_i+1% 0 0 10cm 10cm
    text -l %_i+1% -p 0.1cm 0.2cm -s 20 "layer %_i+1%"
end

pspread 2cm
ptranslate -l 4,5,6 -- -5cm 0 0
protate -l4,5,6 y 20
pscale -l5 0.5 0.5 0.5
perspective -l 1,2,3,4,5,6,7,8 --pan %pan% --tilt %tilt% --hfov 10
lmove 1,2,3,7,8 9
lmove 4,5,6 10
text -l9 -p 6cm 11cm -s 27 -a left -- "ptranslate -l 4,5,6 -- -5cm 0 0"
text -l9 -p 6cm 12cm -s 27 -a left -- "protate -l 4,5,6 y 20"
text -l9 -p 6cm 13cm -s 27 -a left -- "pscale -l 5 0.5 0.5 0.5"

layout -l -m 0.3cm 9x30cm