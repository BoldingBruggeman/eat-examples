import eatpy

experiment = eatpy.models.GOTM(
    diagnostics_in_state=["total_chlorophyll_calculator_result"]
)

filter = eatpy.PDAF(eatpy.pdaf.FilterType.ESTKF)

bgc_variables = [v for v in experiment.variables if "_" in v]
experiment.add_plugin(
    eatpy.plugins.select.Select(include=["temp", "salt"] + bgc_variables)
)
experiment.add_plugin(eatpy.plugins.check.Finite())
experiment.add_plugin(
    eatpy.plugins.transform.Log(
        "total_chlorophyll_calculator_result",
        *bgc_variables,
        transform_obs=False,
        minimum=1e-12
    )
)

# If you comment out the two lines below, you run the ensemble only without assimilation
# Note: if you are running ERGOM, replace total_chlorophyll_calculator_result with msi_ergom1_tot_chla
experiment.add_observations("temp[-1]", "cci_sst.dat")
experiment.add_observations("total_chlorophyll_calculator_result[-1]", "cci_chl.dat")

experiment.run(filter)
