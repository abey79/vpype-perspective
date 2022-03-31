pagesize 10x10cm
repeat 5
    eval "move=-8+_i*4"
    eval "dx=_i*10*cm"
    repeat 5
        rect -l %_i+1% 0 0 10cm 10cm
        text -l %_i+1% -p 0.1cm 0.2cm -s 12 "layer %_i+1%"
    end

    text -l5 -p 5cm 11cm -s 32 -a center "move = (%move%cm, 0, 0)"
    perspective -l 1,2,3,4,5 --move %move%cm 0 0 --hfov 60
    lmove 1,2,3,4,5 6
    scale -l6 0.5 0.5
    translate -l6 %dx% 0
end
layout -l -m 0.3cm 7x30cm