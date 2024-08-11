from bokeh.layouts import column
from bokeh.models import Range1d, DatetimeTickFormatter, RangeTool
from bokeh.plotting import figure, show
from extract_data import getData

### Prepare data
data = getData()

### Create plot and range tool
detailed_plot = figure(
    width=800,
    height=300,
    title='Data Pengujian Jaringan (30 Juli - 8 Agustus 2024)',
    x_range=Range1d(start=data['date_time'][0], end=data['date_time'][30]),
    x_axis_type="datetime",
    x_axis_label='Date Time',
    y_axis_label='Speed (Mbps)',
    tools=['xpan', 'xzoom_in', 'xzoom_out', 'reset', 'wheel_zoom'],
    toolbar_location='above',
)

detailed_plot.xaxis.formatter = DatetimeTickFormatter(days='%d %b', hours='%H:%M', minutes='%H:%M')

avg_plot = figure(
    width=800,
    height=200,
    x_axis_type="datetime",
    x_axis_label='Date',
    y_axis_label='Speed (Mbps)',
    tools='',
    toolbar_location='above'
)

range_tool = RangeTool(x_range=detailed_plot.x_range)
range_tool.overlay.fill_color = 'navy'
range_tool.overlay.fill_alpha = 0.2

avg_plot.xaxis.formatter = DatetimeTickFormatter(days='%d %b %y')
avg_plot.x_range.range_padding = 0
avg_plot.add_tools(range_tool)

### Add line graph to plot
detailed_plot.line(data['date_time'], data['sender_avg_speed'], legend_label="Sender", line_width=2, color='#518494')
avg_plot.line(data['date_time'], data['sender_avg_speed'], legend_label="Sender", line_width=1, color='#188653')

### Show result
show(column(detailed_plot, avg_plot))