import eatpy

experiment = eatpy.models.GOTM()

filter = eatpy.PDAF(eatpy.pdaf.FilterType.ESTKF)

experiment.add_plugin(eatpy.plugins.select.Select(include=("temp", "salt")))
experiment.add_plugin(eatpy.plugins.check.Finite())

# If you comment out the line below, you run the ensemble only, without assimilation
experiment.add_observations("temp[-1]", "cci_sst.dat")

experiment.run(filter)
