import pandas
# name = ["Dhanu","sid","adinath"]
# mark = [90,80,70]
# college = ["SGMCOE","SGMCOE","SGMCOE"]
# x = {"name" :name, "mark":mark, "college": college}
# d = pandas.DataFrame(x)
# print(d)

# name = ["Dhanu","sid","adinath"]
# mark = [90,80,70]
# college = ["SGMCOE","SGMCOE","SGMCOE"]
# x = {"name" :name, "mark":mark, "college": college}
# d = pandas.DataFrame(x,index=[1,2,3])
# print(d)

# read csv

# z = pandas.read_csv(r"C:\Users\ASUS\OneDrive\Documents\Desktop\Football_teams_price_data.csv")
# print(z)

# read excel

z1 = pandas.read_excel(r"C:\Users\ASUS\OneDrive\Documents\Desktop\pd.xlsx")
# print(z1)

print(z1.duplicated())

# print(z1.drop_duplicates())