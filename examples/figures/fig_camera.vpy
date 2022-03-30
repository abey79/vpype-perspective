pagesize 10x10cm

eval "dx = -13*cm"

repeat 5
    rect -l %_i+1% 0 0 10cm 10cm
    text -l %_i+1% -p 0.1cm 0.2cm -s 12 "layer %_i+1%"
end
perspective -l 1,2,3,4,5 --hfov 60
crop -l 1,2,3,4,5 -- -1cm -1cm 12cm 12cm
rect -l 7 -- -1cm -1cm 12cm 12cm
text -l5 -p 5cm 11.5cm -s 25 -a center "default"
lmove 1,2,3,4,5 6
translate -l6,7 %dx% 0

repeat 5
    rect -l %_i+1% 0 0 10cm 10cm
    text -l %_i+1% -p 0.1cm 0.2cm -s 12 "layer %_i+1%"
end
perspective -l 1,2,3,4,5 --hfov 60 --pan 25
crop -l 1,2,3,4,5 -- -1cm -1cm 12cm 12cm
rect -l 7 -- -1cm -1cm 12cm 12cm
text -l5 -p 5cm 11.5cm -s 25 -a center "pan = 25deg"
lmove 1,2,3,4,5 6
translate -l6,7 %dx% 0

repeat 5
    rect -l %_i+1% 0 0 10cm 10cm
    text -l %_i+1% -p 0.1cm 0.2cm -s 12 "layer %_i+1%"
end
perspective -l 1,2,3,4,5 --hfov 60 --pan 25 --tilt  45
crop -l 1,2,3,4,5 -- -1cm -1cm 12cm 12cm
rect -l 7 -- -1cm -1cm 12cm 12cm
text -l5 -p 5cm 11.5cm -s 25 -a center "pan = 25deg"
text -l5 -p 5cm 12.3cm -s 25 -a center "tilt = 45deg"
lmove 1,2,3,4,5 6
translate -l6,7 %dx% 0

repeat 5
    rect -l %_i+1% 0 0 10cm 10cm
    text -l %_i+1% -p 0.1cm 0.2cm -s 12 "layer %_i+1%"
end
perspective -l 1,2,3,4,5 --hfov 60 --pan 25 --tilt  45 --move 0 5cm 0
crop -l 1,2,3,4,5 -- -1cm -1cm 12cm 12cm
rect -l 7 -- -1cm -1cm 12cm 12cm
text -l5 -p 5cm 11.5cm -s 25 -a center "pan = 25deg"
text -l5 -p 5cm 12.3cm -s 25 -a center "tilt = 45deg"
text -l5 -p 5cm 13.1cm -s 25 -a center "move = (0, 5cm, 0)"
lmove 1,2,3,4,5 6
translate -l6,7 %dx% 0


color -l7 grey
layout -l -m 0.3cm 7x30cm