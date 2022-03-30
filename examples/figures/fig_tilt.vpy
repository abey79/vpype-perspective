pagesize 10x10cm
repeat 3
    eval "tilt=-40+_i*40"
    eval "dx=_i*14*cm"
    repeat 5
        rect -l %_i+1% 0 0 10cm 10cm
        text -l %_i+1% -p 0.1cm 0.2cm -s 12 "layer %_i+1%"
    end


    perspective -l 1,2,3,4,5 --tilt %tilt% --hfov 60
    lmove 1,2,3,4,5 6
    translate -l6 %dx% 0
    text -l6 -p %dx+5*cm% 11cm -s 25 -a center "tilt = %tilt%deg"
end
layout -l -m 0.3cm 8x30cm