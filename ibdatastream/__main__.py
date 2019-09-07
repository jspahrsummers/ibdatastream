import logging

from argparse import ArgumentParser

from .server import Server

parser = ArgumentParser(
    prog="ibdatastream",
    description="Microservice to connect to Interactive Brokers and stream market data elsewhere",
    epilog="For more information, or to report issues, please visit: https://github.com/jspahrsummers/ib-data-stream",
)

parser.add_argument(
    "-v",
    "--verbose",
    help="Turns on more logging.",
    dest="verbose",
    default=False,
    action="store_true",
)


def main() -> None:
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    main()
