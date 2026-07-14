<img src="https://raw.githubusercontent.com/AndreWohnsland/CocktailBerry/master/docs/pictures/CocktailBerry.svg" alt="CocktailBerry Hardware"/>

<br/>

[![Support CocktailBerry](https://img.shields.io/badge/Support%20CocktailBerry-donate-yellow)](https://www.buymeacoffee.com/AndreWohnsland)

CocktailBerry Hardware is the **official hardware repository** for the [CocktailBerry](https://github.com/AndreWohnsland/CocktailBerry) project.
It holds the machine designs (FreeCAD sources) and custom PCB(A)s (KiCad projects) you need to build your own CocktailBerry machine.

<a href="https://cocktailberry.org/"><img src="https://raw.githubusercontent.com/AndreWohnsland/CocktailBerry/master/docs/pictures/websitebutton.png" alt="website" height="70"/></a>
<a href="https://hardware.cocktailberry.org/"><img src="https://raw.githubusercontent.com/AndreWohnsland/CocktailBerry/master/docs/pictures/docbutton.png" alt="hardware documentation" height="70"/></a>
<a href="https://docs.cocktailberry.org/"><img src="https://raw.githubusercontent.com/AndreWohnsland/CocktailBerry/master/docs/pictures/softwarebutton.png" alt="software documentation" height="70"/></a>

Build guides, parts lists, specifications, and downloadable fabrication files live in the
**[Hardware Documentation](https://hardware.cocktailberry.org/)**. For the software, setup, and
configuration, see the [main CocktailBerry project](https://github.com/AndreWohnsland/CocktailBerry)
and the [Software Documentation](https://software.cocktailberry.org/).

Like this project? Give the main repo a star on GitHub! ⭐

# Designs

Sources live in this repo; fabrication files (Gerbers/BOM/CPL for boards, STEP/STL for machines)
are generated from them by the build pipeline. Full specs, parts, and downloads are on the
[Hardware Documentation](https://hardware.cocktailberry.org/).

**PCBAs** ([`pcb/`](pcb)) — control boards that replace relay arrays, switching pump circuits via MOSFETs:

| Board                                                                                         | Description                          | Status   |
| --------------------------------------------------------------------------------------------- | ------------------------------------ | -------- |
| [CocktailBerryBoard GPIO](https://hardware.cocktailberry.org/pcbas/cocktailberry-board-gpio/) | GPIO-based, up to 10 circuits        | Released |
| [CocktailBerryBoard Slim](https://hardware.cocktailberry.org/pcbas/cocktailberry-board-slim/) | Compact GPIO-based, up to 8 circuits | Released |
| [CocktailBerryBoard I2C](https://hardware.cocktailberry.org/pcbas/cocktailberry-board-i2c/)   | I2C-based, up to 10 circuits         | Alpha    |

**Machines** ([`cad/`](cad)) — 3D-printable machine builds:

| Machine                                                                  | Description                                            | Status   |
| ------------------------------------------------------------------------ | ------------------------------------------------------ | -------- |
| [CocktailBerry MK III](https://hardware.cocktailberry.org/machines/mk3/) | Compact footprint with integrated touchscreen support  | Released |
| [CocktailBerry 2-Go](https://hardware.cocktailberry.org/machines/2-go/)  | Portable Euro Box build with detachable legs           | Released |
| [CocktailBerry MK IV](https://hardware.cocktailberry.org/machines/mk4/)  | v2 reference build, optional scale + peristaltic pumps | Beta     |

# Contributing / How to Help

Contributions are very welcome - a new machine design, an improved model, or a PCB layout.
Open an issue or pull request.

**Please submit source files only:**

- PCBs: the KiCad project (`*.kicad_sch`, `*.kicad_pcb`, and any local symbols/footprints)
- Machines: the FreeCAD sources (`*.FCStd`)

Do **not** commit generated fabrication artifacts (Gerbers, drill, CPL, STL, STEP) - those are
built from the sources by the pipeline (see [`pcb/README.md`](pcb/README.md) and
[`cad/README.md`](cad/README.md)). See the main project's
[Contributing Guidelines](https://github.com/AndreWohnsland/CocktailBerry/blob/master/CONTRIBUTING.md)
for general rules.

# Related Projects

| Project                                                                        | Description                                |
| ------------------------------------------------------------------------------ | ------------------------------------------ |
| [CocktailBerry](https://github.com/AndreWohnsland/CocktailBerry)               | The main software project (Python + React) |
| [CocktailBerry Addons](https://github.com/AndreWohnsland/CocktailBerry-Addons) | Community addons and extensions            |
| [Software Documentation](https://software.cocktailberry.org/)                  | Software setup and configuration guides    |
