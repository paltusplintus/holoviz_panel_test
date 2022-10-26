import param
import math

class PythagoreanTheorem(param.Parameterized):
    """Model of the Pythagorean Theorem"""

    a = param.Number(default=0, bounds=(0, None), doc="Length of side a")
    b = param.Number(default=0, bounds=(0, None), doc="Length of side b")
    c = param.Number(default=0, bounds=(0, None), doc="Length of the hypotenuse c",
                     constant=True)

    def __init__(self, **params):
        super().__init__(**params)  # Sets values a and b if provided in the params

        self._update_hypotenuse()  # Sets the value c

    @param.depends("a", "b", watch=True)  # Triggers a run of the function whenever a or b is changed
    def _update_hypotenuse(self):
        """Updates the length of the hypotenuse"""
        with param.edit_constant(self):
            self.c = math.sqrt(self.a ** 2 + self.b ** 2)


# def print_event(event):
#     print(event, end='\n\n')
#
# watcher = pythagoras.param.watch(print_event, "c")