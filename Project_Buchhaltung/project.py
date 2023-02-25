# (Aufgabe 1)
import pandas as pd
budget_df = pd.read_csv("budget.csv", sep=";")
print(budget_df)
print(budget_df.info())

# (Aufgabe 2)
print()
result_one = (round(budget_df["In"].sum()))
print(result_one)
result_two = (round(budget_df["Out"].sum()))
print(result_two)
print(result_one - result_two)


# (Aufgabe 3)
print()
out_list = budget_df.groupby(["Category"], sort = True).sum()
print(out_list)

# (Aufgabe 4)
import seaborn as sns

sns.set_theme()

out_plot = sns.barplot(data = out_list, x = "Out", y = out_list.index)
out_plot.set_title("Ausgaben pro Kategorie")
out_plot.set_xlabel("Höhe der Ausgaben")
out_plot.set_ylabel("Kategorie")
out_plot.get_figure().savefig("expenses_per_category.png", bbox_inches='tight')
out_plot.figure.clf()

# (Bonus)

budget_df["Date"] = pd.to_datetime(budget_df["Date"], format = '%Y-%m-%d')
month = budget_df[["Date", "Out"]].groupby(pd.Grouper(key="Date", freq="M")).sum()
print(month)

sns_plot = sns.barplot(data = month, y = "Out", x = month.index.month_name())
sns_plot.set_title("Ausgaben pro Monat")
sns_plot.set_xlabel("Zeitraum in Monaten")
sns_plot.set_ylabel("Ausgaben")
sns_plot.get_figure().savefig("expenses_per_month.png", bbox_inches='tight')
sns_plot.figure.clf()

 





