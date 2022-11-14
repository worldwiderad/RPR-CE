#!/usr/bin/env python3

import argparse
import logging
import binencode
from rpi_rf import RFDevice

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s',)

parser = argparse.ArgumentParser(description='Sends a decimal code via a 433/315MHz GPIO device')
parser.add_argument('-g', dest='gpio', type=int, default=17,
                    help="GPIO pin (Default: 17)")
parser.add_argument('-p', dest='pulselength', type=int, default=None,
                    help="Pulselength (Default: 350)")
parser.add_argument('-t', dest='protocol', type=int, default=None,
                    help="Protocol (Default: 1)")
args = parser.parse_args()

rfdevice = RFDevice(args.gpio)
rfdevice.enable_tx()

if args.protocol:
    protocol = args.protocol
else:
    protocol = "default"
if args.pulselength:
    pulselength = args.pulselength
else:
    pulselength = "default"

logging.info("Welcome to the RPR-CE, Raspberry Pi Radio and Chess Encyption")
user_input = input("Please enter an all-lowercase message with basic punctuation: ")

cipher = binencode.encode(user_input)

logging.info("Here is your encrypted message in binary: " + cipher)

for digit in cipher:
    logging.info("Sending digit: " + digit +
             " [protocol: " + str(protocol) +
             ", pulselength: " + str(pulselength) + "]")
    rfdevice.tx_code(int(digit) + 1, args.protocol, args.pulselength)

logging.info("Sent cipher: " + cipher +
             " [protocol: " + str(protocol) +
             ", pulselength: " + str(pulselength) + "]")

rfdevice.cleanup()
