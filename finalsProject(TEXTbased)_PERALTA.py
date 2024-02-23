# this is for collection of favorite quotes

# EVERY NUMBER WILL DEFINE A SUBCLASS OR CLASS
#1 inspirational
#2 wisdom
#3 humorous
#4 literary
#5 motivational
#6 daily affirmation
#7 adventures 
import json
import os

class Qoutes:
    def __init__(self):
        self.inspi_quote = []
        self.wisdom_quote = []
        self.humor_quote = []
        self.literary_quote = []
        self.motivational_quote = []
        self.affirmation_quote = []
        self.adventure_quote = []

        print("Data loaded from JSON successfully")

    def save_to_json(self):
        data = {
            "inspirationalQuote": [inspi.__dict__ for inspi in self.inspi_quote],
            "WisdomQuote": [wisdom.__dict__ for wisdom in self.wisdom_quote],
            "HumorQuote": [humor.__dict__ for humor in self.humor_quote],
            "LiteraryQuote": [literary.__dict__ for literary in self.literary_quote],
            "MotivationalQuote": [motivational.__dict__ for motivational in self.motivational_quote],
            "AffirmationQuote": [affirmation.__dict__ for affirmation in self.affirmation_quote],
            "AdventureQuote": [adventure.__dict__ for adventure in self.adventure_quote],
        }
        with open("quotes.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Data saved to JSON successfully")

    def load_from_json(self):
        try:
            with open("quotes.json", "r") as file:
                data = json.load(file)
            for inspi_data in data["inspirationalQuote"]:
                inspirational = Inspirational(**inspi_data)
                self.inspi_quote.append(inspirational)
            for wisdom_data in data["WisdomQuote"]:
                wisdom = Wisdom(**wisdom_data)
                self.wisdom_quote.append(wisdom)
            for humor_data in data["HumorQuote"]:
                humor = Humorous(**humor_data)
                self.humor_quote.append(humor)
            for literary_data in data["LiteraryQuote"]:
                literary = Literary(**literary_data)
                self.literary_quote.append(literary)
            for motivation_data in data["MotivationalQuote"]:
                motivation = Motivational(**motivation_data)
                self.motivational_quote.append(motivation)
            for affirmation_data in data["AffirmationQuote"]:
                affirmation = Affirmation(**affirmation_data)
                self.affirmation_quote.append(affirmation)
            for adventure_data in data["AdventureQuote"]:
                adventure = Adventures(**adventure_data)
                self.adventure_quote.append(adventure)
            print("Data loaded from JSON successfully")
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError:
            print("Error decoding JSON data")

    def menu(self):
        while  True:
            try:
                def separator():
                    print("\n__________________________________________________________________________") #this separator is to highlight the Qoute list.

                def qoutes_choices():
                    print("\n1. Inspirational Quote")
                    print("2. Wisdom Quote")
                    print("3. Humor Quote")
                    print("4. Literary Quote")
                    print("5. Motivational Quote")
                    print("6. Affirmation Quote")
                    print("7. Adventure Quote")
                    print("8. Back")

                # os.system('cls')
                print("\nWELCOME TO FAVORITE QUOTES")
                print("\n1. Add quote")
                print("2. Display")
                print("3. Save to JSON.")
                print("4. Load from JSON")
                # try:
                choice1 = int(input("Enter Choice: "))
            

                if choice1 == 1: 
                    os.system('cls')
                    print("What Quote to add?")
                    qoutes_choices()
                    choice2 = int(input("Enter Choice: "))
                    
                    if choice2 == 1:
                        os.system('cls')
                        quote = input("Enter your Inspirational Quote: ")
                        author = input("Enter the Qoute's Author: ")
                        inspirational_quote = Inspirational(quote.title(), author.title())
                        self.inspi_quote.append(inspirational_quote)
                        print("Qoute Added Successfully!\n")
                    elif choice2 == 2:
                        os.system('cls')
                        quote = input("Enter your Wisdom Quote: ")
                        author = input("Enter the Qoute's Author: ")
                        wisdom_quote = Wisdom(quote.title(), author.title())
                        self.wisdom_quote.append(wisdom_quote)
                        print("Qoute Added Successfully!\n")
                    elif choice2 == 3:
                        os.system('cls')
                        quote = input("Enter your Humor Quote: ")
                        author = input("Enter the Qoute's Author: ")
                        humor_quote = Humorous(quote.title(), author.title())
                        self.humor_quote.append(humor_quote)
                        print("Qoute Added Successfully!\n")
                    elif choice2 == 4:
                        os.system('cls')
                        quote = input("Enter your Literary Quote: ")
                        author = input("Enter the Qoute's Author: ")
                        literary_quote = Literary(quote.title(), author.title())
                        self.literary_quote.append(literary_quote)
                        print("Qoute Added Successfully!\n")
                    elif choice2 == 5:
                        os.system('cls')
                        quote = input("Enter your Motivational Quote: ")
                        author = input("Enter the Qoute's Author: ")
                        motivational_quote = Motivational(quote.title(), author.title())
                        self.motivational_quote.append(motivational_quote)
                        print("Qoute Added Successfully!\n")
                    elif choice2 == 6:
                        os.system('cls')
                        quote = input("Enter your Affirmation Quote: ")
                        author = input("Enter the Qoute's Author: ")
                        affirmation_quote = Affirmation(quote.title(), author.title())
                        self.affirmation_quote.append(affirmation_quote)
                        print("Qoute Added Successfully!\n")
                    elif choice2 == 7:
                        os.system('cls')
                        quote = input("Enter your Adventure/Travel Quote: ")
                        author = input("Enter the Qoute's Author: ")
                        adventure_quote = Adventures(quote.title(), author.title())
                        self.adventure_quote.append(adventure_quote)
                        print("Qoute Added Successfully!\n")
                    # else:
                    #     print(choice1)

                elif choice1 == 2:
                    os.system('cls')
                    print("What Quote to Display?")
                    qoutes_choices()
                    choice3 = int(input("Enter your choice: "))
                    os.system('cls')
                    if choice3 == 1:
                        os.system('cls')
                        separator()
                        print("Inspirational Qoute List\n\n")
                        for index, inspi in enumerate(self.inspi_quote, start=1):
                            print([index],".",inspi)
                        separator()
                    elif choice3 == 2:
                        os.system('cls')
                        separator()
                        print("Wisdom Qoute List\n\n")
                        for index, wisdom in enumerate(self.wisdom_quote, start=1):
                            print([index],".",wisdom)
                        separator()
                    elif choice3 == 3:
                        separator()
                        print("Humor Qoute List\n\n")
                        for index, humor in enumerate(self.humor_quote, start=1):
                            print([index],".",humor)
                        separator()   
                    elif choice3 == 4:
                        separator()
                        print("Literary Qoute List\n\n")
                        for index, literary in enumerate(self.literary_quote, start=1):
                            print([index],".",literary)
                        separator()
                    elif choice3 == 5:
                        separator()
                        print("Motivational Qoute List\n\n")
                        for index, motivational in enumerate(self.motivational_quote, start=1):
                            print([index],".",motivational)
                        separator()
                    elif choice3 == 6:
                        separator()
                        print("Affirmation Qoute List\n\n")
                        for index, affirmation in enumerate(self.affirmation_quote, start=1):
                            print([index],".",affirmation)
                        separator()  
                    elif choice3 == 7:
                        separator()
                        print("Adventure Qoute List\n\n")
                        for index, adventure in enumerate(self.adventure_quote, start=1):
                            print([index],".",adventure)
                        separator()              
                    # else:
                    #     os.system('cls')
                    #     print(choice1)

                elif choice1 == 3:
                    self.save_to_json()

                elif choice1 == 4:
                    self.load_from_json()

                else:
                    print("program terminated")

            except ValueError:
                print("INVALID!Please enter a number only.")
                break   



class Inspirational(Qoutes):
    def __init__(self, inspi_quote, author):
        self.inspi_quote = inspi_quote
        self.author = author

    def __str__(self):
        return f"Inspirational Qoute: {self.inspi_quote.title()} \n      Author: {self.author.title()}"

class Wisdom(Qoutes):
    def __init__(self, wisdom_quote, author):
        self.wisdom_quote = wisdom_quote
        self.author = author

    def __str__(self):
        return f" Wisdom Qoute: {self.wisdom_quote.title()} \n      Author: {self.author.title()}"

class Humorous(Qoutes):
    def __init__(self, humor_quote, author):
        self.humor_quote = humor_quote
        self.author = author

    def __str__(self):
        return f" Humorous Qoute: {self.humor_quote.title()} \n      Author: {self.author.title()}"

class Literary(Qoutes):
    def __init__(self, literary_quote, author):
        self.literary_quote = literary_quote
        self.author = author

    def __str__(self):
        return f" Literary Qoute: {self.literary_quote.title()} \n      Author: {self.author.title()}"

class Motivational(Qoutes):
    def __init__(self, motivational_quote, author):
        self.motivational_quote = motivational_quote
        self.author = author

    def __str__(self):
        return f" Motivational Qoute: {self.motivational_quote.title()} \n      Author: {self.author.title()}"

class Affirmation(Qoutes):
    def __init__(self, affirmation_quote, author):
        self.affirmation_quote = affirmation_quote
        self.author = author

    def __str__(self):
        return f" Affirmation Qoute: {self.affirmation_quote.title()} \n      Author: {self.author.title()}"

class Adventures(Qoutes):
    def __init__(self, adventure_quote, author):
        self.adventure_quote = adventure_quote
        self.author = author

    def __str__(self):
        return f" Adventure Qoute: {self.adventure_quote.title()} \n      Author: {self.author.title()}"





if __name__=="__main__": 
    # ins = Inspirational("pray", "pastor")
    # print(ins)

    # wis = Wisdom("wisdom", "none")
    # print(wis)

    # hum = Humorous("humor", "none")
    # print(hum)

    # lit = Literary("litery", "none")
    # print(lit)

    # motive = Motivational("lijfadg", "none")
    # print(motive)
    collection = Qoutes()
    collection.menu()