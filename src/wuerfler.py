import time
import concurrent.futures
from oscrypto import util

# z = wuerfe * 1000
z = 100000
ges = {'kopf': 0, 'zahl': 0}


def counter(counts):
    zaehler = counts
    e = {'kopf': 0, 'zahl': 0}
    while range(zaehler != 0):
        rnd = util.rand_bytes(1)
        rnd = int.from_bytes(rnd, byteorder='little')
        if rnd >= (255 / 2):
            e['zahl'] = e.get("zahl") + 1
        else:
            e['kopf'] = e.get("kopf") + 1
        zaehler = zaehler - 1
    return e


def sumup(g, a):
    ges['zahl'] = g.get('zahl') + a.get('zahl')
    ges['kopf'] = g.get('kopf') + a.get('kopf')
    return ges


if __name__ == '__main__':

    starttime = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(counter, z) for _ in range(1000)]
        for f in concurrent.futures.as_completed(results):
            sumup(ges, f.result())

        print(ges)
    endtime = time.perf_counter()
    print(f'Finished in {endtime - starttime} seconds')
