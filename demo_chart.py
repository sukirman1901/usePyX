from pyx import ui, Lucide

def Bar_chart():
    return ui.chart.bar(
    labels=["Jan", "Feb", "Mar"],
    datasets=[{"label": "Sales", "data": [12, 19, 3], "color": "blue"}],
    title="Bar chart"
).p("[24px]").bg("[#ffffff]").border().border_color("[#e0e0e0]").rounded("[8px]")

app = App()
app.add_page("/", Bar_chart)

if __name__ == "__main__":
    app.run()
