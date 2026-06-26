# Assembly

Step-by-step assembly of the CocktailBerry MK IV.

--8<-- "machine/image_support.md"

## Step 1 - Prepare the Base Plate

You need to drill two M5 (+0.1)mm holes along a line to the center of the base plate.
If you use a scale, you need to drill two additional M5 (+0.1)mm holes for the scale mounting.
Drill a chamfer for the countersunk heads into the holes.

TODO: Add sketch of the base plate with the holes marked.

## Step 2 - Assemble the Tower

Solder the power jack to some wires long enough to reach from the middle back hole for the jack into the middle of the top tower.
Mount the jack into the middle tower, put the wires through the top hole into the tower.

Start by screwing the Tower Bottom to the base plate using the two M5 inserts and M5 screws.
If using a scale, see [scale wiring](#optional-scale-wiring) and for LEDs see [LED wiring](#optional-led-wiring).

Stack the middle tower onto the bottom part and screw it to the bottom part using M3 screws.
If there are cables coming from the bottom tower, ensure to guide them through the middle tower.
Put the Tower Top on and screw it to the middle part using M4 screws.
Also guide all cables through the top tower, so they can be connected to the board later.
Insert the Bundler from top into the top tower using its profile and glue it in place.

## Step 3 - Mount the Pumps

Cut the tubing for the pump inlet, it should be a little longer than the distance from the base plate to the socket top of the pump socket.

### Membrane Pumps

The membrane pumps use the 8x5 mm tubing and are mounted into the kidney shaped pump sockets.
Connect the pump with the tubing, insert the tubing into one pump slot.
Push another tube from the middle tower through the bundler and the outlet, connect it to the pump.
Place the pump into the socket, gently pull the tubing to ensure it is secure.
Cut the outlet tube, leaving some distance to the end of the bundler.
Repeat this for all membrane pumps, try to order outlet tube path to the position in the bundler, so they don't cross each other.

### Peristaltic Pumps

The peristaltic pumps use the 3x5 mm tubing and are mounted into the elevated pump holders in the front.
First, screw the peristaltic pump into the pump holder using the M2.5 screws.
The tubing should look in the opposite direction of the top of the U-shape.
Then proceed connection input and output tubing as described for the membrane pumps.
Mount the pump holder into the tower using the M3 screws.

### Wrap-Up

When the tubes do not lay snugly, you can use the optional pump fixer to fix them in place, parallel to the bottom of the tower (should only concern membrane pumps).
You can use some tape to fix all tubes together at the machine outlet, so the can' slip back.
Push the funnel to the bundler until the magnet holds.

## Step 4 - Mount Electronics

Mount the CocktailBerry Board on the top tower (middle) using M2.5 nuts.
Use as many distance as needed to not collide with the tubes.
Fix the board with more M2.5 nuts on the top, so it doesn't move.
Do not use screws, since we add the Raspberry Pi on top of the board later.
Do the same with the converter on the inner back side of the tower.

## Step 5 - Solder the Pumps

If the pump is not soldered to the wires, they need to be soldered, otherwise skip this step.
Make sure the wire from each pump is long enough to reach the board, and solder the wires to the according pump socket on the board.
For peristaltic pumps, the polarity matters, so make sure to solder the direction that the pumps runs in the outlet direction of the tubing.

## Step 6 - Wiring of Electronics

For all the screw terminals, you can use the crimp connectors to make the wire connection easier and more secure, but this is an optional step.

The Power Jack needs to be connected to the 12V input of the CocktailBerry Board.
The 12V output of the board should be connected to the input of the voltage converter, and the 5V output of the converter should be connected to Raspberry Pi.
Connect each pump with an according +/- of the CocktailBerry Board for one pump.
For easier setup, try to connect the pumps in order (for example, pump 1 to the first pump socket, pump 2 to the second, etc.).

If you use a scale, connect it either to the I2C of the CocktailBerry Board or to the GPIO of the Raspberry Pi (next step), depending on your setup.

## Step 7 - Mount the RPi

Mount the Raspberry Pi on top of the CocktailBerry Board using the M2.5 nuts and screws.
Extend the nuts with a second nut in case you have too short nuts.
You can also already go with step 8 here (CocktailBerry Board connections) and then mount the RPi, since the GPIO connections are easier to access without the RPi in place.

## Step 8 - Connect Signals

If you use the I2C version of the CocktailBerry Board, just connect the I2C (5V, GND, SDA, SCL) of the Raspberry Pi to the I2C of the CocktailBerry Board.

Otherwise, connect the GPIO pins with the GND and pump 1-10 pins of the board using jumper wires.
Some RPi pins have a high signal pulse at startup, or a pull-up (default high) pin, try to avoid these.
Common used pins here are GPIO 18, 23, 24, 26, 17, 15, 9, 10, 22, 27 (and probably much more working ones).
If you experience issues with some GPIO, try another one first.

If you have an LED, connect it to the GND, 5V and GPIO (10 preferred) of the Raspberry Pi.

## Step 9 - Installation of Software

Follow the instructions in the [CocktailBerry docs](https://docs.cocktailberry.org/installation/) to install the software on the Raspberry Pi.
Be sure that you uncheck the pins inverted option at the first program start, since the board is inverted to a normal relay board.
This will cause all pumps to run at first program start.

## *Optional* Scale Wiring

The load cell is screwed by two M5 screws into the plate, with the bottom holder between.
The cable of the scale need to point to the center of the plate/tower.
Then screw the top connector onto the load cell using two M4 screws.
The cable of the load cell needs to be pushed through the hole in the bottom tower.
Most load cells will not have a long enough cable, so you need to solder an extension there.
It should be long enough to reach out of the bottom tower.
Screw the scale board onto the scale electronics socket using the M2.5 screws and slide it into the fitting socket in the tower.
Connect the load cell to the scale board, and add already the connection cable to the CocktailBerry Board/Raspberry Pi.
This will be guided later through the tower to the top, so it can be connected to the board later.

TODO: Exploded view of the scale assembly.

## *Optional* LED Wiring

It is recommended not to solder the LED before pushing the cable through the tower, since it is a tight fit.
Push the LED cable through the tower, and solder it to the LED strip.
Place the LED into the socket in the tower, touching the bottom of the cutout.
Put the led hole plug into the tower, hiding the hole for the cable.
I recommend using a connector cable for the led, so you can disconnect the led from the middle point of the tower, when you need to disassemble the tower later.
Otherwise you can also use a long enough cable to the top of the tower.
In each case already put the counter side of the cable on.
It can be guided through the tower to the top, so it can be connected to the board later.

TODO: Images of the assembly

## Final Checks

- All connections secure
- Pumps run in the correct direction
- First test run with water completed
