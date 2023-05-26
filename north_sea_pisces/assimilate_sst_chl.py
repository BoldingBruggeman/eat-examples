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
experiment.add_plugin(eatpy.plugins.output.NetCDFStats('ensemble_stats.nc'))

#experiment.add_observations("temp[-1]", "cci_sst.dat")
#experiment.add_observations("total_chlorophyll_calculator_result[-1]", "cci_chl.dat")
import datetime
experiment.add_dummy_observations([(datetime.datetime(2020,1,2)+datetime.timedelta(days=i)) for i in range(3*365)])

experiment.run(filter)
