from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter.ttk as ttk
import csv
import os 

class Student_Record:
    
    def __init__ (self,root):
        self.root = root
        blank_space = ""
        self.root.title(200 * blank_space + "Student Information System")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False,False)
        self.data = dict()
        self.temp = dict()
        self.filename = "StudentData.csv"
        
        Std_Fname = StringVar()
        Std_Mname = StringVar()
        Std_Lname = StringVar()
        Std_IDNumber = StringVar()
        Std_YearLevel = StringVar()
        Std_Gender = StringVar()
        Std_Course = StringVar()
        searchbar = StringVar()
        
        if not os.path.exists('StudentData.csv'):
            with open('StudentData.csv', mode='w') as csv_file:
                fieldnames = ["Student ID Number", "Last Name", "First Name", "Middle Name","Gender", "Year Level", "Course"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
        
        else:
            with open('StudentData.csv', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.data[row["Student ID Number"]] = {'Last Name': row["Last Name"], 'First Name': row["First Name"], 'Middle Name': row["Middle Name"], 'Gender': row["Gender"],'Year Level': row["Year Level"], 'Course': row["Course"]}
            self.temp = self.data.copy()
        
        
         
        #=============================================================FUNCTIONS================================================================#
# To exit program        
        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Information System","Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return
# To add Student           
        def addStudent():
            with open('StudentData.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if Std_IDNumber.get()=="" or Std_Fname.get()=="" or Std_Mname.get()=="" or Std_Lname.get()=="" or Std_YearLevel.get()=="":
                    tkinter.messagebox.showinfo("Student Information System","To add, please fill in the box.")
                else:
                    self.data[Std_IDNumber.get()] = {'Last Name': Std_Lname.get(), 'First Name': Std_Fname.get(), 'Middle Name': Std_Mname.get(), 'Gender': Std_Gender.get(),'Year Level': Std_YearLevel.get(), 'Course': Std_Course.get()}
                    self.saveData()
                    tkinter.messagebox.showinfo("Student Information System", "Student added Successfully!")
                Clear()
                displayData()
                    
# To clear data        
        def Clear():
            Std_IDNumber.set("")
            Std_Fname.set("")
            Std_Mname.set("")
            Std_Lname.set("")
            Std_YearLevel.set("")
            Std_Gender.set("")
            Std_Course.set("")
        
        
# To display student data        
        def displayData():
            tree.delete(*tree.get_children())
            with open('StudentData.csv') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    IDNumber=row['Student ID Number']
                    LastName=row['Last Name']
                    FirstName=row['First Name']
                    MiddleName=row['Middle Name']
                    YearLevel=row['Year Level']
                    Course=row['Course']
                    Gender=row['Gender']
                    tree.insert("",0, values=(IDNumber, LastName, FirstName, MiddleName, Gender, YearLevel, Course))
                    
      
# To remove student record        
        def deleteData():
            if tree.focus()=="":
                tkinter.messagebox.showerror("Student Information System","Please select student record")
                return
            id_no = tree.item(tree.focus(),"values")[0]
            
            self.data.pop(id_no, None)
            self.saveData()
            tree.delete(tree.focus())
            tkinter.messagebox.showinfo("Student Information System","Student Record Deleted Successfully")
            
        
# To search student by ID number        
        def searchData():
            if self.searchbar.get() in self.data:
                vals = list(self.data[self.searchbar.get()].values())
                tree.delete(*tree.get_children())
                tree.insert("",0, values=(self.searchbar.get(), vals[0],vals[1],vals[2],vals[3],vals[4],vals[5]))
            elif self.searchbar.get() == "":
                displayData()
            else:
                tkinter.messagebox.showerror("Student Information System","Student not found")
                return
            
        
        
# To edit student data        
        def editData():
            if tree.focus() == "":
                tkinter.messagebox.showerror("Student Information System", "Please select a student record")
                return
            values = tree.item(tree.focus(), "values")
            Std_IDNumber.set(values[0])
            Std_Lname.set(values[1])
            Std_Fname.set(values[2])
            Std_Mname.set(values[3])
            Std_Gender.set(values[4])
            Std_YearLevel.set(values[5])
            Std_Course.set(values[6])
       

# To update student record           
        def updateData():
            with open('StudentData.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if Std_IDNumber.get()=="" or Std_Fname.get()=="" or Std_Mname.get()=="" or Std_Lname.get()=="" or Std_YearLevel.get()=="":
                    tkinter.messagebox.showinfo("Student Information System","Please select a student record")
                else:
                    self.data[Std_IDNumber.get()] = {'Last Name': Std_Lname.get(), 'First Name': Std_Fname.get(), 'Middle Name': Std_Mname.get(), 'Gender': Std_Gender.get(),'Year Level': Std_YearLevel.get(), 'Course': Std_Course.get()}
                    self.saveData()
                    tkinter.messagebox.showinfo("Student Information System", "Student Record Updated!")
                Clear()
                displayData()     

        #============================================================FRAMES====================================================#
        
        MainFrame = Frame(self.root, bd=7, width=1135, height=130, relief=RIDGE, bg="deep sky blue4")
        MainFrame.grid()
       
        
        TopFrame1 = Frame(MainFrame,  width=300, height=130, relief=RIDGE, bg="deep sky blue4")
        TopFrame1.grid(row=2, column=0)
        
        TitleFrame = Frame(MainFrame, bd=5, width=300, height=130, relief=RIDGE, bg="turquoise")
        TitleFrame.grid(row=0, column=0)
        
        TopFrame2 = Frame(MainFrame, bd=5, width=1340, height=1300, relief=RIDGE, bg="light salmon")
        TopFrame2.grid(row=1, column=0)

        SearchFrame = Frame(MainFrame, width = 20, height = 100, relief = RIDGE, bg="turquoise" )
        SearchFrame.grid(row =3, column =0)
        
        LeftFrame = Frame(TopFrame2, width=20, height=80, padx=2, relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        
        
        LeftFrame1 = Frame(LeftFrame, bd=2, width=40, height=40, padx=4, pady=4, relief=RIDGE, bg="deep sky blue4")
        LeftFrame1.pack(side=TOP, padx=0, pady=2)
        
        
        RightFrame1 = Frame(TopFrame2, bd=5, width=800, height=600, padx=2, bg="turquoise", relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        

        

        
        #=============================================TITLE===========================================#
        
        self.lblTitle = Label(TitleFrame, font=('arial',45,'bold'), text="STUDENT INFORMATION SYSTEM", bd=7, bg="light salmon",fg="deep sky blue4")
        self.lblTitle.grid(row=0, column=0)
        
        #===========================================================================LABELS & ENTRY WIDGETS=======================================================#
        
        
        
        self.lblStudentID = Label(LeftFrame1, font=('calibri',16,'bold'), text=" " "Student ID:"" ", bd=5 , anchor=W, bg="deep sky blue4", fg="white")
        self.lblStudentID.grid(row=0, column=0, sticky=W, padx=7)
        self.txtStudentID = Entry(LeftFrame1, font=('calibri',14,'bold'), width=40, justify='left', textvariable = Std_IDNumber)
        self.txtStudentID.grid(row=0, column=1)
        
        self.lblLastName = Label(LeftFrame1, font=('calibri',16,'bold'), text=" " "Last Name: ", bd=5, anchor=W, bg="deep sky blue4", fg="white")
        self.lblLastName.grid(row=1, column=0, sticky=W, padx=7)
        self.txtLastName = Entry(LeftFrame1, font=('calibri',14,'bold'), width=40, justify='left', textvariable = Std_Lname)
        self.txtLastName.grid(row=1, column=1)
        
        self.lblFirstName = Label(LeftFrame1, font=('calibri',16,'bold'), text="First Name:", bd=5, anchor=W, bg="deep sky blue4", fg="white")
        self.lblFirstName.grid(row=2, column=0, sticky=W, padx=7)
        self.txtFirstName = Entry(LeftFrame1, font=('calibri',14,'bold'), width=40, justify='left', textvariable = Std_Fname)
        self.txtFirstName.grid(row=2, column=1)
        
        self.lblMiddleName = Label(LeftFrame1, font=('calibri',16,'bold'), text="Middle Name:", bd=5, anchor=W, bg="deep sky blue4", fg="white")
        self.lblMiddleName.grid(row=3, column=0, sticky=W, padx=7)
        self.txtMiddleName = Entry(LeftFrame1, font=('calbri',14,'bold'), width=37, justify='left', textvariable = Std_Mname)
        self.txtMiddleName.grid(row=3, column=1)

        self.lblGender = Label(LeftFrame1, font=('calibri',16,'bold'), text="Gender:", bd=5, anchor=W, bg="deep sky blue4", fg="white")
        self.lblGender.grid(row=4, column=0, sticky=W, padx=7)
        
        self.cboGender = ttk.Combobox(LeftFrame1, font=('calibri',14,'bold'), state='readonly', width=39, textvariable = Std_Gender)
        self.cboGender['values'] = ('Female', 'Male')
        self.cboGender.grid(row=4, column=1)
        
        self.lblCourse = Label(LeftFrame1, font=('calibri',16,'bold'), text="Course:", bd=5, anchor=W, bg="deep sky blue4", fg="white")
        self.lblCourse.grid(row=5, column=0, sticky=W, padx=7)
        self.txtCourse = Entry(LeftFrame1, font=('calibri',14,'bold'), width=40, justify='left', textvariable = Std_Course)
        self.txtCourse.grid(row=5, column=1)
        
        self.lblYearLevel = Label(LeftFrame1, font=('calibri',16,'bold'), text="Year Level:", bd=5, anchor=W, bg="deep sky blue4", fg="white")
        self.lblYearLevel.grid(row=6, column=0, sticky=W, padx=7)
        
        self.cboYearLevel = ttk.Combobox(LeftFrame1, font=('calibri',14,'bold'), state='readonly', width=39, textvariable = Std_YearLevel)
        self.cboYearLevel['values'] = ('1st Year', '2nd Year', '3rd Year', '4th Year')
        self.cboYearLevel.grid(row=6, column=1)
        
        self.searchbar = Entry(self.root, font=('calibri',16,'bold'), textvariable = searchbar, width = 22)
        self.searchbar.place(x=20,y=550)
        self.searchbar.insert(0,'Search ID No.')
        
        
        #=========================================================BUTTONS================================================#
        
        self.btnAddNew=Button(self.root, pady=1,bd=5,font=('arial',16,'bold'), padx=30, width=10, text='Add New Student', bg="deep sky blue4", fg="white", command=addStudent)
        self.btnAddNew.place(x=20,y=120)
        
        self.btnClear=Button(self.root, pady=1,bd=5,font=('arial',16,'bold'), padx=30, width=10, text='Clear', bg="deep sky blue4", fg="white", command=Clear)
        self.btnClear.place(x=20,y=180)
        
        self.btnUpdate=Button(self.root, pady=1,bd=5,font=('arial',16,'bold'), padx=30, width=10, text='Update Record', bg="deep sky blue4", fg="white" ,command=updateData)
        self.btnUpdate.place(x=380,y=120)

        self.btnEdit=Button(self.root, pady=1,bd=5,font=('arial',16,'bold'), padx=30, width=10, text='Edit Record',bg="deep sky blue4", fg="white", command = editData)
        self.btnEdit.place(x=380,y=180)

        self.btnDelete=Button(self.root, pady=1,bd=5,font=('arial',16,'bold'), padx=2, width=8, height= 2, text='Delete', bg="deep sky blue4", fg="white", command = deleteData)
        self.btnDelete.place(x=240,y=140)

        self.btnExit=Button(self.root, pady=1,bd=5,font=('arial',16,'bold'), padx=2, width=8, text='Exit', bg="deep sky blue4", fg="white", command = iExit)
        self.btnExit.place(x=380,y=590)

        self.btnSearch=Button(self.root, pady=1,bd=5,font=('arial',16,'bold'), padx=26, width=8, text='Search', bg="deep sky blue4", fg="white", command = searchData)
        self.btnSearch.place(x=20,y=590)

        self.btnDisplay=Button(self.root, pady=1,bd=5,font=('arial',16,'bold'), padx=2, width=10, text='Display List', bg="deep sky blue4", fg="white",  command= displayData)
        self.btnDisplay.place(x=380,y=530)

        
        #==============================================================================TREEVIEW=========================================================================#
        
        scroll_y=Scrollbar(RightFrame1, orient=VERTICAL)
        
        tree = ttk.Treeview(RightFrame1, height= 25, columns=("Student ID Number", "Last Name", "First Name", "Middle Name", "Gender", "Year Level", "Course"), yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        tree.heading("Student ID Number", text="Student ID Number")
        tree.heading("Last Name", text="Last Name")
        tree.heading("First Name", text="First Name")
        tree.heading("Middle Name", text="Middle Name")
        tree.heading("Gender", text="Gender")
        tree.heading("Year Level", text="Year Level")
        tree.heading("Course", text="Course")
        tree['show'] = 'headings'

        tree.column("Student ID Number", width=120)
        tree.column("Last Name", width=100)
        tree.column("First Name", width=100)
        tree.column("Middle Name", width=100)
        tree.column("Gender", width=70)
        tree.column("Year Level", width=80)
        tree.column("Course", width=120)
        tree.pack(fill=BOTH,expand=1)
        
        displayData()
        #===========================================================================================================================================================#
    def saveData(self):
        temps = []
        with open('StudentData.csv', "w", newline ='') as update:
            fieldnames = ["Student ID Number","Last Name","First Name","Middle Name","Gender","Year Level","Course"]
            writer = csv.DictWriter(update, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for id, val in self.data.items():
                temp ={"Student ID Number": id}
                for key, value in val.items():
                    temp[key] = value
                temps.append(temp)
            writer.writerows(temps)
            

if __name__ =='__main__':
    root = Tk()
    application = Student_Record(root)
    root.mainloop()
