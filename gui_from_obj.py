import param
import panel as pn
from param_examples.PythagoreanTheorem import PythagoreanTheorem

pn.extension()
obj = PythagoreanTheorem(a=1, b=2)
pn.Param(obj).servable()
