# Analiza rzutu ukośnego bez oporu powietrza oraz z uwzględnieniem oporu powietrza

**Przedmiot:** Programy Użytkowe  
**Temat:** Rzut ukośny – analiza teoretyczna i numeryczna  
**Parametry początkowe:**
- Prędkość początkowa: \(v_0 = 20\ \text{m/s}\)
- Kąt wyrzutu: \(\alpha = 45^\circ\)
- Przyspieszenie ziemskie: \(g = 9{,}81\ \text{m/s}^2\)

---

## Spis treści

1. Wstęp
2. Założenia i model fizyczny
3. Rzut ukośny bez oporu powietrza
4. Analiza matematyczna ruchu
5. Rzut ukośny z oporem powietrza
6. Symulacja numeryczna w języku Python
7. Porównanie obu modeli
8. Analiza wykresów
9. Wnioski

---

## 1. Wstęp

Rzut ukośny jest jednym z podstawowych przykładów ruchu w polu grawitacyjnym. Polega na nadaniu ciału prędkości początkowej skierowanej pod określonym kątem względem poziomu.

Ruch ten można rozłożyć na dwa niezależne ruchy:
- ruch jednostajny w kierunku poziomym,
- ruch jednostajnie zmienny w kierunku pionowym.

W rzeczywistych warunkach na poruszające się ciało działa również opór powietrza. Powoduje on zmniejszenie prędkości, skrócenie zasięgu oraz zmianę kształtu toru ruchu.

Celem niniejszego raportu jest przedstawienie matematycznego opisu rzutu ukośnego w dwóch przypadkach: bez uwzględnienia oporu powietrza oraz z jego uwzględnieniem. Dodatkowo przeprowadzona zostanie symulacja komputerowa pozwalająca porównać oba modele.

## 2. Założenia i model fizyczny

W celu uproszczenia analizy przyjęto następujące założenia:

1. Ciało traktowane jest jako punkt materialny.
2. Ruch odbywa się w jednorodnym polu grawitacyjnym Ziemi.
3. Przyspieszenie ziemskie jest stałe i wynosi \(9{,}81\ \text{m/s}^2\).
4. Początkowa wysokość wyrzutu wynosi zero.
5. Prędkość początkowa wynosi \(20\ \text{m/s}\).
6. Kąt wyrzutu wynosi \(45^\circ\).
7. W modelu z oporem powietrza przyjęto opór proporcjonalny do kwadratu prędkości.

### 2.1. Wielkości fizyczne i jednostki SI

| Wielkość | Symbol | Jednostka |
|---|---|---|
| Położenie poziome | \(x\) | m |
| Położenie pionowe | \(y\) | m |
| Czas | \(t\) | s |
| Prędkość | \(v\) | m/s |
| Przyspieszenie | \(a\) | m/s² |
| Przyspieszenie ziemskie | \(g\) | m/s² |
| Masa | \(m\) | kg |
| Siła | \(F\) | N |
| Kąt wyrzutu | \(\alpha\) | rad lub ° |

## 3. Rzut ukośny bez oporu powietrza

W przypadku pominięcia oporu powietrza na ciało działa wyłącznie siła ciężkości. Zgodnie z drugą zasadą dynamiki Newtona:

$$
\vec{F}=m\vec{a}
$$

Siła ciężkości ma postać:

$$
\vec{F}_g=m\vec{g}
$$

Przyjmując układ współrzędnych, w którym oś X jest skierowana poziomo, a oś Y pionowo w górę, otrzymujemy:

$$
a_x=0
$$

$$
a_y=-g
$$

### 3.1. Rozkład prędkości początkowej na składowe

Prędkość początkową można rozłożyć na dwie składowe:

$$
v_{0x}=v_0\cos\alpha
$$

$$
v_{0y}=v_0\sin\alpha
$$

Dla przyjętych parametrów:

$$
v_{0x}=20\cos45^\circ
$$

$$
v_{0x}\approx14{,}14\ \text{m/s}
$$

Analogicznie:

$$
v_{0y}=20\sin45^\circ
$$

$$
v_{0y}\approx14{,}14\ \text{m/s}
$$

### 3.2. Równania prędkości

W kierunku poziomym nie występuje przyspieszenie, dlatego prędkość pozostaje stała:

$$
v_x(t)=v_0\cos\alpha
$$

W kierunku pionowym działa przyspieszenie ziemskie skierowane w dół:

$$
v_y(t)=v_0\sin\alpha-gt
$$

### 3.3. Równania położenia

Korzystając z zależności między prędkością a położeniem, otrzymujemy równania ruchu.

W kierunku poziomym:

$$
x(t)=v_0\cos\alpha\cdot t
$$

W kierunku pionowym:

$$
y(t)=v_0\sin\alpha\cdot t-\frac{1}{2}gt^2
$$

Powyższe równania opisują położenie ciała w dowolnej chwili czasu.

### 3.4. Czas wznoszenia

W najwyższym punkcie toru składowa pionowa prędkości jest równa zero:

$$
v_y(t)=0
$$

Zatem:

$$
v_0\sin\alpha-gt=0
$$

Po przekształceniu:

$$
t_w=\frac{v_0\sin\alpha}{g}
$$

Podstawiając dane:

$$
t_w=\frac{20\sin45^\circ}{9{,}81}
$$

Ostatecznie:

$$
\boxed{t_w\approx1{,}44\ \text{s}}
$$

### 3.5. Maksymalna wysokość

Maksymalną wysokość można obliczyć, podstawiając czas wznoszenia do równania pionowego:

$$
H_{\max}=v_0\sin\alpha\cdot t_w-\frac{1}{2}gt_w^2
$$

Po uproszczeniu otrzymujemy:

$$
H_{\max}=\frac{v_0^2\sin^2\alpha}{2g}
$$

Dla analizowanego przypadku:

$$
H_{\max}=\frac{20^2\sin^245^\circ}{2\cdot9{,}81}
$$

Ostatecznie:

$$
\boxed{H_{\max}\approx10{,}19\ \text{m}}
$$

### 3.6. Całkowity czas lotu

Zakładając, że ciało ląduje na tej samej wysokości, z której zostało wyrzucone, całkowity czas lotu jest dwukrotnością czasu wznoszenia:

$$
T=2t_w
$$

$$
T=\frac{2v_0\sin\alpha}{g}
$$

Ostatecznie:

$$
\boxed{T\approx2{,}88\ \text{s}}
$$

### 3.7. Zasięg rzutu

Zasięg poziomy to odległość, jaką ciało pokonuje w kierunku poziomym podczas całego lotu.

$$
R=v_0\cos\alpha\cdot T
$$

Po podstawieniu wzoru na czas lotu:

$$
R=\frac{v_0^2\sin(2\alpha)}{g}
$$

Dla przyjętych parametrów:

$$
R=\frac{20^2\sin90^\circ}{9{,}81}
$$

Ostatecznie:

$$
\boxed{R\approx40{,}77\ \text{m}}
$$