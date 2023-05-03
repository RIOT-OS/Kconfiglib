import os
import glob
import kconfiglib
import pytest

CUR_DIR = os.path.dirname(os.path.realpath(__file__))


def test_bench_config(benchmark):
    """Evaluate the performance standard config file."""
    kconfig_path = CUR_DIR + '/Kconfig'

    kconf = kconfiglib.Kconfig(kconfig_path)
    benchmark(kconf.load_config, filename=CUR_DIR + '/app.config')


def test_bench_configpy(benchmark):
    """Evaluate the performance python config."""
    kconfig_path = CUR_DIR + '/Kconfig'

    kconf = kconfiglib.Kconfig(kconfig_path)
    benchmark(kconf.load_config, filename=CUR_DIR + '/config.py')


def test_bench_import_configpy(benchmark):
    """Evaluate the performance of importing."""
    kconfig_path = CUR_DIR + '/Kconfig'

    kconf = kconfiglib.Kconfig(kconfig_path)
    benchmark(kconf.load_config, filename=CUR_DIR + '/config.import.py')


def test_bench_import100_configpy(benchmark):
    """Evaluate the performance of importing foo 100 times."""
    kconfig_path = CUR_DIR + '/Kconfig'

    kconf = kconfiglib.Kconfig(kconfig_path)
    benchmark(kconf.load_config, filename=CUR_DIR + '/config.import100.py')


def test_bench_config1_configpy(benchmark):
    """Evaluate the performance of setting foo 1 time."""
    kconfig_path = CUR_DIR + '/Kconfig'

    kconf = kconfiglib.Kconfig(kconfig_path)
    benchmark(kconf.load_config, filename=CUR_DIR + '/config1.py')


def test_bench_config100_configpy(benchmark):
    """Evaluate the performance of setting foo 100 times."""
    kconfig_path = CUR_DIR + '/Kconfig'

    kconf = kconfiglib.Kconfig(kconfig_path)
    benchmark(kconf.load_config, filename=CUR_DIR + '/config100.py')
