# CocktailBerry MK IV

The **MK IV** is the reference build for the CocktailBerry **v2** software (the [MK III](../mk3/index.md) remains the reference for **v1**).
Like the MK III, it moves the wiring onto the [CocktailBerryBoard](../../pcbas/cocktailberry-board-gpio.md).
It is more streamlined and visually appealing, and adds the option to use a scale.
The base build also includes two peristaltic pumps, allowing the use of syrup in the machine.

It is fully 3D-printed and designed to be produced on a common **250 × 250 mm** print bed.

--8<-- "machine/beta.md"

## Specifications

| Property   | Value                                          |
| ---------- | ---------------------------------------------- |
| Dispensers | 8 × membrane pumps + 2 × peristaltic pumps      |
| Display    | Tablet or Smartphone                           |
| Controller | Raspberry Pi 4 or 5                            |
| Power      | 12 V input; internal transformer powers the Pi |
| Software   | CocktailBerry v2                               |
| Enclosure  | Fully 3D-printed                               |
| Dimensions | ⌀ ~240 mm × ~500 mm (H)                        |
| Scale      | Optional, below the Draining Rack              |
| LEDs       | Optional, behind the glass                     |

## Downloads

The printable and CAD files are attached to each [release]({{extra.repo_url}}/releases) as a single archive:

- **3D files:**
  [`mk4.zip`]({{extra.repo_url}}/releases/latest/download/mk4.zip)
  - STL (print-ready) and STEP (CAD) for every part.

## Build Guide

1. [Needed Parts](needed-parts.md) - what to print, buy, and have ready.
2. [Preparation](preparation.md) - printing, post-processing, and prep work.
3. [Assembly](assembly.md) - putting it all together.
