import eatpy

experiment = eatpy.models.GOTM(
    diagnostics_in_state=["total_chlorophyll_calculator_result"],
    fabm_parameters_in_state=["instances/phy/parameters/mumax0", "instances/dia/parameters/mumax0"]
)

filter = eatpy.PDAF(eatpy.pdaf.FilterType.ESTKF)

par_variables = [v for v in experiment.variables if v.startswith("instances")]
experiment.add_plugin(
    eatpy.plugins.select.Select(include=["temp", "salt", "total_chlorophyll_calculator_result"] + par_variables)
)
experiment.add_plugin(eatpy.plugins.check.Finite())
experiment.add_plugin(
    eatpy.plugins.transform.Log(
        "total_chlorophyll_calculator_result",
        *par_variables,
        transform_obs=False,
        minimum=1e-12
    )
)

# If you comment out the two lines below, you run the ensemble only without assimilation
experiment.add_observations("temp[-1]", "cci_sst.dat")
experiment.add_observations("total_chlorophyll_calculator_result[-1]", "cci_chl.dat")

experiment.run(filter)
