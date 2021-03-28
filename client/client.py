import argparse
import computer
import logging
import json
import os
import sys
import subprocess
import webclient
from pathlib import Path

# ===============================================================================
#  GLOBAL DECLARATIONS
# ===============================================================================

# This logging is not impelented since there is no acuall need for it.
# Only here if it would be needed in the future.

log_file = "{}/client.log".format(Path(os.path.realpath(__file__)).parent)
logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    filename=log_file
                    )


# ===============================================================================
#  MAIN
# ===============================================================================


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(
        description='Sends inventory information to a webservice')
    parser.add_argument('-d', '--dry',
                        action='store_true',
                        help='dry run, no data sent to webservice')
    parser.add_argument('-u', '--users',
                        action='store_true',
                        help='list all users')
    parser.add_argument('-p', '--print',
                        action='store_true',
                        help='prints computer information')
    args = parser.parse_args()

    # Computer information
    computerObj = computer.Computer(args.users)
    computer = json.loads(json.dumps(computerObj.__dict__))

    # Print info
    if args.print:
        computerObj.Print()
    else:
        print(json.dumps(computer))

    # Update inventory
    if args.dry:
        sys.exit()
    webclient.update_inventory(computer["serialNumber"], computer)
