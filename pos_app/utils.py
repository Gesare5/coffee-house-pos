from rich.console import Console
from rich.table import Table


def generate_table(data, columns, color, title):
    table = Table(title=title)
    rows = data
    for i, column in enumerate(columns):
        if len(color) > 1:
            table.add_column(column, style=color[i])
        else:
            table.add_column(column, style=color[0])

    for row in rows:
        table.add_row(*row)

    console = Console()
    console.print(table)