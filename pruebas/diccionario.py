evaluaciones = dict()
print(evaluaciones)
evaluaciones["SA"] = "Satisfactorio"
evaluaciones["DE"] = "Destacado"
evaluaciones["AU"] = "Auto suficiente"
evaluaciones["NA"] = "No acreditado"
print (evaluaciones["DE"])
# print(evaluaciones["9"])
evaluaciones["DE"]="Des"
print(evaluaciones)
print(len(evaluaciones))
print ("DE" in evaluaciones)
print(evaluaciones.keys())
print(evaluaciones.values())
print("Reprobado" in evaluaciones.values())
del evaluaciones["DE"]
print(len(evaluaciones))

# alumnos = dict()
# alumnos={1: "Juan", 2: "Ana"}
# alumnos[3]="Luisa"
# alumnos[4]="Oscar"
# print(alumnos)

# tic=["Si","MC"]
# carreras=dict()
# carreras["TIC"]=tic
# print(carreras)