import tkinter as tk
from tkinter import ttk
import sqlite3

def pagina_principal():
    principal = tk.Tk()
    principal.title("Foro ENA!")
    
    principal.mainloop()

#ventana de registro

login = tk.Tk()
login.title("ENA!")
login.geometry("400x200")

db_name = "database.db"

def runquery(query, parametro = () ):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        result = cursor.fetchall()
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
    loginpage.title("Ingresar a ENA!")
    loginpage.geometry("300x200")

    #inputs y texto
    texto1 = tk.Label(loginpage, text="Usuario")
    userinput = tk.Entry(loginpage)
    userinput.grid(row=2, column=1,padx= 60)
    texto1.grid(row=1, column=1,padx= 60)

    texto2 = tk.Label(loginpage, text="Contraseña")
    passinput = tk.Entry(loginpage, show="*")
    passinput.grid(row=4, column=1,padx= 60)
    texto2.grid(row=3, column=1,padx= 60)
    
    def dbcomparar():
        user = userinput.get()
        psw = passinput.get()
        query = "SELECT * FROM usuario WHERE nombre = '{0}' AND contra = '{1}'".format(user, psw)
        res12 = runquery(query)
        if (len(res12)==0):
            warning2=tk.Label(loginpage, text="El usuario o la contraseña no son correctos", fg= "red")
            warning2.grid(row=5, column=1)
            warning2.after(3000, lambda:warning2.grid_forget())
        else:
            loginpage.destroy()
            login.destroy()
            pagina_principal()

    btnLogear = tk.Button(loginpage, text="Ingresar", command=lambda:dbcomparar())
    btnLogear.grid(row=6, column=1, pady=10)

    loginpage.mainloop()

def registro():
    registerpage= tk.Tk()
    registerpage.title("Registrarse en ENA!")
    registerpage.geometry("300x220")

    #inputs y texto
    texto1 = tk.Label(registerpage, text="Usuario")
    userinput = tk.Entry(registerpage)
    userinput.grid(row=2, column=1,padx= 60)
    texto1.grid(row=1, column=1,padx= 60)

    texto2 = tk.Label(registerpage, text="Contraseña")
    passinput = tk.Entry(registerpage, show="*")
    passinput.grid(row=5, column=1,padx= 60)
    texto2.grid(row=4, column=1,padx= 60)
    #################################################

    #funcion de boton registrar
    def registrar(user, psw):
        query = "INSERT INTO usuario(nombre,contra) VALUES('{0}','{1}')".format(user, psw)
        if (user == "" or psw == ""):
            warning=tk.Tk()
            warning.title("forrrrrrrrrro")
            warning.geometry("200x120")
            wtext=tk.Label(warning, text="Completa los campos forrrrro")
            wboton=tk.Button(warning,text="bueno perdon :(", command=warning.destroy)
            wtext.grid(row=1, column=1)
            wboton.grid(row=2,column=1, pady= 15)
        else:
            query2 = "SELECT * FROM usuario WHERE nombre = '{0}'".format(user)
            res12= runquery(query2)
            if (len(res12)== 0):
                runquery(query)
                volverboton=tk.Button(registerpage, text="Volver", command=registerpage.destroy)
                volverboton.grid(row=7, column=1, pady=5)
                logincorrecto = tk.Label(registerpage, text= "Has sido registrado correctamente!", fg="green")
                logincorrecto.grid(row=3,column=1)
                info = logincorrecto.grid_info()
            else:
                warning2=tk.Label(registerpage, text="Ese usuario ya existe, usa otro, puto.", fg= "red")
                warning2.grid(row=3, column=1)
                warning2.after(3000,lambda:warning2.grid_forget())

        if info:
            btnRegistrar["state"] = tk.DISABLED
        
    btnRegistrar = tk.Button(registerpage, text="Registrar", command=lambda:registrar(userinput.get(), passinput.get()))
    btnRegistrar.grid(row=6, column=1, pady=10)

login.mainloop()