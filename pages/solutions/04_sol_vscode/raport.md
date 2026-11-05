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
## 4. Rzut ukośny z oporem powietrza

W rzeczywistych warunkach ruch ciała odbywa się w ośrodku materialnym, takim jak powietrze. Powoduje to występowanie dodatkowej siły oporu, która działa przeciwnie do kierunku prędkości ciała.

W niniejszym raporcie przyjęto model oporu proporcjonalnego do kwadratu wartości prędkości.

### 4.1. Siła oporu powietrza

Siłę oporu aerodynamicznego opisuje wzór:

$$
F_o=\frac{1}{2}\rho C_d A v^2
$$

gdzie:

- \(\rho\) – gęstość powietrza \([\text{kg/m}^3]\),
- \(C_d\) – współczynnik oporu aerodynamicznego,
- \(A\) – powierzchnia przekroju poprzecznego ciała \([\text{m}^2]\),
- \(v\) – wartość prędkości ciała \([\text{m/s}]\).

Siła oporu jest skierowana przeciwnie do wektora prędkości. Jej zapis wektorowy ma postać:

$$
\vec{F}_o=-\frac{1}{2}\rho C_d A v\vec{v}
$$

Wprowadzając pomocnicze oznaczenie:

$$
k=\frac{1}{2}\rho C_d A
$$

otrzymujemy uproszczony zapis:

$$
\vec{F}_o=-kv\vec{v}
$$

### 4.2. Równania ruchu z oporem powietrza

Zgodnie z drugą zasadą dynamiki Newtona na ciało działa suma siły ciężkości oraz siły oporu powietrza:

$$
m\vec{a}=\vec{F}_g+\vec{F}_o
$$

Rozpatrując osobno obie osie współrzędnych, otrzymujemy:

$$
m\frac{dv_x}{dt}=-kvv_x
$$

$$
m\frac{dv_y}{dt}=-mg-kvv_y
$$

Dzieląc równania przez masę ciała:

$$
\frac{dv_x}{dt}=-\frac{k}{m}vv_x
$$

$$
\frac{dv_y}{dt}=-g-\frac{k}{m}vv_y
$$

Wartość prędkości wypadkowej wyznaczamy z twierdzenia Pitagorasa:

$$
v=\sqrt{v_x^2+v_y^2}
$$

Otrzymujemy układ czterech równań różniczkowych opisujących cały ruch:

$$
\frac{dx}{dt}=v_x
$$

$$
\frac{dy}{dt}=v_y
$$

$$
\frac{dv_x}{dt}=-\frac{k}{m}\sqrt{v_x^2+v_y^2}\,v_x
$$

$$
\frac{dv_y}{dt}=-g-\frac{k}{m}\sqrt{v_x^2+v_y^2}\,v_y
$$

W przeciwieństwie do modelu bez oporu powietrza, powyższe równania są nieliniowe. Oznacza to, że nie można bezpośrednio zastosować prostych wzorów na czas lotu i zasięg.

### 4.3. Parametry symulacji

Do przeprowadzenia symulacji przyjęto następujące wartości:

| Parametr | Symbol | Wartość | Jednostka |
|---|---|---:|---|
| Masa ciała | \(m\) | 0,20 | kg |
| Gęstość powietrza | \(\rho\) | 1,225 | kg/m³ |
| Współczynnik oporu | \(C_d\) | 0,47 | - |
| Powierzchnia przekroju | \(A\) | 0,01 | m² |
| Prędkość początkowa | \(v_0\) | 20 | m/s |
| Kąt wyrzutu | \(\alpha\) | 45 | ° |
| Przyspieszenie ziemskie | \(g\) | 9,81 | m/s² |

Przyjęte parametry odpowiadają uproszczonemu modelowi niewielkiego kulistego ciała poruszającego się w powietrzu.

Wartość współczynnika oporu jest przybliżona i w rzeczywistości może zależeć od kształtu ciała oraz warunków przepływu powietrza.

### 4.4. Warunki początkowe

Na początku symulacji ciało znajduje się w punkcie początkowym układu współrzędnych:

$$
x(0)=0
$$

$$
y(0)=0
$$

Początkowe składowe prędkości wynoszą:

$$
v_x(0)=v_0\cos\alpha
$$

$$
v_y(0)=v_0\sin\alpha
$$

Dla przyjętych parametrów:

$$
v_x(0)\approx14{,}14\ \text{m/s}
$$

$$
v_y(0)\approx14{,}14\ \text{m/s}
$$

### 4.5. Metoda rozwiązania numerycznego

Ze względu na nieliniowy charakter równań różniczkowych zastosowana zostanie metoda numeryczna. W symulacji wykorzystany będzie algorytm Rungego-Kutty czwartego rzędu (RK4).

Metoda ta pozwala przybliżać rozwiązania układów równań różniczkowych poprzez obliczanie kolejnych wartości funkcji w niewielkich odstępach czasu.

W symulacji przyjęty zostanie krok czasowy:

$$
\Delta t=0{,}01\ \text{s}
$$

Obliczenia będą wykonywane aż do momentu zetknięcia ciała z podłożem, czyli osiągnięcia warunku:

$$
y(t)\leq 0
$$

Dzięki temu możliwe będzie wyznaczenie toru ruchu, czasu lotu oraz zasięgu rzutu z uwzględnieniem oporu powietrza.