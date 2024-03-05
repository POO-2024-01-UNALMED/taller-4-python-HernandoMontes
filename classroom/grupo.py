from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        if estudiantes == None:
            estudiantes = []
        self._grupo = grupo
        if asignaturas == None:
            asignaturas = []
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista == None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        variable = "Grupo de estudiantes: " + self._grupo
        return variable

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre