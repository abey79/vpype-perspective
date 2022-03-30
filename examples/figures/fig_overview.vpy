rect -l1 0 0 15cm 15cm
line -l1 0 7.5cm 15cm 7.5cm
line -l1 7.5cm 0 7.5cm 15cm
text -l1 -p 14cm 0.4cm -a right "layer 1"
rect -l3 0 0 15cm 15cm
line -l3 0 7.5cm 15cm 7.5cm
line -l3 7.5cm 0 7.5cm 15cm
text -l3 -p 14cm 0.4cm -a right "layer 2"

rect -l11 0 0 15cm 15cm
line -l11 0 7.5cm 15cm 7.5cm
line -l11 7.5cm 0 7.5cm 15cm
text -l11 -p 14cm 0.4cm -a right "layer N"

# camera
line -l12 7.5cm 0cm 0cm 7.5cm
line -l12 7.5cm 0cm 15cm 7.5cm
ptranslate -l12 -a 0 0 5cm
protate -l12 y 180
protate -l12 x 90
ptranslate -l12 0 0 5cm

line -l13 0cm 7.5cm 7.5cm 0cm
line -l13 0cm 7.5cm 7.5cm 15cm
text -l13 -p .6cm 7.5cm camera
ptranslate -l13 -a 0 0 5cm
protate -l13 y 90
ptranslate -l13 0 0 5cm

# main axis
line -l14 2.5cm 7.5cm 12.5cm 7.5cm
ptranslate -l14 -a 0 0 5cm
protate -l14 y 90

# coordinate system
line -l15 7.5cm 7.5cm 7.5cm 6.5cm
line -l15 7.5cm 7.5cm 8.5cm 7.5cm
text -l15 -p 8.3cm 7.8cm -s 16 x
text -l15 -p 7.7cm 6.2cm -s 16 y
ptranslate -l15 -a 0 0 0

line -l16 7.5cm 7.5cm 6.5cm 7.5cm
text -l16 -p 6.5cm 7.8cm -s 16 z
text -l16 -p 7.7cm 7.3cm -s 12 -s 20 "world origin"
ptranslate -l16 -a 0 0 0
protate -l16 y 90


circle -l7 7.5cm 7.5cm 0.2cm
text -l8 -p 7.5cm 8.2cm "aiming"
text -l8 -p 7.5cm 8.8cm "point"
penwidth -l7 1mm
ptranslate -l7,8 -a 0 0 5cm
protate -l7,8 y 90


pagesize 15x15cm
perspective --hfov 30 --pan 62 --tilt 30
occult -i -k
color -l 7,8 "#0a0"
color -l 2,14 "#ddd"
color -l 1,3,11 black
color -l 12,13 blue

# clean up draw order
lmove 14 2
lmove 15,16 6
color -l6 "#faa"


layout -m 3mm 15x15cm



