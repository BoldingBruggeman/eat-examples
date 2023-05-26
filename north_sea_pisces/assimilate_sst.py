import eatpy

experiment = eatpy.models.GOTM()

filter = eatpy.PDAF(eatpy.pdaf.FilterType.ESTKF)

experiment.add_plugin(eatpy.plugins.select.Select(include=("temp", "salt")))
experiment.add_plugin(eatpy.plugins.check.Finite())

experiment.add_observations("temp[-1]", "cci_sst.dat")

experiment.run(filter)
