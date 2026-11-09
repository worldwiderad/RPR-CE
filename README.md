# RPR-CE

Raspberry Pi Radio + Chess Encryption: sending encoded text messages between two Raspberry Pis over cheap 433 MHz radio modules. I built it in 2022.

`send.py` takes a lowercase message, turns each character into a 5-bit code (`binencode.py`), and transmits the bits one at a time through a GPIO-connected transmitter using [`rpi-rf`](https://github.com/milaq/rpi-rf). `recieve.py` listens on the other Pi and `bindecode.py` turns the bits back into text. The chess-based cipher that gives the project its name was the next step and never got built.

## Running it

On each Pi:

```sh
pip install rpi-rf
python3 recieve.py -g 27   # on the receiving Pi (GPIO pin, default 27)
python3 send.py -g 17      # on the sending Pi (GPIO pin, default 17)
```

`send.py` also takes `-p` for pulse length and `-t` for protocol.

## Log

`log.txt` is my build log. The short version: each Pi could hear its own transmitter but not the other one until I swapped the receivers around, and range was poor without antennas.
