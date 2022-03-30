import vsketch


class WobblyCylindersSketch(vsketch.SketchClass):
    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("13x20.5cm", landscape=False, center=False)
        vsk.scale("cm")

        for i in range(1, 100):
            vsk.stroke(i)
            for j in range(-25, 46, 5):
                vsk.circle(j, 5, 5 * vsk.noise(i * 0.15, 0, j))
                vsk.circle(j, 15, 5 * vsk.noise(i * 0.15, 1, j))

        vsk.vpype("ptranslate 0 0 3cm perspective -f 120 -dz 0.5cm occult -i color blue")
        vsk.vpype("crop 5mm 5mm '%prop.vp_page_size[0]-1*cm%' '%prop.vp_page_size[1]-1*cm%'")
        vsk.vpype("rect 5mm 5mm '%prop.vp_page_size[0]-1*cm%' '%prop.vp_page_size[1]-1*cm%'")
        vsk.vpype("lmove all 1")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    WobblyCylindersSketch.display()
