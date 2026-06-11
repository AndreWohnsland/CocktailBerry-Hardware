# CocktailBerryBoard

The **CocktailBerryBoard** is a dedicated control board for CocktailBerry machines.
It replaces the loose jumper wires and generic relay arrays normally used to switch
the pumps, giving you clean, repeatable wiring on a single board.

It is currently available as a **GPIO-based** board (CBB-GPIO), driving its outputs
directly from the Raspberry Pi's GPIO pins. An I²C-based variant may follow in the
future.

!!! success "Released"
    This board is **released**. Full production artifacts (ready to order at JLCPCB)
    are available.

## Overview

The board switches up to **10 circuits** through the Raspberry Pi's GPIO pins and
on-board **MOSFETs**, replacing relay arrays with a quieter, more compact, and more
reliable solution. Each output carries a built-in **flyback (backflow) diode**, and
the 12 V supply can be **daisy-chained** onward, which keeps wiring across the
machine simple.

Although it was designed for the [MK III](../machines/mk-iii/index.md), it works with
any device that can be controlled from a GPIO output.

## Specifications

| Property          | Detail                                                    |
| ----------------- | --------------------------------------------------------- |
| Variant           | GPIO (CBB-GPIO)                                           |
| Channels          | Up to 10 independently switched circuits                  |
| Switching         | MOSFET, driven from Raspberry Pi GPIO                     |
| Per-channel diode | Built-in flyback / backflow protection                    |
| Wiring            | One signal header pin per channel + 2 × GND               |
| Power             | 12 V input **and** output connector (PSU daisy-chain)     |
| Dispenser outputs | One (+/–) connector per dispenser — no voltage conversion |
| Protection        | Input fuse and per-channel flyback diodes                 |
| Indication        | On/off status LED                                         |
| Status            | Released — production-ready (JLCPCB artifacts)            |

## Mechanical

- Shares the **Raspberry Pi mounting-hole pattern**, so the board and a Pi can be
  stacked / co-mounted.
- It is **not** a HAT — it does not plug onto the Pi's 40-pin header. Connections are
  made via **pin headers**: one signal pin per channel, plus 2 × GND, wired to the
  Pi's GPIO.

## Files

Production files are attached to each [release][releases] as a single archive,
generated with KiKit:

- **Fabrication package (JLCPCB):**
  [`cbb-gpio.zip`](https://github.com/AndreWohnsland/CocktailBerry-Hardware/releases/latest/download/cbb-gpio.zip)
  — Gerbers, drill, BOM, and CPL (pick-and-place).

!!! info
    The link always points to the **latest release** and will 404 until the
    first release is published.

[releases]: https://github.com/AndreWohnsland/CocktailBerry-Hardware/releases
