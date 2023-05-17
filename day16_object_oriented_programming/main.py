from prettytable import PrettyTable
# create table object from the PrettyTable class
table = PrettyTable()
# call method
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# call attributes
table.align = "l"
print(table)