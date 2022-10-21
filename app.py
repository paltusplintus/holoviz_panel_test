#see intro to reactivity here: https://param.holoviz.org/
#see widget examples here: https://panel.holoviz.org/reference/index.html#
import panel as pn
import pandas as pd
pn.extension()

multi_choice = pn.widgets.MultiChoice(name='MultiSelect', value=['Apple', 'Pear'],
    options=[f"foo{str(i)}" for i in range(1,6)])
multi_choice.servable()

str_pane = pn.pane.Str('text', style={'font-size': '12pt'})
str_pane.servable()

df = pd._testing.makeMixedDataFrame()
df_pane = pn.pane.DataFrame(df, width=400)
df_pane.servable()

def update_str(event):
    str_pane.object = str(event.obj.value)
    df_pane.object = df[df["C"].map(lambda x: x in event.obj.value)]
watcher = multi_choice.param.watch(update_str, "value")

#run:
#Windows:
#venv\Scripts\python -m panel serve app.py --show --autoreload
#Unix:
#venv/bin/python -m panel serve app.py --show --autoreload
