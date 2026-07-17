---
tags: [Machine]
---

# Needed Parts

Everything required to build the CocktailBerry MK III.

## Printed Parts (STLs)

--8<-- "machine/variants.md"

| Part                 | Qty | File Name          | Notes           |
| -------------------- | --- | ------------------ | --------------- |
| Bundler              | 1   | Bundler            |                 |
| Draining Rack        | 1   | DrainingRack       |                 |
| Funnel Bend          | 1   | FunnelBend         | default funnel  |
| Funnel Bend Small    | 1   | FunnelBendSmall    | optional funnel |
| Funnel Straight      | 1   | FunnelStraight     | optional funnel |
| Lid Tower            | 1   | LidTower           |                 |
| Monitor Bridge       | 1   | MonitorBridge      |                 |
| Pump Fixer           | 8   | PumpFixer          | optional        |
| Tower Bottom         | 1   | TowerBottom        |                 |
| Tower Middle         | 1   | TowerMiddle        | default middle  |
| Tower Middle RingLED | 1   | TowerMiddleRingLED | optional middle |
| Tower Top            | 1   | TowerTop           |                 |
| Tube Fixer 40mm      | 2   | TubeFixer40mm      | optional        |
| Tube Fixer 50mm      | 2   | TubeFixer50mm      | optional        |

## Custom Boards

See also the [PCBAs](../../pcbas/index.md) section.

| Component | Qty | Notes                       |
| --------- | --- | --------------------------- |
| CBB-GPIO  | 1   | I2C Variant is fine as well |

## Hardware

| Item                                | Qty    | Notes                                         |
| ----------------------------------- | ------ | --------------------------------------------- |
| {{extra.pi_3bplus_link}}            | 1      | Pi 4/5 needs a different HDMI cable           |
| {{extra.sd_card_link}}              | 1      |                                               |
| {{extra.touch_7in_link}}            | 1      | Case designed for this                        |
| {{extra.power_jack_2_5_mm_link}}    | 1      |                                               |
| {{extra.voltage_converter_link}}    | 1      |                                               |
| {{extra.power_supply_12v_link}}     | 1      |                                               |
| {{extra.membrane_pump_link}}        | 8      | {{extra.membrane_pump_alt_link}} is also fine |
| {{extra.tubing_link}}               | 5-10 m | 5×8 mm                                        |
| {{extra.jumper_wires_link}}         | 1      | 10 cm is long enough                          |
| {{extra.hex_standoffs_link}}        | 16     | can use other height                          |
| {{extra.hdmi_cable_link}}           | 1      | needs to be slim                              |
| {{extra.usb_cable_link}}            | 1      | needs to be slim                              |
| {{extra.micro_usb_open_cable_link}} | 1      |                                               |
| (Wooden) Base Plate ~40×40 cm       | 1      |                                               |
| {{extra.ring_led_12_link}}          | 2      | *Optional* if using LED tower                 |

## Fasteners

For more information on the threaded inserts, see the section below.
The following inserts are required for the assembly of the machine:

| Metric | Qty |
| ------ | --- |
| 2.5    | 8   |
| 3      | 4   |
| 4      | 3   |
| 5      | 1   |

The screw length allows slight variations, but stay within +5 mm of the given size.
The following screws are recommended for the assembly of the machine:

| Metric | Type       | l (mm) | Qty |
| ------ | ---------- | ------ | --- |
| 2.5    | socket cap | 10     | 5   |
| 3      | flat       | 15     | 2   |
| 3      | flat       | 10     | 2   |
| 3      | grub screw | ~5     | 8   |
| 4      | socket cap | 10     | 3   |
| 5      | flat       | 25     | 2   |

I usually use a one-stop shop for all screws and fasteners, like {{extra.screw_shop_link}}.

--8<-- "inserted_threads.md"

--8<-- "additional_parts.md"
