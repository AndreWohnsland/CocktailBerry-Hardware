# CocktailBerryBoard Slim

The **CocktailBerryBoard** is a dedicated control board for CocktailBerry machines.
It replaces the loose jumper wires and generic relay arrays normally used to switch the pumps, giving you clean, repeatable wiring on a single board.
It drives its outputs directly from the Raspberry Pi's GPIO pins.
This is a variant of the GPIO-based board (CBB-GPIO), with a smaller form factor and fewer channels, designed for compact builds.

--8<-- "board/released.md"

<figure markdown>
  ![Top view](../../img/cbb-slim/board_top.jpeg)
  <figcaption>Top view of the board</figcaption>
</figure>

## Overview

The board switches up to **8 circuits** through the Raspberry Pi's GPIO pins and on-board **MOSFETs**, replacing relay arrays with a quieter and more compact solution.
Each output carries a built-in **flyback (backflow) diode**, and the 12 V supply can be **daisy-chained** onward, which keeps wiring across the machine simple.

Although it was designed for the [2-Go](../machines/2-go/index.md), it works with any device that can be controlled from a GPIO output.

## Specifications

| Property          | Detail                                                    |
| ----------------- | --------------------------------------------------------- |
| Variant           | GPIO (CBB-Slim)                                           |
| Channels          | Up to 8 independently switched circuits                   |
| Switching         | MOSFET, driven from Raspberry Pi GPIO                     |
| Per-channel diode | Built-in flyback / backflow protection                    |
| Wiring            | One signal header pin per channel + 2×GND                 |
| Power             | 12 V input **and** output connector (PSU daisy-chain)     |
| Dispenser outputs | One (+/–) connector per dispenser - no voltage conversion |
| Protection        | Input fuse and per-channel flyback diodes                 |
| Indication        | On/off status LED                                         |

## Mechanical

- It is **not** a HAT - it does not plug onto the Pi's 40-pin header. Connections are
  made via **pin headers**: one signal pin per channel, plus 2 × GND, wired to the
  Pi's GPIO.
- Smaller footprint but a longer body than the CBB-GPIO.

## Files

Production files are attached to each [release][releases] as a single archive, generated with KiKit:

- **Fabrication package (JLCPCB):**
  [`cbb-slim.zip`]({{extra.repo_url}}/releases/latest/download/cbb-slim.zip)
  - Gerbers, BOM, and positions (pick-and-place).

[releases]: {{extra.repo_url}}/releases

--8<-- "disclaimer.md"
