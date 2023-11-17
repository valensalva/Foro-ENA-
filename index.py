import tkinter as tk

import sqlite3

#ventana de registro

login = tk.Tk()
login.title("ENA!")
login.geometry("400x200")

db_name = "database.db"

def runquery(query, parametro = () ):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(query, parametro)
        result = conn.commit()
    return result

titulo1 = tk.Label(login, text="Bienvenido, ingrese a su cuenta o cree una nueva")
titulo1.grid(row=1, column=1, padx= 30,pady=10)

#botones
btnR = tk.Button(login, text="Registrarse", command=lambda:registro())
btnL = tk.Button(login, text="Ingresar", command=lambda:logeo())
btnR.grid(row=2, column=1, pady=20)
btnL.grid(row=3, column=1)

def logeo():
    loginpage= tk.Tk()
    loginpage.geometry("300x200")

    
    #inputs y texto
    texto1 = tk.Label(loginpage, text="Usuario")
    userinput = tk.Entry(loginpage)
    userinput.grid(row=2, column=1,padx= 60)
    texto1.grid(row=1, column=1,padx= 60)

    texto2 = tk.Label(loginpage, text="Contraseña")
    passinput = tk.Entry(loginpage)
    passinput.grid(row=4, column=1,padx= 60)
    texto2.grid(row=3, column=1,padx= 60)


    def dbcomparar():
        user = userinput.get()
        print(user)

    btnLogear = tk.Button(loginpage, text="Ingresar", command=lambda:dbcomparar())
    btnLogear.grid(row=5, column=1, pady=10)

    loginpage.mainloop()
    
def registro():
    registerpage= tk.Tk()
    registerpage.geometry("300x200")

    #inputs y texto
    texto1 = tk.Label(registerpage, text="Usuario")
    userinput = tk.Entry(registerpage)
    userinput.grid(row=2, column=1,padx= 60)
    texto1.grid(row=1, column=1,padx= 60)

    texto2 = tk.Label(registerpage, text="Contraseña")
    passinput = tk.Entry(registerpage)
    passinput.grid(row=4, column=1,padx= 60)
    texto2.grid(row=3, column=1,padx= 60)
    #################################################

    #funcion de boton registrar
    def registrar(user, psw):
        query = "INSERT INTO usuario(nombre,contra) VALUES('{user}','{pasw}')".format(user= user, pasw=psw)
        if (user == "" and psw == ""):
            warning=tk.Tk()
            warning.geometry("200x100")
            wtext=tk.Label(warning, text="Completa los campos forrrrro")
            wboton=tk.Button(warning,text="bueno perdon :(", command=warning.destroy)
            wtext.grid(row=1, column=1)
            wboton.grid(row=2,column=1, pady= 15)
        else:
            runquery(query)
            volverboton=tk.Button(registerpage, text="Volver", command=registerpage.destroy)
            volverboton.grid(row=6, column=1, pady=5)
    #################################################        
        
    btnRegistrar = tk.Button(registerpage, text="Registrar", command=lambda:registrar(userinput.get(), passinput.get()))
    btnRegistrar.grid(row=5, column=1, pady=10)

  

login.mainloop()

