from tkinter import *
import tkinter.messagebox

''' Widgets used:
    LabelFrame: a labelframe is a widget that can hold other widgets. We are using it to separate different 
            components/parts of the student info form like student data, exploratory data analysis, students above 70 etc
    Label: To create a single line caption for other widgets like Entry .Firstname, Score, Lastname, Matric no 
            are all labels
    Entry: To display a single line text field for accepting values inputted by a user
    Button: display a button
    
    attributes/options used:
    padx: gives space outside the widget to the x-axis
    pady: gives space outside the widget to the y-axis
    ipadx: gives space inside the widget to the x-axis like in an Entry widget
    ipady: gives space inside the widget to the y-axis
    text: sets the text of a Label (or button or any other widget) to a particular text. For example 
            Label(text="Forever") sets the text of the label to Forever
    bg: background color
    command: 
    row:
    column:
    textvariable:
    
    Methods:
    .pack: you use .pack to set a widget to the bottom, right, left or top 
    .grid: you always need to use .grid when you are using rows and columns to arrange things in the window
'''


class ProcessButtons:
    def __init__(self):
        window = Tk()  # create a window where all the widgets are going to be in
        window.title('STUDENT INFO')  # set the title of the window to "STUDENT INFO"
        self.bg_color = 'lightgreen'  # creating a variable that stores a color
        window['bg'] = self.bg_color  # setting the background color of the window to th color in self.bg_color
        #self.show_analysis = True  # this lets us click the "make analysis" button only once

        self.fname = StringVar()  # holds a String value/data where we can set text value and retrieve it. We can pass
        # this variable to textVariable for a widget like Entry. For example, the value that the user enters in Entry
        # widget "fname" is stored here in self.fname.
        self.lname = StringVar()
        self.matric_no = IntVar()  # stores an Integer value/data
        self.score = IntVar()

        frame1 = LabelFrame(window, padx=25, pady=15, bg=self.bg_color, text='student data')  # create a label frame
        # and when we want to add any widget to the LabelFrame we just created we can access it with using 'frame1'
        # because that is the variable this paricular LabelFrame is assigned to
        frame1.pack()
        fname_lbl = Label(frame1, text='Firstname: ', bg=self.bg_color).grid(row=1, column=1)
        # the frame1 in Label(frame1) indicates that we want to add this Label to frame1. We do this everytime we create
        # a new widget.
        fname = Entry(frame1, textvariable=self.fname).grid(row=1, column=2, ipadx=5, ipady=5)
        lname_lbl = Label(frame1, text='Lastname: ', bg=self.bg_color).grid(row=1, column=3, ipadx=5, ipady=5)
        lname = Entry(frame1, textvariable=self.lname).grid(row=1, column=4, ipadx=5, ipady=5)
        matric_lbl = Label(frame1, text='Matric no: ', bg=self.bg_color).grid(row=2, column=1, ipadx=5, ipady=5)
        matric = Entry(frame1, textvariable=self.matric_no).grid(row=2, column=2, ipadx=5, ipady=5)
        score_lbl = Label(frame1, text='score: ', bg=self.bg_color).grid(row=2, column=3, ipadx=5, ipady=5)
        score = Entry(frame1, textvariable=self.score).grid(row=2, column=4, ipadx=5, ipady=5)

        save_btn = Button(window, text='SAVE DATA', command=self.save_data, padx=5, pady=5).pack()
        # creating a button. The command attribute stores the function save_data and when the button is clicked the
        # function is executed. So the command property just gives the button access to whatever function you assign
        # to it

        self.frame2 = LabelFrame(window, padx=95, pady=15, bg=self.bg_color, text='EXPLORATORY DATA ANALYSIS')
        # creating another labelframe
        self.frame2.pack()
        self.button_EDA = Button(window, text='MAKE ANALYSIS', command=self.compute_EDA, pady=5, width=15)
        self.button_EDA.pack(side=BOTTOM)
        self.allStudentsButton = Button(window, text="VIEW ALL STUDENTS", command=self.view_all_students, pady=5)
        self.allStudentsButton.pack(side=BOTTOM)

        window.mainloop()
        # window.mainloop() shows the end of the window. If you do not use .mainloop(), the window would not show

    def save_data(self):
        # the save_data function is created to store information taken from the user in a text file

        file_db = open('file_db.txt', 'a')
        # standard way to open a file. 'file_db.txt' is the name of the file we want to open. 'a' means that we are
        # adding to the file. It also creates the file if it does not exist

        # the try except is used to handle errors.
        try:
            first_name = str(self.fname.get())  # .get is a python function that gets the value stored in variable. In
            # this case fname. It stores the value gotten in first_name.
            matric_no = int(self.matric_no.get())
            last_name = str(self.lname.get())
            score = int(self.score.get())
            if score not in range(101) or score == '':
                # if the score is not between 0 and 100 raise an error
                raise InvalidInput('Invalid Score: score should be between 0 and 100')
                # the InvalidInput error is a custom error created to warn user against wrong inputs
                #and takes care of the error to prevent the program from crashing and saving wrong inputs to the file
            if matric_no == 0 or matric_no == '' or len(str(matric_no)) != 9:
                # if the matric number is 0 or empty or is longer than 9 numbers, raise an error
                raise InvalidInput('Matric Number should be a number of  length 9 and not start with 0')
            if first_name == '' or last_name == '':
                # if there is no firstname or lastname inputted, raise an error
                raise InvalidInput('name should not be a number or empty!')
            file_db.write(f'{first_name} {last_name} {matric_no} {score}\n')
            # save to the file in the format fistname, lastname, matric no, score
            file_db.close()  # close the file
            tkinter.messagebox.showinfo('data saved', 'data saved successfully!')
            # tkinter.messagebox.showinfo is a function that shows a messagebox with some text. "data saved" is shown in the
            # header and "data saved successfully is shown in the body of the messagebox"
            self.clear_data()
            #clears the firstname, lastname, matric and score
            self.compute_EDA()
            #calls the compute_EDA method in order to update the data analysis section after a new data is entered without closing the window

        except InvalidInput as err:
            #the except block only runs when an error of type InvalidInput is raised
            tkinter.messagebox.showerror('ERROR', err.message)
            # same as tkinter.messagebox.showinfo but .showerror is used to show errors
            #it is used to display error message passed to our error class

        except: 
            #this except block runs if any other input error occurs that might have escaped the first except block
            tkinter.messagebox.showerror('ERROR', 'Invalid Input!')


    def clear_data(self):  # clear the information in the Entry widgets
        self.fname.set('')  # set the f.name variable back to empty
        self.score.set('')  # set the score variable back to empty
        self.matric_no.set('')  # set the matric_no variable back to empty
        self.lname.set('')  # set the lname variable back to empty

    def get_student(self, fnames, lnames, matrics, index):
        # we'll use this later
        return f'{fnames[index]} {lnames[index]} {matrics[index]}'

    def students_above70_below30(self, scores, fnames, lnames, matrics):
        # this function gets the students with the highest score(put in frame 3) and lowest score(put in frame 4)

        self.frame3 = LabelFrame(self.frame2, bg=self.bg_color, text='STUDENTS ABOVE 69', padx=30)
        # creates a labelframe that we'll add students above score 69
        self.frame4 = LabelFrame(self.frame2, bg=self.bg_color, text='STUDENTS BELOW 31', padx=35)
        # another labelframe to add student below 31

        index = 0
        # the index variable is just a counter for use in the for loop
        for score in scores:
            if score > 69:
                Label(self.frame3, text=self.get_student(fnames, lnames, matrics, index), bg=self.bg_color).pack()
            elif score < 31:
                Label(self.frame4, text=self.get_student(fnames, lnames, matrics, index), bg=self.bg_color).pack()
            index += 1
        self.frame3.grid(row=5, column=1, columnspan=2)
        self.frame4.grid(row=5, column=3, columnspan=2, ipady=30)

    def compute_EDA(self):
        file_db = open('file_db.txt', 'r')
        # open the file. 'r' means to read the fine
        scores = []  # variableName = [] creates an array.
        first_names = []
        last_names = []
        matric_nos = []
        for line in file_db:  # here we are iterating over each line in the now opened file
            first, last, matric, score = line.split()  # .split() detects whitespaces in the line
            scores.append(int(score))  # and appends/adds the first string of words before the whitespace to array score
            first_names.append(first)  # appends/adds the second string of words to array first_name
            last_names.append(last)  # appends/adds the third string of words to array first_name
            matric_nos.append(matric)  # appends/adds the second string of words to array matric_nos
        minimum_score = min(scores)  # min is a python function that returns the minimum value from a set of
        # numbers(array scores)
        maximum_score = max(scores)  # max is a python function that returns the max value from a set of
        # numbers(array scores)
        highest_index = scores.index(maximum_score)  # .index gets the index of the value in maximum_score
        best_student = self.get_student(first_names, last_names, matric_nos, highest_index)
        # this is where we use the get_student function. It returns the name and matric number of the student with the
        # highest score
        average_score = sum(scores) / len(scores)  # calculate the average score of all students
        file_db.close()  # close the file

        # here we show/display the minimum score, maximum score, average score and best student in frame 2
        Label(self.frame2, text='LOWEST SCORE: ', bg=self.bg_color).grid(row=1, column=1)
        Label(self.frame2, text=minimum_score, bg=self.bg_color).grid(row=1, column=2)
        Label(self.frame2, text='HIGHEST SCORE: ', bg=self.bg_color).grid(row=2, column=1)
        Label(self.frame2, text=maximum_score, bg=self.bg_color).grid(row=2, column=2)
        Label(self.frame2, text='AVERAGE SCORE: ', bg=self.bg_color).grid(row=3, column=1)
        Label(self.frame2, text=format(average_score, '.2f'), bg=self.bg_color).grid(row=3, column=2)
        # .2f is a format converter. It prints/shows the average score in 2 decimal places
        Label(self.frame2, text='BEST STUDENT: ', bg=self.bg_color).grid(row=4, column=1)
        best_student_label = Label(self.frame2, text=best_student, bg=self.bg_color)
        best_student_label.grid(row=4, column=2)
        #saving the label to a variable so we can clear it before updating and prevent a certain bug
        best_student_label['text'] = best_student
        #performs the function students_above70_below30
        self.students_above70_below30(scores, first_names, last_names, matric_nos)
        self.button_EDA.destroy()
        #this destroys the analysis button after the first time as it's no longer needed.

    def view_all_students(self):
        wind = []
        new_window = Toplevel()  # create a new window
        file_db = open('file_db.txt', 'r')
        matrix = [line.split() for line in file_db]  # destructuring. This line reads each line in the file, splits it
        # and stores it in the matrix array as words.
        height = len(matrix)
        width = 4
        # Label(new_window, text="First Name" + "  " + "Last Name" + "  " + "Matric Number" + "  " + "Score").pack()
        for i in range(height):
            for j in range(width):
                Label(new_window, text=matrix[i][j]).grid(row=i + 1, column=j)  # this line just displays the
                # information of each student in the window we just created

#creates a custom error class to help us express error message to the users
class InvalidInput(RuntimeError):
    def __init__(self, message):
        super().__init__()
        self.message = message
ProcessButtons()  # run the process button class
