"""
genfp.py

Description:

Generate the kicad footprint for a resistive touch plate.

Author: Mahesh Venkitachalam
Website: electronut.in
"""

import argparse
import math

str_hdr="""(module TouchPlate-10mm (layer F.Cu) (tedit 55E32894)
  (fp_text reference TP1 (at 0.254 12.7) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value Touch_Plate (at 0.127 -12.573) (layer F.Fab)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_circle (center 0 0) (end -8.382 -5.461) (layer F.SilkS) (width 0.15))
"""

str_footer = ")\n"

str_pad0 = """  (pad 1 smd rect (at -6.731 -6.223 40) (size 1.524 1.524) (layers F.Cu F.Paste F.Mask))
"""
# radium in mm
radius = 8


# generate arcs of touch plate
def genArcs():
    str_pad = ""
    # generate right arc
    for theta in range(-75, 80, 5):
        x = radius*math.cos(math.radians(theta))
        y = radius*math.sin(math.radians(theta))
        angle = 180-theta
        if theta == -75 or theta == 75:
            line = "  (pad 2 smd circle (at %.3f %.3f %f) (size 1.524 1.524) (layers F.Cu F.Paste F.Mask))\n" % (x, y, angle)
        else: 
            line = "  (pad 2 smd rect (at %.3f %.3f %f) (size 1.524 1.524) (layers F.Cu F.Paste F.Mask))\n" % (x, y, angle)
        str_pad += line 

    # generate left arc
    for theta in range(100, 260, 5):
        x = radius*math.cos(math.radians(theta))
        y = radius*math.sin(math.radians(theta))
        angle = 180-theta
        if theta == 100 or theta == 255:
            line = "  (pad 1 smd circle (at %.3f %.3f %f) (size 1.524 1.524) (layers F.Cu F.Paste F.Mask))\n" % (x, y, angle)
        else: 
            line = "  (pad 1 smd rect (at %.3f %.3f %f) (size 1.524 1.524) (layers F.Cu F.Paste F.Mask))\n" % (x, y, angle)
        str_pad += line 

    return str_pad

# main() function
def main():
    # create parser
    descStr = "Generate kicad footprint for a touch plate."
    parser = argparse.ArgumentParser(description=descStr)
    # add expected arguments
    parser.add_argument('--file', dest='fpFile', required=True)
    # parse args
    args = parser.parse_args()
    # create file
    fpFile = args.fpFile
    print("writing to %s...\n" % (fpFile, ))
    f = open(fpFile, 'w')
    # write header
    f.write(str_hdr)
    # arcs
    tmp = genArcs()
    f.write(tmp)
    # write footer
    f.write(str_footer)
    f.close();
    print("done.")

# call main
if __name__ == '__main__':
    main()
