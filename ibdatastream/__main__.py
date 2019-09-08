import asyncio
import logging
import random
import signal
from argparse import ArgumentParser

from . import server

parser = ArgumentParser(
    prog="ibdatastream",
    description="Microservice to connect to Interactive Brokers and stream market data elsewhere",
    epilog="For more information, or to report issues, please visit: https://github.com/jspahrsummers/ib-data-stream",
)

parser.add_argument(
    "-v",
    "--verbose",
    help="Turns on more logging. Stack multiple times to increase logging even further.",
    action="count",
)

parser.add_argument(
    "-p", "--port", help="The port to listen for incoming connections on.", dest="port"
)


def main() -> None:
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG if args.verbose >= 2 else logging.INFO)

    port = args.port or random.randint(49152, 65535)
    server.start(port)
    print(f"Server listening on port {port}")

    # Install SIGINT handler. This is apparently necessary for the process to be interruptible with Ctrl-C on Windows:
    # https://bugs.python.org/issue23057
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
