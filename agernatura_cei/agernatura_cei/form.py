import tkinter
import customtkinter as ctk
import os, sys
from PIL import Image, ImageTk
from agernatura_cei.patient import ScalePatient

from agernatura_cei.patient_charts import ChartGenerator
from agernatura_cei.exceptions import GenderError, ActivityError, FormError
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("800x540")
app.title("Formulario Paciente")

def get_data():
    """obtenemos los datos del paciente"""
    datos_paciente = {}

    datos_paciente['nombre'] = entry1.get()
    datos_paciente['apellido'] = entry2.get()
    datos_paciente['edad'] = int(entry3.get())
    datos_paciente['genero'] = entry15.get()
    datos_paciente['altura'] = float(entry4.get())
    datos_paciente['peso'] = float(entry5.get())
    datos_paciente['actividad'] = dropdown_actividad.get()
    datos_paciente['medida_cintura'] = float(entry7.get())
    datos_paciente['porcentaje_graso'] = float(entry8.get())
    datos_paciente['masa_osea'] = float(entry9.get())
    datos_paciente['masa_muscular'] = float(entry10.get())
    datos_paciente['edad_metabolica'] = float(entry12.get())
    datos_paciente['grasa_visceral'] = float(entry13.get())
    datos_paciente['porcentaje_agua'] = float(entry14.get())


    peso = datos_paciente['peso']
    altura_m = datos_paciente['altura'] / 100
    imc = peso / (altura_m * altura_m)


    datos_paciente_list = [
        datos_paciente['nombre'],
        datos_paciente['apellido'],
        datos_paciente['edad'],
        datos_paciente['genero'],
        datos_paciente['altura'],
        datos_paciente['peso'],
        datos_paciente['actividad'],
        datos_paciente['medida_cintura'],
        datos_paciente['porcentaje_graso'],
        datos_paciente['masa_osea'],
        datos_paciente['masa_muscular'],
        imc,  # IMC calculado
        datos_paciente['edad_metabolica'],
        datos_paciente['grasa_visceral'],
        datos_paciente['porcentaje_agua']
    ]

    return datos_paciente_list

def create_patient(data):
    """creamos el paciente"""
    try:
        new_patient = ScalePatient(*data)
        return new_patient
    except (ValueError, GenderError, ActivityError) as e:
        print("Error al crear al paciente:", e)
        return None





def imc_button():
    """boton para mostrar el imc"""
    try:
        peso = float(entry5.get())
        altura = float(entry4.get())
        altura_imc = altura / 100

        imc = peso / (altura_imc * altura_imc)

        label_imc.configure(text=f"IMC: {imc:.2f}", font=('Century Gothic', 25))
    except ValueError:
        label_imc.configure(text="Error: Ingrese números válidos", font=('Century Gothic', 10))


def patient_review():
    """mostramos la review del paciente al nutricionista"""
    data_patient = get_data()
    patient = create_patient(data_patient)
    app.destroy()

    if patient:
        chart_generator = ChartGenerator(patient)
        patient_review_window = ctk.CTk()
        pt_window_width = 900
        pt_window_height = 800
        pt_frame_width = pt_window_width // 2


        data_pt_frame = ctk.CTkFrame(master=patient_review_window, width=pt_frame_width, height=616)
        data_pt_frame.place(x=0, y=0)

        graph_pt_frame = ctk.CTkFrame(master=patient_review_window, width=pt_frame_width, height=616)
        graph_pt_frame.place(x=pt_frame_width, y=0)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        patient_review_window.geometry("900x800")
        patient_review_window.title("Agernatura")

        figs = [chart_generator.get_imc_graf(),
                chart_generator.get_gc_graf(),
                chart_generator.get_wl_graf(),
                chart_generator.get_cvrisk_graf()
                ]
        for i, fig in enumerate(figs):
            canvas = FigureCanvasTkAgg(fig, master=graph_pt_frame)
            canvas.get_tk_widget().grid(row=i, column=0)

        pt_l1 = ctk.CTkLabel(master=patient_review_window, text=f"{patient.name} {patient.surname} ",
                             font=('Century Gothic', 40))
        pt_l1.place(x=10, y=10)

        pt_l2 = ctk.CTkLabel(master=data_pt_frame,
                             text=f"Calorias diarias necesarias: {round(patient.get_basal_metabolic_rate(), 2)} ",
                             font=('Century Gothic', 22))
        pt_l2.place(x=10, y=90)

        pt_l3 = ctk.CTkLabel(master=data_pt_frame,
                             text=f"Riesgo cardiovascular: {patient.get_cardiovascular_risk()}",
                             font=('Century Gothic', 22))
        pt_l3.place(x=10, y=160)

        pt_l4 = ctk.CTkLabel(master=data_pt_frame, text=f"{patient.get_complexion()}", font=('Century Gothic', 22))
        pt_l4.place(x=10, y=230)

        pt_l5 = ctk.CTkLabel(master=data_pt_frame, text=f"IMC: {patient.get_imc_standard()}",
                             font=('Century Gothic', 22))
        pt_l5.place(x=10, y=300)

        pt_l6 = ctk.CTkLabel(master=data_pt_frame, text=f"% Graso: {patient.get_grass_percent()}",
                             font=('Century Gothic', 22))
        pt_l6.place(x=10, y=370)

        pt_l7 = ctk.CTkLabel(master=data_pt_frame, text=f"Niveles de Agua: {patient.get_w_level()}",
                             font=('Century Gothic', 22))
        pt_l7.place(x=10, y=440)

        pt_l8 = ctk.CTkLabel(master=data_pt_frame, text=f"I. Masa muscular: {patient.get_im_muscular()}",
                             font=('Century Gothic', 22))
        pt_l8.place(x=10, y=510)

        pt_l9 = ctk.CTkLabel(master=data_pt_frame,
                             text=f"Grasa visceral: '{patient.visceral_grass}' {patient.get_ev_gv()}",
                             font=('Century Gothic', 22))
        pt_l9.place(x=10, y=580)

        pt_l10 = ctk.CTkLabel(master=patient_review_window, text=f"Observaciones:", font=('Century Gothic', 25))
        pt_l10.place(x=10, y=620)

        text_obs = ctk.CTkTextbox(master=patient_review_window, width=650, height=130, wrap="word",
                                  font=('Century Gothic', 15))
        text_obs.place(x=10, y=650)

        pt_l11 = ctk.CTkLabel(master=patient_review_window, text=f"Datos:", font=('Century Gothic', 25))
        pt_l11.place(x=670, y=620)

        texto_datos = (
            """Mariló *****
Dietista nutricionista
N. coleg: AND 004**
Telf: 652 ** 77 **
marilo*****@gmail.com"""
        )
        pt_l12 = ctk.CTkLabel(master=patient_review_window, text=texto_datos, justify="left",
                              font=('Century Gothic', 20))
        pt_l12.place(x=670, y=655)

        patient_review_window.mainloop()


    else:
        raise FormError
def resource_path(relative_path):
    """para solucionar posibles problemas con el pathing del fondo"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


img1 = ImageTk.PhotoImage(Image.open(resource_path("Images/pattern.png")))
l1 = ctk.CTkLabel(master=app, image=img1)
l1.pack()


frame = ctk.CTkFrame(master=l1, width=500, height=480, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

label_imc = ctk.CTkLabel(master=frame, width=200, text="", font=('Century Gothic', 22))
label_imc.place(x=30, y=320)

l2 = ctk.CTkLabel(master=frame, text="Datos de paciente", font=('Century Gothic', 22))
l2.place(x=150, y=15)

entry1 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Nombre')
entry1.place(x=30, y=70)

entry2 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Apellidos')
entry2.place(x=260, y=70)

entry3 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Edad')
entry3.place(x=30, y=120)

entry4 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Altura')
entry4.place(x=260, y=120)

entry5 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Peso')
entry5.place(x=30, y=170)


entry7 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Medida de Cintura')
entry7.place(x=30, y=220)

entry8 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Porcentaje Graso')
entry8.place(x=260, y=220)

entry9 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Masa Ósea')
entry9.place(x=30, y=270)

entry10 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Masa Muscular')
entry10.place(x=260, y=270)


dropdown_actividad = ctk.CTkComboBox(master=frame, values=["Sedentario", "Poco activo", "Activo con moderacion", "Activo", "Muy activo"], dropdown_hover_color="grey", width=200, border_color="grey")
dropdown_actividad.place(x=260, y=170)


entry12 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Edad Metabolica')
entry12.place(x=260, y=320)

entry13 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Grasa Visceral')
entry13.place(x=30, y=370)

entry14 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Porcentaje Agua')
entry14.place(x=260, y=370)

entry15 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Género "h o m"')
entry15.place(x=30, y=420)

button_patient_review = ctk.CTkButton(master=frame, width=150, text="Enviar", command=patient_review, corner_radius=16)
button_patient_review.place(x=280, y=420)

button_get_imc = ctk.CTkButton(master=frame, width=10,height=10, text="IMC", command=imc_button, corner_radius=16)
button_get_imc.place(x=00, y=320)

app.mainloop()