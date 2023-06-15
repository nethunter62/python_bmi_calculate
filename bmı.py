import tkinter

window = tkinter.Tk()
window.geometry("400x400")
window.title("Beden Kitle İndex Hesaplayıcı")

def hesapla_bmi():
    height = height_input.get()
    weight = weight_input.get()
    if weight == "" or height == "":
        result_label.config(text="Kilonuzu ve boyunuzu girin")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Lütfen bir değer girin!")


# ui
weight_input_label = tkinter.Label(text="Kilonuzu girin (kg)")
weight_input_label.pack()
weight_input = tkinter.Entry(width=10)
weight_input.pack()
height_input_label = tkinter.Label(text="Boyunuzu girin (cm)")
height_input_label.pack()
height_input = tkinter.Entry(width=10)
height_input.pack()
calculate_button = tkinter.Button(text="HESAPLA", command=hesapla_bmi)
calculate_button.pack()
result_label = tkinter.Label()
result_label.pack()


def write_result(bmi):
    result_string = f"Senin indexin  {round(bmi, 2) : } "
    if bmi <= 16:
        result_string += "ZAYIF"
    elif 16 < bmi <= 17:
        result_string += "İDEAL"
    elif 17 < bmi <= 18.5:
        result_string += "ORTA"
    elif 18.5 < bmi <= 25:
        result_string += "NORMAL"
    elif 25 < bmi <= 30:
        result_string += "AŞIRI!"
    elif 30 < bmi <= 35:
        result_string += "OBEZ DERECE 1!"
    elif 35 < bmi <= 40:
        result_string += "OBEZ DERECE 2!!"
    else:
        result_string += "OBEZ DERECE 3!!!"
    return result_string


window.mainloop()