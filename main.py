import sqlite3

DB_NAME = "estudiantes.db"

class Estudiante:
    def __init__(self, nombre, carrera, promedio):
        self.nombre = nombre
        self.carrera = carrera
        self.promedio = promedio

    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                id_estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                carrera TEXT NOT NULL,
                promedio REAL
            );
        """)
        conn.commit()
        return conn

    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO estudiantes (nombre, carrera, promedio) VALUES (?, ?, ?)",
                (self.nombre, self.carrera, self.promedio)
            )
        print(f"Estudiante '{self.nombre}' guardado con éxito.")

    @staticmethod
    def listar():
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT * FROM estudiantes")
            filas = cur.fetchall()
            if not filas:
                print("No hay estudiantes registrados.")
                return
            print("\n--- LISTADO DE ESTUDIANTES ---")
            for f in filas:
                print(f"ID: {f['id_estudiante']} | Nombre: {f['nombre']} | Carrera: {f['carrera']} | Promedio: {f['promedio']}")

    @staticmethod
    def modificar():
        ide = input("Ingrese ID del estudiante a modificar: ")
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT * FROM estudiantes WHERE id_estudiante = ?", (ide,))
            fila = cur.fetchone()
            if not fila:
                print("No se encontró el estudiante.")
                return
            nombre = input(f"Nuevo nombre [{fila['nombre']}]: ") or fila['nombre']
            carrera = input(f"Nueva carrera [{fila['carrera']}]: ") or fila['carrera']
            promedio = input(f"Nuevo promedio [{fila['promedio']}]: ") or fila['promedio']
            conn.execute("UPDATE estudiantes SET nombre=?, carrera=?, promedio=? WHERE id_estudiante=?",
                         (nombre, carrera, promedio, ide))
        print("Estudiante actualizado con éxito.")

    @staticmethod
    def eliminar():
        ide = input("Ingrese ID del estudiante a eliminar: ")
        with Estudiante._conn() as conn:
            cur = conn.execute("DELETE FROM estudiantes WHERE id_estudiante = ?", (ide,))
            if cur.rowcount == 0:
                print("No se encontró el estudiante.")
            else:
                print("Estudiante eliminado con éxito.")

    @staticmethod
    def promedio_general():
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT AVG(promedio) AS prom FROM estudiantes")
            prom = cur.fetchone()["prom"]
            if prom:
                print(f"\nPromedio general: {prom:.2f}")
            else:
                print("No hay datos para calcular el promedio.")



class Curso:
    def __init__(self,nombre, docente):
        self.nombre = nombre
        self.docente = docente

    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute("""
               CREATE TABLE IF NOT EXISTS cursos (
                   matricula INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   docente TEXT NOT NULL
               );
           """)
        conn.commit()
        return conn

    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO cursos (nombre, docente) VALUES (?, ?)",
                (self.nombre, self.docente)
            )
        print(f"Curso '{self.nombre}' guardado con éxito.")

    @staticmethod
    def listar():
        with Curso._conn() as conn:
            cur = conn.execute("SELECT * FROM cursos")
            filas = cur.fetchall()
            if not filas:
                print("No hay cursos registrados.")
                return
            print("\n--- LISTADO DE CURSOS ---")
            for f in filas:
                print(f"ID: {f['matricula']} | Nombre: {f['nombre']} | Docente: {f['docente']} ")

    @staticmethod
    def modificar():
        matricula = input("Ingrese la matricula del curso a modificar: ")
        with Curso._conn() as conn:
            cur = conn.execute("SELECT * FROM cursos WHERE matricula = ?", (matricula,))
            fila = cur.fetchone()
            if not fila:
                print("No se encontró el curso.")
                return
            nombre = input(f"Nuevo nombre [{fila['nombre']}]: ") or fila['nombre']
            docente = input(f"Nueva carrera [{fila['docente']}]: ") or fila['docente']
            conn.execute("UPDATE cursos SET nombre=?, docente=? WHERE matricula=?",
                         (nombre, docente, matricula))
        print("Curso actualizado con éxito.")

    @staticmethod
    def eliminar():
        matricula = input("Ingrese ID de la matricula a eliminar: ")
        with Curso._conn() as conn:
            cur = conn.execute("DELETE FROM cursos WHERE id_estudiante = ?", (matricula,))
            if cur.rowcount == 0:
                print("No se encontró el curso.")
            else:
                print("Curso eliminado con éxito.")


class Docente:
    def __init__(self, nombre):
        self.nombre = nombre

    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute("""
                  CREATE TABLE IF NOT EXISTS docentes(
                      codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                      nombre TEXT NOT NULL
                  );
              """)
        conn.commit()
        return conn

    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO cursos (nombre) VALUES (?)",
                (self.nombre,)
            )
        print(f"Docente '{self.nombre}' guardado con éxito.")

    @staticmethod
    def listar():
        with Docente._conn() as conn:
            cur = conn.execute("SELECT * FROM docentes")
            filas = cur.fetchall()
            if not filas:
                print("No hay docentes registrados.")
                return
            print("\n--- LISTADO DE DOCENTES ---")
            for f in filas:
                print(f"Nombre: {f['nombre']}")

    @staticmethod
    def modificar():
        codigo = input("Ingrese el codigo del docente a modificar: ")
        with Docente._conn() as conn:
            cur = conn.execute("SELECT * FROM docentes WHERE codigo = ?", (codigo,))
            fila = cur.fetchone()
            if not fila:
                print("No se encontró el docente.")
                return
            nombre = input(f"Nuevo nombre [{fila['nombre']}]: ") or fila['nombre']
            conn.execute("UPDATE docentes SET nombre=? WHERE codigo=?",
                         (nombre,))
        print("Curso actualizado con éxito.")

    @staticmethod
    def eliminar():
        codigo = input("Ingrese el código del docente a eliminar: ")
        with Docente._conn() as conn:
            cur = conn.execute("DELETE FROM docentes WHERE codigo = ?", (codigo,))
            if cur.rowcount == 0:
                print("No se encontró el docente.")
            else:
                print("docente eliminado con éxito.")
def submenu_1():
    while True:
        print('1. Crear Curso\n2. Listar Cursos\n3. Modificar curso\n4. Eliminar Curso\n5. Regresar')
        op = input('Ingrese una opción: ')
        match op:
            case 1:
                nombre = input('Nombre: ')
                docente = input('Docente: ')
                tmp = Curso(nombre, docente)
                tmp.guardar() #se guarda el objeto en las tablas

            case 2:
                Curso.listar()
            case 3:
                Curso.modificar()
            case 4:
                Curso.eliminar()
            case 5:
                print('Regresando')
                break
            case _:
                print('Error opcion incorrecta')

def submenu_2():

    while True:
        print('1. Agregar Docente\n2. Listar docentes\n3. Modificar Docentes\n4. Eliminar docente\n5. Regresar')
        op2 = input('Ingrese una opción: ')
        match op2:
            case 1:
                nombre  = input('Nombre: ')
                tmp_doc = Docente(nombre)
                tmp_doc.guardar()
            case 2:
                Docente.listar()
            case 3:
                Docente.modificar()
            case 4:
                Docente.eliminar()
            case 5:
                print('Regresando...')
                break
            case _:
                print('Error por favor ingrese una opción valida')


# --- MENÚ PRINCIPAL ---
def menu():
    while True:
        print("\n===== MENÚ DE ESTUDIANTES =====")
        print("1. Ingresar estudiante")
        print("2. Listar estudiantes")
        print("3. Modificar estudiante")
        print("4. Eliminar estudiante")
        print("5. Promedio general")
        print("6. Submenú Cursos")
        print("7. Submenú  docentes")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            carrera = input("Carrera: ")
            promedio = float(input("Promedio: "))
            e = Estudiante(nombre, carrera, promedio)
            e.guardar()
        elif opcion == "2":
            Estudiante.listar()
        elif opcion == "3":
            Estudiante.modificar()
        elif opcion == "4":
            Estudiante.eliminar()
        elif opcion == "5":
            Estudiante.promedio_general()
        elif opcion == "6":
            submenu_1()
        elif opcion == "7":
            submenu_2()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()