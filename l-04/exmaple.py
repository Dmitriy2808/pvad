import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig


DT = 0.02
FS = 50

FILTER_LEN = 301


def ex_zero_anomaly():
    """Effect of zero for the filtration."""
    T = 60
    f1 = 0.25
    a1 = 1
    f2 = 3
    a2 = 0.05

    ts = np.arange(0, T, DT)
    h1 = a1 * np.cos(2*np.pi*f1*ts) + 50
    h2 = a2 * np.cos(2*np.pi*f2*ts) + 50
    xs = h1 + h2

    h = sig.firwin(cutoff=[2, 4], pass_zero=False,
                   fs=FS, numtaps=FILTER_LEN)
    xf = sig.lfilter(h, [1], xs)

    xs[len(xs)//2] = 0
    xfz = sig.lfilter(h, [1], xs)

    plt.subplot(311)
    plt.plot(ts, xs)
    plt.grid(True)

    plt.subplot(312)
    plt.plot(ts[FILTER_LEN:], xf[FILTER_LEN:])
    plt.grid(True)

    plt.subplot(313)
    plt.plot(ts[FILTER_LEN:], xfz[FILTER_LEN:])
    plt.grid(True)


def ex_jumps_anomaly():
    """Effect of number of jumps for the filtration."""
    T = 60
    f1 = 0.25
    a1 = 1
    f2 = 3
    a2 = 0.05

    ts = np.arange(0, T, DT)
    h1 = a1 * np.cos(2*np.pi*f1*ts) + 50
    h2 = a2 * np.cos(2*np.pi*f2*ts) + 50
    xs = h1 + h2

    for i in range(5):
        xs[len(xs)//2 + i*50] = 0

    h = sig.firwin(cutoff=[2, 4], pass_zero=False,
                   fs=FS, numtaps=FILTER_LEN)
    xf = sig.lfilter(h, [1], xs)

    plt.subplot(211)
    plt.plot(ts, xs)
    plt.grid(True)

    plt.subplot(212)
    plt.plot(ts[FILTER_LEN:], xf[FILTER_LEN:])
    plt.grid(True)


def ex_long_zero_anomaly():
    """Effect of long zero for the filtration."""
    T = 60
    f1 = 0.25
    a1 = 1
    f2 = 3
    a2 = 0.05

    ts = np.arange(0, T, DT)
    h1 = a1 * np.cos(2*np.pi*f1*ts) + 50
    h2 = a2 * np.cos(2*np.pi*f2*ts) + 50
    xs = h1 + h2

    xs[len(xs)//2-300:len(xs)//2] = 0

    h = sig.firwin(cutoff=[2, 4], pass_zero=False,
                   fs=FS, numtaps=FILTER_LEN)
    xf = sig.lfilter(h, [1], xs)

    plt.subplot(211)
    plt.plot(ts, xs)
    plt.grid(True)

    plt.subplot(212)
    plt.plot(ts[FILTER_LEN:], xf[FILTER_LEN:])
    plt.grid(True)


def ex_skip():
    """Skip one value."""
    ts = np.arange(0, 60, DT)
    xs = np.cos(2*np.pi*3*ts)

    xs[len(xs)//2] = None

    h = sig.firwin(cutoff=[2, 4], pass_zero=False, fs=FS,
                   numtaps=FILTER_LEN)
    xf = sig.lfilter(h, [1], xs)
    plt.plot(ts[FILTER_LEN:], xf[FILTER_LEN:])


def run_vis_example(func, save=True):
    """Runs example with single figure output."""
    if save:
        fig = plt.figure()
        func()
        plt.tight_layout()
        plt.savefig("{}.png".format(func.__name__))
        plt.close(fig)
        return

    func()
    plt.show()


def run_text_example(func):
    """Runs example with text output."""
    print("Ex: {}".format(func.__doc__))
    func()
    print()


# run_vis_example(ex_zero_anomaly, save=False)
# run_vis_example(ex_jumps_anomaly, save=False)
# run_vis_example(ex_long_zero_anomaly, save=False)
run_vis_example(ex_skip, save=False)
