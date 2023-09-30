class Predecessors:
    strength = 100
    historyknowledge = 200

class Presenters(Predecessors):
    intellect = 100
    languageknowledge = 200

class Heirs(Presenters):
    sportskills = 150


w = Heirs()
day_str = ""
print(f"{day_str:=^30}", "\n")
print(f"Heirs Strength: {w.strength}\n")
print(f"{day_str:=^30}", "\n")
print(f"Heirs Historyknowledge: {w.historyknowledge}\n")
print(f"{day_str:=^30}", "\n")
print(f"Heirs Intellect: {w.intellect}\n")
print(f"{day_str:=^30}", "\n")
print(f"Heirs Languageknowledge: {w.languageknowledge}\n")
print(f"{day_str:=^30}", "\n")
print(f"Heirs Sportskills: {w.sportskills}\n")
print(f"{day_str:=^30}", "\n")
