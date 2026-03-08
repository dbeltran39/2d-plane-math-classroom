# 2D Plane Math Classroom

Projecte educatiu per treballar **moviments al pla** (translacions, girs i simetries) a través d'un petit videojoc programat amb **Python i Pygame**.

Aquest projecte està pensat per ser utilitzat a l'aula de **3r d'ESO** dins de la unitat didàctica de **moviments al pla**.

**Institut Escola Lluís Millet**
Autor: **David Beltran Lacasa**

---

# Objectiu educatiu

L'objectiu del projecte és connectar els conceptes matemàtics de geometria amb una aplicació visual i interactiva.

Els alumnes implementen funcions matemàtiques que controlen el moviment d'un avió dins d'un entorn gràfic.

D'aquesta manera poden observar com:

* una **translació** desplaça un objecte al pla
* un **gir** canvia la seva orientació
* les **simetries** transformen la figura
* les **transformacions** es poden combinar

Aquest enfocament permet treballar també elements de **pensament computacional**.

---

# Estructura del projecte

```
2d-plane-math-classroom/

assets/          # sprites i imatges
engine/          # motor del joc
activities/      # activitats pels alumnes

main.py          # punt d'entrada del joc
requirements.txt # dependències
README.md
```

---

# Carpetes

## assets

Conté els recursos gràfics utilitzats pel joc.

Per exemple:

```
assets/avio_vermell.png
```

---

## engine

Conté el **motor del joc**.

Aquesta part no es modifica durant l'activitat.

Inclou funcionalitats com:

* renderització
* gestió del joc
* dibuix del fons i dels núvols
* gestió de l'sprite de l'avió

---

## activities

Conté les activitats que els alumnes han de completar.

Exemple:

```
activities/rotation_and_translation.py
```

Els alumnes han d'implementar funcions matemàtiques com:

* translacions
* girs

---

# Activitat 1 — Moviments al pla

Els alumnes han d'implementar dues funcions:

```
translacio(x, y, dx, dy)
gir(x, y, angle)
```

Aquestes funcions controlen el moviment de l'avió.

---

## Translació

Matemàticament:

```
(x, y) → (x + dx, y + dy)
```

---

## Gir

Gir d'un punt respecte l'origen:

```
x' = x cosθ − y sinθ
y' = x sinθ + y cosθ
```

---

# Controls del joc

```
W → pujar
S → baixar
A → gir antihorari
D → gir horari

ESC → sortir
```

---

# Instal·lació

Cal tenir **Python 3.10 o superior**.

Instal·lar dependències:

```
pip install -r requirements.txt
```

---

# Executar el joc

```
python main.py
```

---

# Possibles extensions

Aquest projecte està pensat per créixer amb noves activitats:

* Activitat 1 → Moviments al pla
* Activitat 2 → Enemics i col·lisions
* Activitat 3 → Dispars
* Activitat 4 → Física del moviment

Aquestes extensions permeten integrar:

* vectors
* trigonometria
* detecció de col·lisions
* modelització matemàtica

---

# Context educatiu

Aquest projecte forma part d'una **intervenció didàctica sobre moviments al pla** desenvolupada dins del màster de professorat.

Els continguts s'alineen amb el currículum de matemàtiques de secundària:

**DECRET 175/2022, de 27 de setembre, d’ordenació dels ensenyaments de l’educació bàsica.**

---

# Llicència

Aquest projecte es pot utilitzar amb finalitats educatives.

