
import requests, json

x= requests.get("https://coronavirus-data.azurewebsites.net/api/countries?fbclid=IwAR1FBqet7jsaLQQbPwDiR9fE0iJcY1l52hRhxwaQncF1FB0YpDiJHcB1ZLE")
data = x.json()


x1 = requests.get("https://restcountries.eu/rest/v2/all")
data1 = x1.json()


new_dict = {
"Bolivia (Plurinational State of)":"Bolivia",
"Brunei Darussalam":"Brunei",
"Central African Republic":"Car",
"Czech Republic":"Czechia",
"Congo":"DRC",
"Faroe Islands":"Faeroe Islands",
"Iran (Islamic Republic of)":"Iran",
"Côte d'Ivoire":"Ivory Coast",
"Moldova (Republic of)":"Moldova",
"Macedonia (the former Yugoslav Republic of)":"North Macedonia",
"Palestine, State of":"Palestine",
"Russian Federation":"Russia",
"Korea (Republic Of)":"S. Korea",
"Saint Martin (French Part)":"Saint Martin",
"Saint Maarten (Dutch part)":"Sint Maarten",
"Saint Barthelémy":"St. Barth",
"Saint Vincent and the Grenadines":"St. Vincent Grenadines",
"Tanzania, United Republic of":"Tanzania",
"Virgin Islands (U.S.)":"U.S. Virgin Islands",
"United Arab Emirates":"Uae",
"United Kingdom of Great Britain and Northern Ireland":"Uk",
"United States of America":"Usa",
"Venezuela (Bolivarian Republic of)":"Venezuela",
"Viet Nam":"Vietnam"
}

def mapper():
    for c in data1:
        a = c["name"]
        b = None
        p = None
        d = None
        if a in new_dict:
            for x in new_dict:
                if a == x:
                    p = new_dict[x]
                    d = x
                    for z in data1:
                        if z["name"] == d:
                            z["name"] = p
                        else:
                            pass
        else:
            pass

    for c in data:
        if c["country"] == "USA":
            c["country"] = "Usa"
        if c["country"] == "UK":
            c["country"] = "Uk"
        if c["country"] == "UAE":
            c["country"] = "Uae"
        if c["country"] == "DRC":
            c["country"] = "Drc"


class Country:

    def __init__(self, country_choice):
        self.country_choice = country_choice

    def absolute_cases(self):
        g = None
        checker = False
        for c in data:
            b = c["country"]
            if self.country_choice == b:
                g = (c["cases"])
                print(self.country_choice + " has " + str(g) + " cases")
                checker = True
                break
        if checker == False:
            print("Country not found")
        return g

    def relative_cases(self):
        g = None
        population = None
        for c in data1:
            g = c["name"]
            if self.country_choice == g:
                population = c["population"]
            else:
                pass


        checker = False
        relative = None
        x = None

        for c in data:
            b = c["country"]
            if self.country_choice == b:
                x = (c["cases"])
                relative = int(x)/int(population) * 100000
                if relative != None:
                    print("Number of cases per 100000 inhabitatns: " + str(relative))
                    checker = True
            if checker == True:
                break
        return relative




def main():
    mapper()
    while True:
        User_choice = Country(input("type your country: ").title())
        User_choice.absolute_cases()
        User_choice.relative_cases()








main()
