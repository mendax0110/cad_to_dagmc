""""Reset OpenMC IDs between CSG and DAGMC models in benchmark comparisons."""


def pytest_runtest_setup(item):
    import openmc

    openmc.reset_auto_ids()


def pytest_configure(config):
    import openmc
    from model_benchmark_zoo.utils import BaseCommonGeometryObject

    dagmc_model = BaseCommonGeometryObject.dagmc_model

    def dagmc_model_with_fresh_ids(self, *args, **kwargs):
        openmc.reset_auto_ids()
        return dagmc_model(self, *args, **kwargs)

    BaseCommonGeometryObject.dagmc_model = dagmc_model_with_fresh_ids
