line -l10 0 0 0 10cm
text -l10 -p 0 -0.5cm -a center "layer N"
line -l10 14cm 0 14cm 10cm
text -l10 -p 14cm -0.5cm -a right "layer 2"
line -l10 15cm 0 15cm 10cm
text -l10 -p 15cm -0.5cm "layer 1"
color -l10 black

line -l5 14cm 10.5cm 14cm 10.8cm
line -l5 14cm 10.8cm 15cm 10.8cm
line -l5 15cm 10.8cm 15cm 10.5cm
text -l2 -p 14.5cm 11.2cm -a center "delta_z"
line -l5 -- -7cm 10.5cm -7cm 10.8cm
line -l5 -- -7cm 10.8cm 0 10.8cm
line -l5 0 10.8cm 0 10.5cm
text -l2 -p -3.5cm 11.2cm -a center "focal"
color -l2 black

line -l9 0 0 -7cm 5cm
line -l9 0 10cm -7cm 5cm
text -l9 -p -7.2cm 5cm -a right "camera"
arc -l9 -- -7cm 5cm 1cm 1cm -35.5 35.5
text -l9 -p -5.8cm 5cm "hfov"
color -l9 blue

# world origin
line -l11 15cm 5cm 15cm 5.8cm
line -l11 15cm 5cm 14.2cm 5cm
text -l11 -p 14.2cm 4.8cm "z"
text -l11 -p 15.2cm 5.8cm "x"
text -l11 -p 15.2cm 5cm "world origin"
color -l11 red

# aiming point
circle -l12 7.5cm 5cm 0.2cm
text -l12 -p 7.5cm 5.6cm -a center "camera"
text -l12 -p 7.5cm 6.2cm -a center "aiming"
text -l12 -p 7.5cm 6.8cm -a center "point"
color -l12 "#0a0"


# projected layers
line -l5 -- -7cm 5cm 15cm 0
line -l5 -- -7cm 5cm 14cm 0
line -l5 -- -7cm 5cm 15cm 10cm
line -l5 -- -7cm 5cm 14cm 10cm
line -l5 -- -7cm 5cm 15cm 5cm
color -l5 "#ddd"

layout -m 0.3cm -l 20x10cm