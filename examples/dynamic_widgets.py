import panel as pn

pn.extension()

selector = pn.widgets.Select(
    value=pn.widgets.ColorPicker, options=[
    pn.widgets.ColorPicker,
    pn.widgets.DatePicker,
    pn.widgets.FileInput,
    pn.widgets.FloatSlider,
    pn.widgets.RangeSlider,
    pn.widgets.Spinner,
    pn.widgets.TextInput,
], css_classes=['panel-widget-box'])

row = pn.Row(selector, pn.widgets.ColorPicker(), pn.pane.Str())
row.servable()

def update_value(event):
    row[2].object = 'Current Value: ' + str(event.new)

def update_widget(event):
    widget = event.new()
    widget.param.watch(update_value, 'value')
    widget.param.trigger('value')
    row[1] = widget

selector.param.watch(update_widget, 'value')
selector.param.trigger('value')

pn.Column(
    '## Dynamically generated user interfaces',
    row
)