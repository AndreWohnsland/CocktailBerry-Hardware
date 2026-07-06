# CocktailBerryBoard I2C

The **CocktailBerryBoard** is a dedicated control board for CocktailBerry machines.
It replaces the loose jumper wires and generic relay arrays normally used to switch the pumps, giving you clean, repeatable wiring on a single board.
It drives its outputs directly from the Raspberry Pi's I²C interface.

It is still in the concept phase and not yet production-ready. It is not recommended to use it in a production environment yet.

--8<-- "board/alpha.md"

## Overview

The board switches up to **10 circuits** through the Raspberry Pi's I²C interface and on-board **MOSFETs**, replacing relay arrays with a quieter and more compact solution.
Each output carries a built-in **flyback (backflow) diode**, and the 12 V supply can be **daisy-chained** onward, which keeps wiring across the machine simple.
The I²C bus can be daisy-chained to further devices, sharing the Pi's single bus.

Although it was designed for the [MK IV](../machines/mk4/index.md), it works with any device that can be controlled over I²C.

## Specifications

| Property          | Detail                                                    |
| ----------------- | --------------------------------------------------------- |
| Variant           | I²C (CBB-I2C)                                             |
| Channels          | Up to 10 independently switched circuits                  |
| Switching         | MOSFET, driven from Raspberry Pi I²C                      |
| Per-channel diode | Built-in flyback / backflow protection                    |
| Wiring            | 4 Pin Headers, SH, PH 4 pin (SDA, SCL, GND, VCC)          |
| Power             | 12 V input **and** output connector (PSU daisy-chain)     |
| Dispenser outputs | One (+/–) connector per dispenser - no voltage conversion |
| Protection        | Input fuse and per-channel flyback diodes                 |
| Indication        | On/off status LED                                         |

## Mechanical

- Shares the **Raspberry Pi mounting-hole pattern**, so the board and a Pi can be
  stacked / co-mounted.
- It is **not** a HAT - it does not plug onto the Pi's 40-pin header. Connections are
  made via **pin headers**: one 4-pin header per channel, wired to the
  Pi's I²C interface.

## Files

Production files are attached to each [release][releases] as a single archive, generated with KiKit:

- **Fabrication package (JLCPCB):**
  [`cbb-i2c.zip`]({{extra.repo_url}}/releases/latest/download/cbb-i2c.zip)
  - Gerbers, BOM, and positions (pick-and-place).

All parts (SMD, THT) are included in the package, so you can order the board and all parts from JLCPCB directly.

[releases]: {{extra.repo_url}}/releases

--8<-- "disclaimer.md"
