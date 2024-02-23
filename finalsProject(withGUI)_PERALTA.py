import tkinter as tk
from tkinter import ttk, messagebox
import json
from os.path import isfile

class MyButton:
    def __init__(self, root, width, text, bg, fg, command, row, column, sticky):
        self.button = tk.Button(root, width=width, text=text, bg=bg, fg=fg, command=command)
        self.button.grid(row=row, column=column, padx=10, pady=(5,0), sticky=sticky)
        self.button.bind("<Enter>", self.on_enter)
        self.button.bind("<Leave>", self.on_leave)

        #this is for buttonbind
    def on_enter(self, event):
        event.widget.config(bg='#003f5c', fg="khaki")

    def on_leave(self, event):
        event.widget.config(bg="khaki", fg="#003f5c")

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" ")

        # Create LabelFrame
        self.lf = tk.LabelFrame(root)
        self.lf.grid(row=0, column=0, padx=10, ipady=10)
        self.lf2 = tk.LabelFrame(root)
        self.lf3 = tk.LabelFrame(root)
        self.lf4 = tk.LabelFrame(root)

        # Create buttons using MyButton class
        self.add = MyButton(self.lf, 12, "Add Quote", "khaki", "#003f5c", self.on_add ,0,0,'w')
        
        # self.save = MyButton(self.lf, 12, "Save to JSON", "khaki", "#003f5c", self.on_save ,2,0,'w')
        self.load = MyButton(self.lf, 12, "Load from JSON", "khaki", "#003f5c", self.on_load ,2,0,'w')
        self.exit = MyButton(self.lf, 12, "Exit", "khaki", "#003f5c", self.on_exit ,3,0,'w')

    def entry(self):
        self.lf2.grid_forget()
        self.lf3.grid(row=0, column=0, padx=5, ipady=5)
        self.author = tk.Entry(self.lf3, width=30, bg='lightblue')
        self.author.insert(0, "Enter Quote Here!")
        self.author.bind("<FocusIn>", lambda e:self.author.delete(0, 'end') )
        self.author.grid(row=0, column=0, padx=5) 
        self.quote = tk.Entry(self.lf3, width=30, bg='lightblue')
        self.quote.insert(0, "Enter Your Author Here!")
        self.quote.bind("<FocusIn>", lambda e:self.quote.delete(0, 'end') )
        self.quote.grid(row=1, column=0, padx=5, pady=(5,0))

        self.backll = MyButton(self.lf3, 10, "Back", "khaki", "#003f5c", self.back2 ,2,0, 'e')

    def displayQ(self):
        self.lf.grid_forget()
        self.lf2.grid(row=0, column=0, padx=10, ipady=10)
        self.inspirational = MyButton(self.lf2, 20, "Inspirational Quote", "khaki", "#003f5c", self.display_inspirational ,0,0,'w')
        self.wisdom = MyButton(self.lf2, 20, "Wisdom Quote", "khaki", "#003f5c", self.display_wisdom ,1,0,'w')
        self.humor = MyButton(self.lf2, 20, "Humorous Quote", "khaki", "#003f5c", self.display_humor ,2,0,'w')
        self.literary = MyButton(self.lf2, 20, "Literary Quote", "khaki", "#003f5c", self.display_literary ,3,0,'w')
        self.motivational = MyButton(self.lf2, 20, "Motivational Quote", "khaki", "#003f5c", self.display_motivational ,4,0,'w')
        self.affirmation = MyButton(self.lf2, 20, "Affirmation Quote", "khaki", "#003f5c", self.display_affirmation ,5,0,'w')
        self.adventure = MyButton(self.lf2, 20, "Adventure Quote", "khaki", "#003f5c", self.display_adventure ,6,0,'w')
        self.back = MyButton(self.lf2, 20, "Back", "khaki", "#003f5c", self.backQ ,7,0,'w')

    #this is for button function
    def on_add(self):
        self.lf.grid_forget()
        self.lf2.grid(row=0, column=0, padx=10, ipady=10)
        self.inspirational = MyButton(self.lf2, 20, "Inspirational Quote", "khaki", "#003f5c", self.inspirationalQ ,0,0,'w')
        self.wisdom = MyButton(self.lf2, 20, "Wisdom Quote", "khaki", "#003f5c", self.wisdomQ ,1,0,'w')
        self.humor = MyButton(self.lf2, 20, "Humorous Quote", "khaki", "#003f5c", self.humorQ ,2,0,'w')
        self.literary = MyButton(self.lf2, 20, "Literary Quote", "khaki", "#003f5c", self.literaryQ ,3,0,'w')
        self.motivational = MyButton(self.lf2, 20, "Motivational Quote", "khaki", "#003f5c", self.motivationalQ ,4,0,'w')
        self.affirmation = MyButton(self.lf2, 20, "Affirmation Quote", "khaki", "#003f5c", self.affirmationQ ,5,0,'w')
        self.adventure = MyButton(self.lf2, 20, "Adventure Quote", "khaki", "#003f5c", self.adventureQ ,6,0,'w')
        self.back = MyButton(self.lf2, 20, "Back", "khaki", "#003f5c", self.backQ ,7,0,'w')

    def inspirationalQ(self):
        self.entry()  
        self.save = MyButton(self.lf3, 10, "Save", "khaki", "#003f5c", self.save_inspirational ,2,0, 'w')

    def wisdomQ(self):
        self.entry()
        self.save = MyButton(self.lf3, 10, "Save", "khaki", "#003f5c", self.save_wisdom ,2,0, 'w')

    def humorQ(self):
        self.entry()
        self.save = MyButton(self.lf3, 10, "Save", "khaki", "#003f5c", self.save_humor ,2,0, 'w')

    def literaryQ(self):
        self.entry()
        self.save = MyButton(self.lf3, 10, "Save", "khaki", "#003f5c", self.save_literary ,2,0, 'w')

    def motivationalQ(self):
        self.entry()
        self.save = MyButton(self.lf3, 10, "Save", "khaki", "#003f5c", self.save_motivational ,2,0, 'w')

    def affirmationQ(self):
        self.entry()
        self.save = MyButton(self.lf3, 10, "Save", "khaki", "#003f5c", self.save_affirmation ,2,0, 'w')

    def adventureQ(self):
        self.entry()
        self.save = MyButton(self.lf3, 10, "Save", "khaki", "#003f5c", self.save_adventure ,2,0, 'w')

    def backQ(self):
        self.lf2.grid_forget()
        self.lf.grid(row=0, column=0, padx=10, ipady=10)

    def back2(self):
        self.lf3.grid_forget()
        self.lf2.grid(row=0, column=0, padx=10, ipady=10)

    def back3(self):
        self.lf4.grid_forget()
        self.lf2.grid(row=0, column=0, padx=10, ipady=10)

    def on_display(self):
        self.displayQ()

    def save_inspirational(self):
        try:
            quote = self.quote.get()
            author = self.author.get()
            new_data = {"Quote": author.upper(), "Author": quote.title()}

            if quote == "Enter Your Author Here!" or  quote == "" or quote == "Quote" or quote == "quote":
                messagebox.showerror("INVALID",f"Please Enter your Quote first before saving.")
            elif author == "Enter Quote Here!" or author == "" or author == "Author" or author == "author":
                messagebox.showerror("INVALID",f"Please Enter your Author first before saving.")
            elif quote == author:
                messagebox.showerror("INVALID",f"The Quote and Author cannot be the same.")
            else:

                if isfile("inspirational.json"):
                    # Read existing data from the JSON file
                    with open("inspirational.json", "r") as json_file:
                        existing_data = json.load(json_file)
                    
                    # Append the new data to the list of inputs
                    existing_data["Inspirational"].append(new_data)
                else:
                    # If the file doesn't exist, start with a list containing the new data
                    existing_data = {"Inspirational": [new_data]}

                # Write the updated data to the JSON file
                with open("inspirational.json", "w") as json_file:
                    json.dump(existing_data, json_file, indent=2)
                self.root.withdraw()
                messagebox.showinfo("NOTICE!",f"Quote:{author.title()}\nAuthor:{quote.title()} \n\n\nYour Quote has been saved") 
                self.display_inspirational()
                self.root.deiconify()
                self.lf3.grid_forget()
                self.lf2.grid(row=0, column=0, padx=10, ipady=10)
            for data in existing_data:
               self.tree.insert("", "end", values=(data['Quote'], data['Author']))   
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError:
            print("Error decoding JSON data")

    def save_wisdom(self):
        try:
            quote = self.quote.get()
            author = self.author.get()
            new_data = {"Quote": author.upper(), "Author": quote.title()}

            if quote == "Enter Your Author Here!" or  quote == "" or quote == "Quote" or quote == "quote":
                messagebox.showerror("INVALID",f"Please Enter your Quote first before saving.")
            elif author == "Enter Quote Here!" or author == "" or author == "Author" or author == "author":
                messagebox.showerror("INVALID",f"Please Enter your Author first before saving.")
            elif quote == author:
                messagebox.showerror("INVALID",f"The Quote and Author cannot be the same.")
            else:
                if isfile("wisdom.json"):
                    # Read existing data from the JSON file
                    with open("wisdom.json", "r") as json_file:
                        existing_data = json.load(json_file)
                    
                    # Append the new data to the list of inputs
                    existing_data["Wisdom"].append(new_data)
                else:
                    # If the file doesn't exist, start with a list containing the new data
                    existing_data = {"Wisdom": [new_data]}

                # Write the updated data to the JSON file
                with open("wisdom.json", "w") as json_file:
                    json.dump(existing_data, json_file, indent=2)
                self.root.withdraw()
                messagebox.showinfo("NOTICE!",f"Quote:{author.title()}\nAuthor:{quote.title()} \n\n\nYour Quote has been saved")
                self.display_wisdom()
                self.root.deiconify()
                self.lf3.grid_forget()
                self.lf2.grid(row=0, column=0, padx=10, ipady=10)
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError:
            print("Error decoding JSON data")

    def save_humor(self):
        try:
            quote = self.quote.get()
            author = self.author.get()
            new_data = {"Quote": author.upper(), "Author": quote.title()}

            if quote == "Enter Your Author Here!" or  quote == "" or quote == "Quote" or quote == "quote":
                messagebox.showerror("INVALID",f"Please Enter your Quote first before saving.")
            elif author == "Enter Quote Here!" or author == "" or author == "Author" or author == "author":
                messagebox.showerror("INVALID",f"Please Enter your Author first before saving.")
            elif quote == author:
                messagebox.showerror("INVALID",f"The Quote and Author cannot be the same.")
            else:

                if isfile("humor.json"):
                    # Read existing data from the JSON file
                    with open("humor.json", "r") as json_file:
                        existing_data = json.load(json_file)
                    
                    # Append the new data to the list of inputs
                    existing_data["Humorous"].append(new_data)
                else:
                    # If the file doesn't exist, start with a list containing the new data
                    existing_data = {"Humorous": [new_data]}

                # Write the updated data to the JSON file
                with open("humor.json", "w") as json_file:
                    json.dump(existing_data, json_file, indent=2)
                self.root.withdraw()
                messagebox.showinfo("NOTICE!",f"Quote:{author.title()}\nAuthor:{quote.title()} \n\n\nYour Quote has been saved")
                self.display_humor()
                self.root.deiconify()
                self.lf3.grid_forget()
                self.lf2.grid(row=0, column=0, padx=10, ipady=10)
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError:
            print("Error decoding JSON data")

    def save_literary(self):
        try:
            quote = self.quote.get()
            author = self.author.get()
            new_data = {"Quote": author.upper(), "Author": quote.title()}

            if quote == "Enter Your Author Here!" or  quote == "" or quote == "Quote" or quote == "quote":
                messagebox.showerror("INVALID",f"Please Enter your Quote first before saving.")
            elif author == "Enter Quote Here!" or author == "" or author == "Author" or author == "author":
                messagebox.showerror("INVALID",f"Please Enter your Author first before saving.")
            elif quote == author:
                messagebox.showerror("INVALID",f"The Quote and Author cannot be the same.")
            else:
                if isfile("literary.json"):
                    # Read existing data from the JSON file
                    with open("literary.json", "r") as json_file:
                        existing_data = json.load(json_file)
                    
                    # Append the new data to the list of inputs
                    existing_data["Literary"].append(new_data)
                else:
                    # If the file doesn't exist, start with a list containing the new data
                    existing_data = {"Literary": [new_data]}

                # Write the updated data to the JSON file
                with open("literary.json", "w") as json_file:
                    json.dump(existing_data, json_file, indent=2)
                self.root.withdraw()
                messagebox.showinfo("NOTICE!",f"Quote:{author.title()}\nAuthor:{quote.title()} \n\n\nYour Quote has been saved")
                self.display_literary()
                self.root.deiconify()
                self.lf3.grid_forget()
                self.lf2.grid(row=0, column=0, padx=10, ipady=10)
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError:
            print("Error decoding JSON data")

    def save_motivational(self):
        try:
            quote = self.quote.get()
            author = self.author.get()
            new_data = {"Quote": author.upper(), "Author": quote.title()}

            if quote == "Enter Your Author Here!" or  quote == "" or quote == "Quote" or quote == "quote":
                messagebox.showerror("INVALID",f"Please Enter your Quote first before saving.")
            elif author == "Enter Quote Here!" or author == "" or author == "Author" or author == "author":
                messagebox.showerror("INVALID",f"Please Enter your Author first before saving.")
            elif quote == author:
                messagebox.showerror("INVALID",f"The Quote and Author cannot be the same.")
            else:
                if isfile("motivational.json"):
                    # Read existing data from the JSON file
                    with open("motivational.json", "r") as json_file:
                        existing_data = json.load(json_file)
                    
                    # Append the new data to the list of inputs
                    existing_data["Motivational"].append(new_data)
                else:
                    # If the file doesn't exist, start with a list containing the new data
                    existing_data = {"Motivational": [new_data]}

                # Write the updated data to the JSON file
                with open("motivational.json", "w") as json_file:
                    json.dump(existing_data, json_file, indent=2)
                self.root.withdraw()
                messagebox.showinfo("NOTICE!",f"Quote:{author.title()}\nAuthor:{quote.title()} \n\n\nYour Quote has been saved")
                self.display_motivational()
                self.root.deiconify()
                self.lf3.grid_forget()
                self.lf2.grid(row=0, column=0, padx=10, ipady=10)
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError:
            print("Error decoding JSON data")

    def save_affirmation(self):
        try:
            quote = self.quote.get()
            author = self.author.get()
            new_data = {"Quote": author.upper(), "Author": quote.title()}

            if quote == "Enter Your Author Here!" or  quote == "" or quote == "Quote" or quote == "quote":
                messagebox.showerror("INVALID",f"Please Enter your Quote first before saving.")
            elif author == "Enter Quote Here!" or author == "" or author == "Author" or author == "author":
                messagebox.showerror("INVALID",f"Please Enter your Author first before saving.")
            elif quote == author:
                messagebox.showerror("INVALID",f"The Quote and Author cannot be the same.")
            else:
                if isfile("affirmation.json"):
                    # Read existing data from the JSON file
                    with open("affirmation.json", "r") as json_file:
                        existing_data = json.load(json_file)
                    
                    # Append the new data to the list of inputs
                    existing_data["Affirmation"].append(new_data)
                else:
                    # If the file doesn't exist, start with a list containing the new data
                    existing_data = {"Affirmation": [new_data]}
                # Write the updated data to the JSON file
                with open("affirmation.json", "w") as json_file:
                    json.dump(existing_data, json_file, indent=2)
                self.root.withdraw()
                messagebox.showinfo("NOTICE!",f"Quote:{author.title()}\nAuthor:{quote.title()} \n\n\nYour Quote has been saved")
                self.display_affirmation()
                self.root.deiconify()
                self.lf3.grid_forget()
                self.lf2.grid(row=0, column=0, padx=10, ipady=10)
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError:
            print("Error decoding JSON data")

    def save_adventure(self):
        try:
            quote = self.quote.get()
            author = self.author.get()
            new_data = {"Quote": author.upper(), "Author": quote.title()}

            if quote == "Enter Your Author Here!" or  quote == "" or quote == "Quote" or quote == "quote":
                messagebox.showerror("INVALID",f"Please Enter your Quote first before saving.")
            elif author == "Enter Quote Here!" or author == "" or author == "Author" or author == "author":
                messagebox.showerror("INVALID",f"Please Enter your Author first before saving.")
            elif quote == author:
                messagebox.showerror("INVALID",f"The Quote and Author cannot be the same.")
            else:
                if isfile("adventure.json"):
                    # Read existing data from the JSON file
                    with open("adventure.json", "r") as json_file:
                        existing_data = json.load(json_file)
                    
                    # Append the new data to the list of inputs
                    existing_data["Adventure"].append(new_data)
                else:
                    # If the file doesn't exist, start with a list containing the new data
                    existing_data = {"Adventure": [new_data]}

                # Write the updated data to the JSON file
                with open("adventure.json", "w") as json_file:
                    json.dump(existing_data, json_file, indent=2)
                self.root.withdraw()
                messagebox.showinfo("NOTICE!",f"Quote:{author.title()}\nAuthor:{quote.title()} \n\n\nYour Quote has been saved")
                self.display_adventure()
                self.root.deiconify()
                self.lf3.grid_forget()
                self.lf2.grid(row=0, column=0, padx=10, ipady=10)
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError:
            print("Error decoding JSON data")
            
    def treeview(self):
        self.lf2.grid_forget()
        self.lf4.grid(row=0, column=0, padx=5, ipady=5)
        self.treeFrame = ttk.Frame(self.lf4)
        self.treeFrame.grid(row=0, column=0)
        self.back = MyButton(self.lf4, 40, "Back", "khaki", "#003f5c", self.back3 ,2,0,'')

        self.v = ttk.Scrollbar(self.lf4)
        self.v.grid(row=0, column=1, sticky='ns')

        self.h = ttk.Scrollbar(self.lf4 ,orient='horizontal')
        self.h.grid(row=1, column=0, sticky='we')

        def expand_treeview(event):
            self.tree.column("#0", width=event.width)
        self.root.bind("<Configure>", expand_treeview)

        self.tree = ttk.Treeview(self.lf4, selectmode='browse', wrap=None,
                            xscrollcommand=self.h.set,
                            yscrollcommand=self.v.set)
        self.tree.grid(row=0, column=0)

        self.v.configure(command=self.tree.yview)
        self.h.configure(command=self.tree.xview)

        self.tree["columns"] = ("1"
                        , "2")
        self.tree['show'] = 'headings' 

        self.tree.column("1", width=500, anchor='c')
        self.tree.column("2", width=150, anchor='c') 

        self.tree.tag_configure('evenrow'
                   , background='lightcyan', font=('calibri', 8))
                        #this is to achieve the alternating colors in treeview
        self.tree.tag_configure('oddrow'
                   , background='skyblue', font=('calibri', 8)) 
        
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure('Treeview', rowheight=31,
                        fieldbackground='lavender')
        self.style.configure("Treeview.Heading"
                        , background="blue", foreground="white"
                        , font=('calibri bold', 10))

    def display_inspirational(self):
        #treeview
        self.treeview()
        self.tree.heading("1", text="Inspirational Quote")
        self.tree.heading("2", text="Author")
        with open('inspirational.json', "r") as f:
            data = json.load(f)
    
            self.tree.tag_configure('evenrow'
                            , background='lightcyan', font=('calibri', 8))
                                    #this is to achieve the alternating colors in treeview
            self.tree.tag_configure('oddrow'
                            , background='skyblue', font=('calibri', 8))
            count=0
            for record in data['Inspirational']:
                if count % 2 ==0:
                    self.tree.insert(parent='', index="end", iid=count, text="", values=(record['Quote'],record['Author']), tags=('evenrow',))
                else:    
                    self.tree.insert(parent='', index="end", iid=count, text="", values=(record['Quote'],record['Author']), tags=('oddrow',))
        
                count+=1
    
    def display_wisdom(self):
        #treeview
        self.treeview()
        self.tree.heading("1", text="Wisdom Quote")
        self.tree.heading("2", text="Author")
        with open('wisdom.json', "r") as f:
            data = json.load(f)
    
            self.tree.tag_configure('evenrow'
                            , background='lightcyan', font=('calibri', 8))
                                    #this is to achieve the alternating colors in treeview
            self.tree.tag_configure('oddrow'
                            , background='skyblue', font=('calibri', 8))
            count=0
            for record in data['Wisdom']:
                if count % 2 ==0:
                    self.tree.insert(parent='', index="end", iid=count, text="", values=(record['Quote'],record['Author']), tags=('evenrow',))
                else:    
                    self.tree.insert(parent='', index="end", iid=count, text="", values=(record['Quote'],record['Author']), tags=('oddrow',))
        
                count+=1

    def display_humor(self):
        #treeview
        self.treeview()
        self.tree.heading("1", text="Humorous Quote")
        self.tree.heading("2", text="Author")
        with open('humor.json', "r") as f:
            data = json.load(f)
    
            self.tree.tag_configure('evenrow'
                            , background='lightcyan', font=('calibri', 8))
                                    #this is to achieve the alternating colors in treeview
            self.tree.tag_configure('oddrow'
                            , background='skyblue', font=('calibri', 8))
            count=0
            for record in data['Humorous']:
                if count % 2 ==0:
                    self.tree.insert(parent='', index="end", iid=count, text="", values=(record['Quote'],record['Author']), tags=('evenrow',))
                else:    
                    self.tree.insert(parent='', index="end", iid=count, text="", values=(record['Quote'],record['Author']), tags=('oddrow',))
                count+=1

    def display_literary(self):
        #treeview
        self.treeview()
        self.tree.heading("1", text="Literary Quote")
        self.tree.heading("2", text="Author")
        with open('literary.json', "r") as f:
            data = json.load(f)
    
            self.tree.tag_configure('evenrow'
                            , background='lightcyan', font=('calibri', 8))
                                    #this is to achieve the alternating colors in treeview
            self.tree.tag_configure('oddrow'
                            , background='skyblue', font=('calibri', 8))
            count=0
            for record in data['Literary']:
                if count % 2 ==0:
                    self.tree.insert(parent='', index="end", iid=count, text="", values=(record['Quote'],record['Author']), tags=('evenrow',))
                else:    
                    self.tree.insert(parent='', index="end", iid=count, text="", values=(record['Quote'],record['Author']), tags=('oddrow',))
                count+=1

    def display_motivational(self):
        #treeview
        self.treeview()
        self.tree.heading("1", text="Motivational Quote")
        self.tree.heading("2", text="Author")
        with open('motivational.json', "r") as f:
            data = json.load(f)
    
            self.tree.tag_configure('evenrow'
                            , background='lightcyan', font=('calibri', 8))
                                    #this is to achieve the alternating colors in treeview
            self.tree.tag_configure('oddrow'
                            , background='skyblue', font=('calibri', 8))
            count=0
            for record in data["Motivational"]:
                if count % 2 ==0:
                    self.tree.insert(parent='', index="end", iid=count, text="", values=(record['Quote'],record['Author']), tags=('evenrow',))
                else:    
                    self.tree.insert(parent='', index="end", iid=count, text="", values=(record['Quote'],record['Author']), tags=('oddrow',))
                count+=1

    def display_affirmation(self):
        #treeview
        self.treeview()
        self.tree.heading("1", text="Affirmation Quote")
        self.tree.heading("2", text="Author")
        with open('affirmation.json', "r") as f:
            data = json.load(f)
    
            self.tree.tag_configure('evenrow'
                            , background='lightcyan', font=('calibri', 8))
                                    #this is to achieve the alternating colors in treeview
            self.tree.tag_configure('oddrow'
                            , background='skyblue', font=('calibri', 8))
            count=0
            for record in data['Affirmation']:
                if count % 2 ==0:
                    self.tree.insert(parent='', index="end", iid=count, text="", values=(record['Quote'],record['Author']), tags=('evenrow',))
                else:    
                    self.tree.insert(parent='', index="end", iid=count, text="", values=(record['Quote'],record['Author']), tags=('oddrow',))
                count+=1

    def display_adventure(self):
        #treeview
        self.treeview()
        self.tree.heading("1", text="Adventure Quote")
        self.tree.heading("2", text="Author")
        with open('adventure.json', "r") as f:
            data = json.load(f)
    
            self.tree.tag_configure('evenrow'
                            , background='lightcyan', font=('calibri', 8))
                                    #this is to achieve the alternating colors in treeview
            self.tree.tag_configure('oddrow'
                            , background='skyblue', font=('calibri', 8))
            count=0
            for record in data['Adventure']:
                if count % 2 ==0:
                    self.tree.insert(parent='', index="end", iid=count, text="", values=(record['Quote'],record['Author']), tags=('evenrow',))
                else:    
                    self.tree.insert(parent='', index="end", iid=count, text="", values=(record['Quote'],record['Author']), tags=('oddrow',))
                count+=1

    def on_load(self):
        # self.lf.grid_forget()
        messagebox.showinfo("NOTICE!",f"Data Loaded succesfully.")
        self.display = MyButton(self.lf, 12, "Display Quote", "khaki", "#003f5c", self.on_display ,1,0,'w')
        # self.lf2.grid(row=0, column=0, padx=10, ipady=10)

    def on_exit(self):
        self.root.withdraw()

if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg='#f0ead2')
    root.resizable(False, False)
    app = MyApp(root)
    root.mainloop()


