# Needed Parts

Everything required to build the CocktailBerry MK IV.

## Printed Parts (STLs)

--8<-- "machine/variants.md"

| Part                        | Qty | File                    | Notes               |
| --------------------------- | --- | ----------------------- | ------------------- |
| Bundler                     | 1   | Bundler                 |                     |
| Draining Rack               | 1   | DrainingRack            |                     |
| Drip Tray No Scale          | 1   | DripTrayNoScale         | default tray        |
| Drip Tray With Scale        | 1   | DripTrayWithScale       | *variant* scale     |
| Load Cell Bottom Holder     | 1   | LoadCellBottomHolder    | *optional* scale    |
| Load Cell Top Connector     | 1   | LoadCellTopConnector    | *optional* scale    |
| Scale Electrics Socket      | 1   | ScaleElectricsSocket    | *optional* scale    |
| Tablet Holder Plate         | 1   | TabletHolderPlate       |                     |
| Funnel                      | 1   | Funnel                  | default funnel      |
| Short Funnel                | 1   | ShortFunnel             | *variant* funnel    |
| Long Funnel                 | 1   | LongFunnel              | *variant* funnel    |
| LED Hole Plug               | 1   | LedHolePlug             | *optional* LED      |
| Lid Top                     | 1   | LidTop                  |                     |
| Peristaltic Holder          | 2   | PeristalticHolder       |                     |
| Pump Tower Lid              | 2   | PumpTowerLid            |                     |
| Tube Fixer                  | 1   | TubeFixer               | *optional*          |
| Tower Top                   | 1   | TowerTop                |                     |
| Tower Middle                | 1   | TowerMiddle             |                     |
| Tower Bottom No Scale       | 1   | TowerBottomNoScale      | default bottom      |
| Tower Bottom No Scale LED   | 1   | TowerBottomNoScaleLED   | *variant* LED       |
| Tower Bottom With Scale     | 1   | TowerBottomWithScale    | *variant* scale     |
| Tower Bottom With Scale LED | 1   | TowerBottomWithScaleLED | *variant* scale LED |

Note that the tower comes in different variants, most notably at the bottom section.
There are 4 variants:

- plain
- with LED
- with scale
- with scale and LED

## Electronics

See also the [PCBAs](../../pcbas/index.md) section.

| Component | Qty | Notes                            |
| --------- | --- | -------------------------------- |
| CBB-I2C   | 1   | GPIO Variant is fine if no scale |

Note that the I2C board version is easier to install and integrate with the rest of the components.
You can always use the GPIO version if you prefer, but it will require more wiring.
If you do not use a scale, the GPIO version is still a good fit.

## Hardware

| Item                              | Qty    | Notes                                         |
| --------------------------------- | ------ | --------------------------------------------- |
| {{extra.pi_5_link}}               | 1      | {{extra.pi_4_link}} works as well             |
| {{extra.sd_card_link}}            | 1      |                                               |
| {{extra.power_jack_2_5_mm_link}}  | 1      |                                               |
| {{extra.voltage_converter_link}}  | 1      |                                               |
| {{extra.power_supply_12v_link}}   | 1      |                                               |
| {{extra.membrane_pump_link}}      | 8      | {{extra.membrane_pump_alt_link}} is also fine |
| {{extra.peristaltic_pump_link}}   | 2      |                                               |
| {{extra.tubing_link}}             | 5-10 m | 5×8 mm                                        |
| {{extra.tubing_link}}             | 2 m    | 3×5 mm                                        |
| {{extra.jumper_wires_link}}       | 1      | 10 cm is long enough                          |
| {{extra.hex_standoffs_link}}      | 16     | can use other height                          |
| {{extra.usb_c_open_cable_link}}   | 1      |                                               |
| {{extra.lenovo_tab_link}}         | 1      | Can use your phone instead                    |
| {{extra.magnet_6x3_link}}         | 2      |                                               |
| (Wooden) Base Plate ~40×40 cm     | 1      |                                               |
| {{extra.strip_led_link}}          | 1      | *Optional* if using LED                       |
| {{extra.led_3pin_connector_link}} | 1      | *Optional* if using LED                       |
| {{extra.load_cell_link}}          | 1      | *Optional* if using scale                     |
| {{extra.nau7802_link}}            | 1      | *Optional* if using scale                     |

## Fasteners

For more information on the threaded inserts, see the section below.
The following inserts are required for the assembly of the machine:

| Metric | Qty              |
| ------ | ---------------- |
| 2.5    | 12 or 16 (scale) |
| 3      | 14               |
| 4      | 3                |
| 5      | 2                |

The screw length allows slight variations, but stay within +5 mm of the given size.
The following screws are recommended for the assembly of the machine:

| Metric | Type       | l (mm) | Qty |
| ------ | ---------- | ------ | --- |
| 2.5    | Socket cap | 10     | 4   |
| 3      | Socket cap | 10     | 10  |
| 3      | Socket cap | 10-15  | 2   |
| 3      | Flat       | 10-12  | 2   |
| 4      | Socket cap | 25     | 3   |
| 5      | Flat       | 25     | 2   |

For the scale, the following screws are required:

| Metric | Type | l (mm) | Qty |
| ------ | ---- | ------ | --- |
| 4      | Flat | 10-15  | 2   |
| 5      | Flat | 30     | 2   |

I usually use a one-stop shop for all screws and fasteners, like {{extra.screw_shop_link}}.

--8<-- "inserted_threads.md"

--8<-- "additional_parts.md"
