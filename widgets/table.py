import curses
from curses import panel


class Table:
    def __init__(self, parent, row_labels, col_labels, data):
        self.parent = parent
        self.row_labels = row_labels
        self.col_labels = col_labels
        self.data = data
        self.panel = None

    def draw(self):
        height, width = self.parent.getmaxyx()

        # Create window for the table
        table_height = len(self.row_labels) + 2
        table_width = len(self.col_labels) * 10 + 2
        table_y = (height - table_height) // 2
        table_x = (width - table_width) // 2
        table_win = curses.newwin(table_height, table_width, table_y, table_x)

        # Draw border around table
        table_win.border()

        # Add column labels
        for i, label in enumerate(self.col_labels):
            table_win.addstr(1, 2 + i * 10, label)

        # Add row labels and data
        for i, label in enumerate(self.row_labels):
            table_win.addstr(i + 2, 1, label)
            for j, value in enumerate(self.data[i]):
                table_win.addstr(i + 2, 2 + j * 10, str(value))

        # Refresh the table window
        table_win.refresh()

        # Create a panel for the table
        self.panel = panel.new_panel(table_win)

    def show(self):
        self.panel.top()
        self.panel.show()
        curses.doupdate()

    def hide(self):
        self.panel.hide()
        curses.doupdate()
