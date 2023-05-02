import os
import glob
import kconfiglib
import pytest

CUR_DIR = os.path.dirname(os.path.realpath(__file__))

@pytest.mark.parametrize("config_file",
                         sorted(glob.glob(CUR_DIR + '/config*.py',
                                          recursive=True)))
def test_configs_should_not_crash(config_file):
    """Test config files that should not crash.

    No asserts are used as we are just looking for exceptions.
    """
    kconfig_path = CUR_DIR + '/Kconfig'

    kconf = kconfiglib.Kconfig(kconfig_path, suppress_traceback=True)
    kconf.load_config(filename=config_file)


@pytest.mark.parametrize("config_file",
                         sorted(glob.glob(CUR_DIR + '/fail.config*.py',
                                          recursive=True)))
def test_configs_should_crash(config_file):
    """Test config files that should not crash.

    No asserts are used as we are just looking for exceptions.
    """
    kconfig_path = CUR_DIR + '/Kconfig'

    kconf = kconfiglib.Kconfig(kconfig_path, warn=False)
    with pytest.raises(Exception):
        kconf.load_config(filename=config_file)
