import os
clear = lambda: os.system('clear')
clear()

import math as m
import numpy as np
import curses
from prettytable import PrettyTable

class Manage:
    def __init__(self):
        self.__no = 0
    
    def input(self):
        self.__no = int(input())
        clear()
        return self.__no

    def list(self):
        pass

    
class Student(Manage):
    def __init__(self):
        self.__noStudent = 0
        self.__students = []

    def input(self):
        print("Input number of students: ")
        self.__noStudent = super().input()
        
        for i in range(1, self.__noStudent+1):
            student = {
            "Id" : "None",
            "Name" : "None",
            "DoB" : "None"
            }

            print(f"Input info of student #{i}:")
            student.update({"Id" : input("Input ID: ")})
            student.update({"Name" : input("Input name: ")})
            student.update({"DoB" : input("Input DoB (dd/mm/yyyy): ")})
            self.__students.append(student)
            clear()

    def list(self):
        table = PrettyTable()
        table.field_names = ["ID", "Name", "DoB"]
        for i in self.__students:
            table.add_row(i.values())
        
        return table

    def get_student(self):
        return self.__students
    
class Course(Manage):
    def __init__(self):
        self.__noCourse = 0
        self.__courses = []

    def input(self):
        print("Input number of courses: ")
        self.__noCourse = super().input()
        
        for i in range(1, self.__noCourse+1):
            course = {
            "Id" : "None",
            "Name" : "None",
            "Credit": "None"
            }

            print(f"Input info of course #{i}:")
            course.update({"Id" : input("Input ID: ")})
            course.update({"Name" : input("Input name: ")})
            course.update({"Credit" : int(input("Input number of credits: "))})
            self.__courses.append(course)
            clear()

    def list(self):
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Credits"]
        for i in self.__courses:
            table.add_row(i.values())
        
        return table

    def get_course(self):
        return self.__courses

class Mark(Manage):
    def __init__(self, students, courses):
        self.__marks = []
        self.__students = students
        self.__courses = courses

    def input(self):
        index = 0
        for i in self.__students:
            inv_mark = []
            mark = {"Id" : "None",
                    "Name" : "None",
                    "Mark" : "None"
                    }              
            mark["Id"] = i["Id"]
            mark["Name"] = i["Name"]

            for j in self.__courses:
                print("Input mark for student " + i["Id"] + ":")
                print("Mark of course " + j["Name"] + ": ")
                
                fix_mark = float(input())
                fix_mark = m.floor(fix_mark * 10)/10.0
                inv_mark.append(fix_mark)
                mark.update({"Mark" : inv_mark})
                clear()

            self.__marks.append(mark)
            index += 1
            clear()
                
    def GPA_cal(self):
        credits = []
        for i in self.__courses:
            credits.append(i["Credit"])
        arr_credit = np.array(credits)
        
        for j in self.__marks:
            arr_mark = np.array(j["Mark"])

            GPA = np.average(arr_mark, weights=arr_credit)
            GPA = m.floor(GPA * 10) /10.0
            j["GPA"] = GPA
            arr_mark = np.delete(arr_mark, range(len(arr_mark)))
        
    def GPA_sort(self):
        self.__marks.sort(key=lambda x : x["GPA"], reverse=True)
    
    def list(self):
        self.GPA_cal()
        self.GPA_sort()
        table = PrettyTable()
        field = ["ID", "Name","GPA"]
        for index, course in zip(range(len(self.__courses)), self.__courses):
            field.insert(index + 2, course["Name"])

        table.field_names = field
        for i in self.__marks:
            table.add_row([i["Id"], i["Name"], *i["Mark"], i["GPA"]])

        return table

s = Student()
s.input()
c = Course()
c.input()
ma = Mark(s.get_student(), c.get_course())
ma.input()

menu = ['List', 'Exit']
submenu = ['Student List', 'Course List', 'Mark List', 'Back']

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_YELLOW)

    current_row_index = 0
    
    menu_func(stdscr, current_row_index)

def print_menu(stdscr, selected_row_idx, menu):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()


def menu_func(stdscr, indx):
    print_menu(stdscr, indx, menu)

    while True:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and indx > 0:
            indx -= 1
        elif key == curses.KEY_DOWN and indx < len(menu) - 1:
            indx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            
            option = "{}".format(menu[indx])
            match option:
                case 'List' : submenu_func(stdscr, indx=0)
                case 'Exit' : exit()

            stdscr.refresh()
            stdscr.getch()

        print_menu(stdscr, indx, menu)
        stdscr.refresh()

def submenu_func(stdscr, indx):
    print_menu(stdscr, indx, submenu)

    while True:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and indx > 0:
            indx -= 1
        elif key == curses.KEY_DOWN and indx < len(submenu) - 1:
            indx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            
            option = "{}".format(submenu[indx])
            match option:
                case 'Student List': 
                    stdscr.addstr(1, 0, "Student List: ", curses.color_pair(2))
                    stdscr.addstr(3, 0, s.list().get_string(), curses.color_pair(1))
                    stdscr.addstr(0, 0, "Press ENTER to get back")

                case 'Course List': 
                    stdscr.addstr(1, 0, "Course List: ", curses.color_pair(2))
                    stdscr.addstr(3, 0, c.list().get_string(), curses.color_pair(1))
                    stdscr.addstr(0, 0, "Press ENTER to get back")

                case 'Mark List':
                    stdscr.addstr(1, 0, "Mark List: ", curses.color_pair(2))
                    stdscr.addstr(3, 0, ma.list().get_string(), curses.color_pair(1))
                    stdscr.addstr(0, 0, "Press ENTER to get back")
                    
                case 'Back': menu_func(stdscr, indx = 0)

            stdscr.refresh()
            stdscr.getch()

        print_menu(stdscr, indx, submenu)
        stdscr.refresh()

curses.wrapper(main)
