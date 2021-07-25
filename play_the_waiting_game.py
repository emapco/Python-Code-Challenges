import random as r
import time as t

# calculates time elapsed between subsequent 'Enter' button presses
# outputs comparison of time elapsed to waiting time
def waiting_game():
    waiting_time = r.randint(1, 6)
    print(f"Your target time is {waiting_time} seconds.")

    input("--- Press Enter to Begin---\n")
    beginning_time = t.perf_counter()

    input(f"...Press Enter again after {waiting_time} seconds...\n")
    ending_time = t.perf_counter()

    elapsed_time = round((ending_time - beginning_time), 3)
    abs_difference = abs(elapsed_time-waiting_time)
    print("Elapsed time: {:.3f} seconds".format(elapsed_time))
    if elapsed_time > waiting_time:
        print("({:.3f} seconds too slow)".format(abs_difference))
    elif elapsed_time < waiting_time:
        print("({:.3f} seconds too fast)".format(abs_difference))
    else:
        print("(You pressed Enter right on time!)")


def solution():
    target = r.randint(2, 4)
    print(f"\nYour target time is {target} seconds.")

    input("--- Press Enter to Begin---\n")
    start = t.perf_counter()

    input(f"...Press Enter again after {target} seconds...\n")
    elapsed = t.perf_counter() - start

    print("Elapsed time: {0:.3f} seconds".format(elapsed))
    if elapsed == target:
        print("(Unbelievable! Perfect timing!)")
    elif elapsed < target:
        print("({0:.3f} seconds too fast)".format(target - elapsed))
    else:
        print("({0:.3f} seconds too slow)".format(elapsed - target))


if __name__ == '__main__':
    waiting_game()