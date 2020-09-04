#import actions
import reactor
import action_timer
from time import sleep


def main():
    r = reactor.Reactor()
    r.start_watch()

if __name__ == "__main__":
    main()
