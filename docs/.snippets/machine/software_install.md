Follow the instructions in the [CocktailBerry docs](https://docs.cocktailberry.org/installation/) to install the software on the Raspberry Pi.
Uncheck the pins inverted option at the first program start - the board is inverted compared to a normal relay board, so with the wrong setting all pumps will run as soon as the program starts.
If you use the I2C version of the CocktailBerry Board, add and enable a MCP23017 board (default address 0x27) in the software settings.
Select *DC over I2C* as the pump type for all pumps, pin 0 is for pump 1 up till pin 9 for pump 10.
