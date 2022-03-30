pagesize 10x10cm

eval "pan=45;tilt=45"

repeat 5
    rect -l %_i+1% 0 0 10cm 10cm
    text -l %_i+1% -p 0.1cm 0.2cm -s 12 "layer %_i+1%"
end


pspread 2cm
perspective -l 1,2,3,4,5 --pan %pan% --tilt %tilt% --hfov 10
lmove 1,2,3,4,5 6
text -l6 -p -3cm 11cm -s 25 -a left "delta_z = 2cm"
translate -l6 -- -14cm 0

repeat 5
    rect -l %_i+1% 0 0 10cm 10cm
    text -l %_i+1% -p 0.1cm 0.2cm -s 12 "layer %_i+1%"
end

pspread 1cm
perspective -l 1,2,3,4,5 --pan %pan% --tilt %tilt% --hfov 10
lmove 1,2,3,4,5 6
text -l6 -p .5cm 11cm -s 25 -a left "delta_z = 1cm"
translate -l6 -- -12cm 0

repeat 5
    rect -l %_i+1% 0 0 10cm 10cm
    text -l %_i+1% -p 0.1cm 0.2cm -s 12 "layer %_i+1%"
end

pspread 0.2cm
perspective -l 1,2,3,4,5 --pan %pan% --tilt %tilt% --hfov 10
text -l6 -p 1.5cm 11cm -s 25 -a left "delta_z = 0.2cm"
lmove 1,2,3,4,5 6


layout -l -m 0.3cm 8x20cm