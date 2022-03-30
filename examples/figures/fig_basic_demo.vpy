pagesize 10x10cm
repeat 5
    rect -l %_i+1% 0 0 10cm 10cm
    text -l %_i+1% -p 0.1cm 0.2cm -s 12 "layer %_i+1%"
end
perspective --hfov 60
lmove all 1