from tkinter import *

from Circle import Circle


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def calculate(event):  # paneb nupu tööle
   # print('Button Clicked') Test
    radius = user_input.get()
   # print(radius)  # Test
    if is_float(radius):
        user_input.delete(0, END)
        radius = float(radius)  # now is radius float, number
        circle = Circle(radius)  # tee import
        txt_field['state'] = 'normal' # lubab muuta tekstivälja
        txt_field.delete('1.0', END)    # tühjendab kasti peale uut sisestust, esimesest reast kuni lõpuni
        txt_field.insert(END, 'Radius: ' + str(circle.radius) + '\n')
        txt_field.insert(END, 'Diameter: ' + str(circle.get_diameter()) + '\n')
        txt_field.insert(END, 'Area: ' + str(circle.get_area()) + '\n')
        txt_field.insert(END, 'Perimeter: ' + str(circle.get_diameter()) + '\n')
        txt_field['state'] = 'disabled' # keelab tekstivälja lisamise
        # print('Number')  # Test  ütleb kas sistatud on number või mitte.
  #  else: # Test
       # print('Error')


# main window omadused
window = Tk()  # Loob akna
window.title('Geometry - Circle') # Akna tekst
window.geometry('400x500')  # laius 400 pikkus 500
window.resizable(False, False) # True width, false height

# Frames loob sinise riba üles
frame_top = Frame(window,bg='#89CFF0', height=50 )
frame_top.pack(fill='both')  # .pack toob asja esile.

# loob järgmise riba alla
frame_bottom = Frame(window, bg='#90EE90', height=50)
frame_bottom.pack(fill=BOTH)

# First line in frame top
lbl = Label(frame_top, text='Circle radius', bg='#89CFF0')
lbl.pack(side='left')

user_input = Entry(frame_top)
user_input.pack(side=LEFT)
user_input.focus()  # teeb kursori kohe aktiivseks

#nupp

btn_calc = Button(frame_top, text='Calculate', command=lambda: calculate(0))  # tuvastab nupu vajutuse kui ka enetriga
btn_calc.pack(side=LEFT, padx=2, pady=2)    # padx ja pady muudavad nupu suurust
# teksti objekt

txt_field = Text(frame_bottom, state=DISABLED)
txt_field.pack(side='left', padx=2, pady=2)

# Et enter klahv toimiks
window.bind('<Return>', lambda event: calculate(event))




# No MVC last line
window.mainloop()