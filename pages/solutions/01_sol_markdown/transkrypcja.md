
# Transkrypcja

![Zrzut ekranu z odręcznymi notatkami](./zrzut.png)

## Prompt użyty do wygenerowania tekstu przez AI

```text
Dokonaj transkrypcji tekstu widocznego na załączonym obrazie z odręcznymi notatkami. Zachowaj język polski, strukturę nagłówków i list punktowanych oraz poprawnie zapisz wzory matematyczne. Następnie sprawdź transkrypcję pod kątem błędów i nieścisłości, uwzględniając kontekst fizyki kwantowej.
```

## Finalna wersja notatki

### 11. Co to są kropki kwantowe i jakie mają własności?

- **0D – struktura zerowymiarowa.**
- Ruch elektronów jest ograniczony w trzech wymiarach.
- **Najprostszy model – quantum box:** kropka kwantowa w kształcie sześcianu, na zewnątrz którego potencjał jest nieskończony.

**Równanie Schrödingera:**

$$
-\frac{\hbar^2}{2m}
\left(
\frac{\partial^2}{\partial x^2}
+\frac{\partial^2}{\partial y^2}
+\frac{\partial^2}{\partial z^2}
\right)\psi(x,y,z)
=E\psi(x,y,z)
$$

**Energia:**

$$
E=\frac{\hbar^2\pi^2}{2m}
\left(
\frac{n_x^2}{L_x^2}
+\frac{n_y^2}{L_y^2}
+\frac{n_z^2}{L_z^2}
\right)
$$

Gdzie:

- $m$ – masa elektronu,
- $L_x,L_y,L_z$ – długości krawędzi sześcianu,
- $n_x,n_y,n_z=1,2,3,\ldots$ – liczby kwantowe,
- $\hbar$ – zredukowana stała Plancka.

- Stany energetyczne mogą być zdegenerowane.
- **Sferyczna kropka kwantowa** – rozdzielenie funkcji falowej \(\psi\) na część radialną i kątową (podobnie jak w zagadnieniu atomu wodoru w mechanice kwantowej).

Rozwiązanie równania radialnego prowadzi do funkcji Bessela. Dla problemu sferycznie symetrycznego stosuje się sferyczne funkcje Bessela \(j_l(kr)\), które można wyrazić za pomocą funkcji Bessela rzędu \(l+\frac{1}{2}\).
