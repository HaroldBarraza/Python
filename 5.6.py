import random

def main():
    print(make_sentence(1, "pasado"))
    print(make_sentence(1, "presente"))
    print(make_sentence(1, "futuro"))
    print(make_sentence(2, "pasado"))
    print(make_sentence(2, "presente"))
    print(make_sentence(2, "futuro"))

def get_determiner(cantidad):
    if cantidad == 1:
        palabras = ["un", "uno", "el"]
    else:
        palabras = ["algunos", "muchos", "el"]
    palabra = random.choice(palabras)
    return palabra

def get_noun(cantidad):
    if cantidad == 1:
        palabras = ["perro", "gato", "árbol", "persona", "libro"]
    else:
        palabras = ["perros", "gatos", "árboles", "personas", "libros"]
    palabra = random.choice(palabras)
    return palabra

def get_verb(cantidad, tiempo):
    if tiempo == "pasado":
        verbos = ["bebió", "comió", "creció", "rió", "pensó", "corrió", "dormió", "habló", "caminó", "escribió"]
    elif tiempo == "presente" and cantidad == 1:
        verbos = ["bebe", "come", "crece", "ríe", "piensa", "corre", "duerme", "habla", "camina", "escribe"]
    elif tiempo == "presente" and cantidad != 1:
        verbos = ["beben", "comen", "crecen", "ríen", "piensan", "corren", "duermen", "hablan", "caminan", "escriben"]
    elif tiempo == "futuro":
        verbos = ["beberá", "comerá", "crecerá", "reirá", "pensará", "correrá", "dormirá", "hablará", "caminará", "escribirá"]
    verbo = random.choice(verbos)
    return verbo

def make_sentence(cantidad, tiempo):

    determinante = get_determiner(cantidad)
    sustantivo = get_noun(cantidad)
    verbo = get_verb(cantidad, tiempo)
    oracion = determinante + " " + sustantivo + " " + verbo + "."
    return oracion.capitalize()
main()
