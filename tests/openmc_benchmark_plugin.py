"""Reset OpenMC IDs between CSG and DAGMC models in benchmark comparisons."""


def pytest_runtest_setup(item):
    import openmc

    openmc.reset_auto_ids()
