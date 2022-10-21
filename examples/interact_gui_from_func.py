import panel as pn

from panel.interact import interact, interactive, fixed, interact_manual
from panel import widgets

pn.extension()

@interact(x=True, y=1.0)
def g(x, y):
    return (x, y)

pn.Column('**A custom interact layout**', pn.Row(*g).servable())
