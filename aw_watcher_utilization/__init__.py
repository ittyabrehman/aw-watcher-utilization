import argparse

from aw_core.log import setup_logging

from aw_watcher_utilization.watcher import UtilizationWatcher


def main() -> None:
    # Set up argparse
    parser = argparse.ArgumentParser("An Activity Watch watcher which monitors CPU, RAM, GPU and disk usage.")
    parser.add_argument("-v", "--verbose", dest='verbose', action="store_true",
                        help='run with verbose logging')
    parser.add_argument("--testing", action="store_true",
                        help='run in testing mode')
    parser.add_argument("--host", dest="aw_host", default=None,
        help="ActivityWatch server hostname (overrides config)")
    parser.add_argument("--port", dest="aw_port", type=int, default=None,
        help="ActivityWatch server port (overrides config)")

    args = parser.parse_args()

    # Set up logging
    setup_logging("aw-watcher-utilization",
                  testing=args.testing, verbose=args.verbose,
                  log_stderr=True, log_file=True)

    # Start watcher
    watcher = UtilizationWatcher(
        testing=args.testing,
        host=args.aw_host,
        port=args.aw_port,
    )
    watcher.run()


if __name__ == "__main__":
    main()
