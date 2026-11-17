#-----------
#ejercicio 1
#-----------
print("=== 1. Numerales mayas ===")
VALOR_SIMBOLO = {"●": 1, "▬": 5, "◎": 0}   # punto, barra, concha

def nivel_a_valor(nivel):
    return sum(VALOR_SIMBOLO[s] for s in nivel)

def maya_a_decimal(niveles):
    """niveles: lista de cadenas, del nivel MÁS ALTO al más bajo."""
    total = 0
    for nivel in niveles:
        total = total * 20 + nivel_a_valor(nivel)
    return total

def decimal_a_maya(n):
    if n == 0:
        return ["◎"]
    niveles = []
    while n > 0:
        n, resto = divmod(n, 20)
        barras, puntos = divmod(resto, 5)
        niveles.append("●" * puntos + "▬" * barras if resto else "◎")
    return niveles[::-1]

print(maya_a_decimal(["●", "◎"]))          # 20
print(maya_a_decimal(["●●", "▬▬●●●"]))     # 2*20 + 13 = 53
print(decimal_a_maya(2026))                # ['●●●●▬', '▬', '●▬']

#-----------
#ejercicio 2
#-----------
print("\n=== 2. Herbario ===")
herbario = [
    ("Agave tequilana", "Asparagaceae", "Jalisco"),
    ("Opuntia ficus-indica", "Cactaceae", "Zacatecas"),
    ("Tagetes erecta", "Asteraceae", "Puebla"),
    ("Dahlia coccinea", "Asteraceae", "Hidalgo"),
    ("Echinocactus platyacanthus", "Cactaceae", "San Luis Potosí"),
    ("Yucca filifera", "Asparagaceae", "Coahuila"),
    ("Theobroma cacao", "Malvaceae", "Tabasco"),
    ("Ceiba pentandra", "Malvaceae", "Yucatán"),
]

por_familia = {}
por_estado = {}
for especie, familia, estado in herbario:
    por_familia.setdefault(familia, []).append(especie)
    por_estado.setdefault(estado, []).append(especie)

print(por_familia["Cactaceae"])
print(por_estado.get("Tabasco", "Sin ejemplares"))
print(por_estado.get("Sonora", "Sin ejemplares"))

#-----------
#ejercicio 3
#-----------
print("\n=== 3. Codones ===")
CODONES = {
    "AUG": "Met", "UUU": "Phe", "UUC": "Phe", "UGG": "Trp",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
    "GCU": "Ala", "AAA": "Lys", "GAU": "Asp", "CAU": "His",
    "CUU": "Leu", "UAA": "STOP", "UAG": "STOP", "UGA": "STOP",
}

def traducir(arn):
    inicio = arn.find("AUG")
    if inicio == -1:
        return []
    proteina = []
    for i in range(inicio, len(arn) - 2, 3):
        aa = CODONES.get(arn[i:i + 3], "?")
        if aa == "STOP":
            break
        proteina.append(aa)
    return proteina

print("-".join(traducir("CCAUGUUUGGAAAAUGGCAUUAGGCU")))  # Met-Phe-Gly-Lys-Trp-His

#-----------
#ejercicio 4
#-----------
print("\n=== 4. Metro CDMX ===")
lineas = {
    "1": ["Tacubaya", "Insurgentes", "Balderas", "Salto del Agua",
          "Pino Suárez", "Merced", "Pantitlán"],
    "2": ["Hidalgo", "Bellas Artes", "Allende", "Zócalo",
          "Pino Suárez", "San Antonio Abad", "Chabacano"],
    "3": ["Guerrero", "Hidalgo", "Juárez", "Balderas",
          "Niños Héroes", "Hospital General", "Centro Médico"],
    "8": ["Garibaldi", "Bellas Artes", "San Juan de Letrán",
          "Salto del Agua", "Doctores", "Obrera", "Chabacano"],
    "9": ["Tacubaya", "Patriotismo", "Chilpancingo", "Centro Médico",
          "Lázaro Cárdenas", "Chabacano", "Jamaica", "Pantitlán"],
}

estacion_lineas = {}
for linea, estaciones in lineas.items():
    for est in estaciones:
        estacion_lineas.setdefault(est, set()).add(linea)

transbordos = {e: sorted(l) for e, l in estacion_lineas.items() if len(l) > 1}
print(transbordos)

def linea_comun(a, b):
    return estacion_lineas.get(a, set()) & estacion_lineas.get(b, set())

print("Zócalo -> Chabacano sin transbordo:", linea_comun("Zócalo", "Chabacano"))
print("Garibaldi -> Jamaica sin transbordo:", linea_comun("Garibaldi", "Jamaica"))

#-----------
#ejercicio 5
#-----------
print("\n=== 5. Anagramas ===")
palabras = ["amor", "roma", "ramo", "mora", "omar", "saco", "cosa",
            "caso", "asco", "lámina", "animal", "manila", "trigo", "tigre"]

def firma(palabra):
    sin_acentos = palabra.lower().translate(str.maketrans("áéíóú", "aeiou"))
    return "".join(sorted(sin_acentos))

indice_anagramas = {}
for p in palabras:
    indice_anagramas.setdefault(firma(p), []).append(p)

def anagramas_de(palabra):
    return [p for p in indice_anagramas.get(firma(palabra), []) if p != palabra]

print(anagramas_de("amor"))
print(anagramas_de("animal"))
print(anagramas_de("trigo"))

#-----------
#ejercicio 6
#-----------
print("\n=== 6. Fotos duplicadas ===")
import hashlib

fotos = {   # nombre de archivo -> contenido (bytes simulados)
    "IMG_001.jpg": b"\xff\xd8 atardecer en Bacalar",
    "copia de IMG_001.jpg": b"\xff\xd8 atardecer en Bacalar",
    "IMG_002.jpg": b"\xff\xd8 ajolote en Xochimilco",
    "WhatsApp Image.jpg": b"\xff\xd8 ajolote en Xochimilco",
    "IMG_003.jpg": b"\xff\xd8 piramide de Teotihuacan",
}

por_huella = {}
for nombre, contenido in fotos.items():
    huella = hashlib.sha256(contenido).hexdigest()
    por_huella.setdefault(huella, []).append(nombre)

for huella, nombres in por_huella.items():
    if len(nombres) > 1:
        print(huella[:12], "->", nombres)

#-----------
#ejercicio 7
#-----------
print("\n=== 7. Sismos ===")
sismos = [
    {"fecha": "1985-09-19", "estado": "Michoacán", "mag": 8.1},
    {"fecha": "2017-09-07", "estado": "Chiapas", "mag": 8.2},
    {"fecha": "2017-09-19", "estado": "Puebla", "mag": 7.1},
    {"fecha": "2018-02-16", "estado": "Oaxaca", "mag": 7.2},
    {"fecha": "2020-06-23", "estado": "Oaxaca", "mag": 7.4},
    {"fecha": "2021-09-07", "estado": "Guerrero", "mag": 7.0},
    {"fecha": "2022-09-19", "estado": "Michoacán", "mag": 7.6},
]

idx_estado, idx_magnitud = {}, {}
for s in sismos:
    idx_estado.setdefault(s["estado"], []).append(s)
    idx_magnitud.setdefault(int(s["mag"]), []).append(s)   # cubeta 7.x, 8.x

print([s["fecha"] for s in idx_estado["Oaxaca"]])
print([(s["estado"], s["mag"]) for s in idx_magnitud.get(8, [])])
dias_19 = [s["fecha"] for s in sismos if s["fecha"].endswith("09-19")]
print("Sismos un 19 de septiembre:", dias_19)

#-----------
#ejercicio 8
#-----------
print("\n=== 8. Aves ===")
bitacora = ["colibrí", "zanate", "garza", "zanate", "colibrí", "quetzal",
            "zanate", "pelícano", "garza", "zanate", "colibrí"]

conteo = {}
for ave in bitacora:
    conteo[ave] = conteo.get(ave, 0) + 1

print(conteo)
mas_vista = max(conteo, key=conteo.get)
print("Más vista:", mas_vista, conteo[mas_vista])
print("¿Se vio un ajolote?", "ajolote" in conteo)
raras = [ave for ave, n in conteo.items() if n == 1]
print("Vistas una sola vez:", raras)

#-----------
#ejercicio 9
#-----------
print("\n=== 9. Chapulín (memoización) ===")
import time

def saltos_lento(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return saltos_lento(n - 1) + saltos_lento(n - 2) + saltos_lento(n - 3)

cache = {}
def saltos_rapido(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = saltos_rapido(n - 1) + saltos_rapido(n - 2) + saltos_rapido(n - 3)
    return cache[n]

t = time.perf_counter(); r1 = saltos_lento(25); t1 = time.perf_counter() - t
t = time.perf_counter(); r2 = saltos_rapido(25); t2 = time.perf_counter() - t
print(f"n=25 sin caché: {r1} en {t1:.4f} s")
print(f"n=25 con caché: {r2} en {t2:.6f} s")
print("n=100:", saltos_rapido(100))

#-----------
#ejercicio 10
#-----------
print("\n=== 10. Tabla hash propia ===")

class Guardarropa:
    def __init__(self, ganchos=7):
        self.ganchos = [[] for _ in range(ganchos)]   # cada gancho = cubeta

    def _hash(self, clave):
        # hash polinomial simple (base 31) módulo número de ganchos
        h = 0
        for c in clave:
            h = (h * 31 + ord(c)) % len(self.ganchos)
        return h

    def guardar(self, visitante, objeto):
        cubeta = self.ganchos[self._hash(visitante)]
        for par in cubeta:
            if par[0] == visitante:
                par[1] = objeto          # actualiza si ya existía
                return
        cubeta.append([visitante, objeto])   # colisión -> se encadena

    def buscar(self, visitante):
        for clave, objeto in self.ganchos[self._hash(visitante)]:
            if clave == visitante:
                return objeto
        return None

    def mostrar(self):
        for i, cubeta in enumerate(self.ganchos):
            print(f"gancho {i}: {cubeta}")

g = Guardarropa()
for v, o in [("Frida", "rebozo"), ("Diego", "sombrero"), ("Remedios", "paraguas"),
             ("Leonora", "mochila"), ("Rufino", "abrigo"), ("Lola", "bolsa"),
             ("Juan", "chamarra"), ("Elena", "bufanda")]:
    g.guardar(v, o)
g.mostrar()
print("Objeto de Leonora:", g.buscar("Leonora"))
print("Objeto de Octavio:", g.buscar("Octavio"))
