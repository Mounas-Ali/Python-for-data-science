
from typing import Iterable
import time

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_length = 70
    start_time = time.time()

    print("Progression:")
    for i in range(total):
        progress = int((i / (total - 1)) * bar_length)
        bar = '[' + '■' * progress + ' ' * (bar_length - progress) + ']'
        print(f"{i + 1}/{total} {bar}", end='\r')
        time.sleep(0.005)

    end_time = time.time()
    elapsed_time = end_time - start_time

    m, s = divmod(elapsed_time, 60)
    h, m = divmod(m, 60)
    elapsed_time_formatted = f"{int(h):02d}:{int(m):02d}:{s:.2f}"

    progress_rate = total / elapsed_time if elapsed_time > 0 else 0

    print(f"\nTerminé! Temps écoulé: {elapsed_time_formatted} <00:00, {progress_rate:.2f}it/s>")
    return lst


