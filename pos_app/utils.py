from rich.console import Console
from rich.table import Table


def generate_table(data, columns, color, title):
    table = Table(title=title)
    rows = data
    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row, style=color)

    console = Console()
    console.print(table)
