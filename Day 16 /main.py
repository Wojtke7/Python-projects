from prettytable import PrettyTable

table = PrettyTable()
table.add_column("First column", ["One", "Two", "Three"])
table.add_column("Second column", ["Four", "Five", "Six"])
table.align = "l"
print(table)
