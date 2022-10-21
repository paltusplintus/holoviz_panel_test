import panel as pn
import asyncio

pn.extension()

button = pn.widgets.Button(name='Click me!')
text = pn.widgets.StaticText()

async def run_async(event):
    text.value = f'Running {event.new}'
    await asyncio.sleep(2)
    text.value = f'Finished {event.new}'

button.on_click(run_async)

pn.Row(button, text).servable()