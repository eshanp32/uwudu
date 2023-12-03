# (U w U)_/××××××  Custom styled table generation  ××××××\_(U w U)

import click
from prettytable import FRAME
from prettytable.colortable import ColorTable, Themes


class StyledTable:
    def __init__(self):
        self.table = ColorTable(theme=Themes.OCEAN)
        self.table.field_names = ["#", "Todo", "Status", "Created", "Updated"]

        self.style_table()

    def style_table(self):
        self.table.border = True
        self.table.preserve_internal_border = True
        self.table.header = True
        self.table.hrules = FRAME
        self.table.vrules = FRAME
        self.table.padding_width = 2

    def display(self, todo_list):
        self.table.clear_rows()
        pending_count = 0

        if len(todo_list) > 0:
            max_widths, pending_count = self.calculate_max_widths_and_pending_todos(
                todo_list
            )

            for idx, todo in enumerate(todo_list, start=1):
                todo_data = todo.split(" │ ")
                row_data = [idx, todo_data[1], todo_data[2], todo_data[3], todo_data[4]]

                row_data = [str(cell) for cell in row_data]

                row_data = [
                    f"\033[3m{cell}\033[0m" if isinstance(cell, str) else cell
                    for cell in row_data
                ]

                if isinstance(row_data[1], str):
                    row_data[1] = f"\033[96m{row_data[1]}\033[0m"

                row_data_aligned = [
                    str(cell).ljust(width) for cell, width in zip(row_data, max_widths)
                ]

                self.table.add_row(row_data_aligned)

        click.echo(self.table)

        click.echo(f"\nYou have {pending_count} pending todos.")

    def calculate_max_widths_and_pending_todos(self, todo_list):
        max_widths = [0] * len(todo_list[0].split(" │ "))
        count = 0

        for todo in todo_list:
            todo_data = todo.split(" │ ")
            if todo_data[2] == "ongoing":
                count += 1
            max_widths = [
                max(width, len(str(cell))) for width, cell in zip(max_widths, todo_data)
            ]

        return max_widths, count
