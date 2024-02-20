import tkinter as tk
import tkinter.ttk as ttk


class CountdownCalender:
    def __init__(self):
        self.__load_event_information__()
        self.__render_information__()

    def __load_event_information__(self):
        self.events = [
            ['Title1', 'Date1', 'Days to go 1', 'To do1'],
            ['Title2', 'Date2', 'Days to go 2', 'To do2'],
            ['Title3', 'Date3', 'Days to go 3', 'To do3'],
        ]

    def __render_information__(self):
        # Creating a window and setting its attributes

        self.window = tk.Tk()
        self.window.title('CountDown Calender')
        self.window.geometry('400x300')
        self.window.resizable(width=False, height=False)
        self.window['bg'] = '#FFAECE'
        # Create widgets
        # Frame
        main_frame = tk.LabelFrame(master=self.window, text='Events')
        main_frame['bg'] = '#EFE4B0'
        main_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        # Combobox
        event_titles = ['A', 'B', 'C', 'D']
        cmb_current_selection = tk.StringVar()
        cmb_current_selection.set('SELECT')
        cmb_event = ttk.Combobox(master=main_frame, values=event_titles, state='readonly', )

        #Labels
        lbl_date = tk.Label(master=main_frame,text='Date : ')
        lbl_days_to_go = tk.Label(master=main_frame, text='Days to go: ')
        lbl_to_do = tk.Label(master=main_frame, text='To Do: ')


        # Add the widgets to main frame
        cmb_event.grid(row=0, column=0)

        # Event Procedure

        self.window.mainloop()


def main():
    cc = CountdownCalender()


main()
