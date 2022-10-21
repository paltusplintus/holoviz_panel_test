import param


class Exposure(param.Parameterized):
    date = param.Integer(default=None, constant=True)
    drug = param.String(default="", allow_None=False)

    def __init__(self, **params):
        super().__init__(**params)

    def get(self, key):
        return self.param[key]


class Subject(param.Parameterized):
    """Clinical Study Subject"""
    id = param.String(default="", regex="(^\d+\-\d+$)|(^$)", allow_None=False)
    exposure = param.List(default=[], class_=Exposure, item_type=Exposure,
                          instantiate=True)
    trtsdt = param.Dynamic(constant=True)

    def __init__(self, **params):
        super().__init__(**params)

        self._update_trtsdt()  # Sets the value trtsdt

    @param.depends("exposure", watch=True)
    def _update_trtsdt(self):
        """Updates trtsdt - sets to the earliest exposure"""
        with param.edit_constant(self):
            self.trtsdt = min(self.exposure, key=lambda x: x.__dict__['_date_param_value'])


# def print_event(event):
#     print(event, end='\n\n')
#
# watcher = pythagoras.param.watch(print_event, "c")

subj1 = Subject(
    id='001-001',
    exposure=[Exposure(drug="DRUG1", date=x) for x in [3, 4, 5, 6]]
)
#subj1=eval("Subject(exposure=[Exposure(date=3, drug='DRUG1', name='Exposure00002'), Exposure(date=4, drug='DRUG1', name='Exposure00003'), Exposure(date=5, drug='DRUG1', name='Exposure00004'), Exposure(date=6, drug='DRUG1', name='Exposure00005')], id='001-001', name='Subject00006', trtsdt=Exposure(date=3, drug='DRUG1', name='Exposure00002'))")

print(subj1.trtsdt.date)

import pprint
pprint.pprint(subj1)