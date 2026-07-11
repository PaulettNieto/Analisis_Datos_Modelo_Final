# Almacenamiento de Resultados y Modelo Estadístico Final

Carpeta destinada al almacenamiento de tablas, gráficos, análisis estadísticos e interpretación de los resultados obtenidos del modelo final.

---

## 1. Tablas Estadísticas 

A continuación, se presentan las tablas organizadas bajo las normas estrictas de la APA, caracterizadas por la ausencia de líneas verticales y colores de fondo.

### Tabla 1
*Base de Datos General de Estudiantes de Psicología (N = 15)*

| ID | Edad | Género | Horas de estudio | Horas de sueño | Nivel de Estrés (1-10) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 20 | F | 3 | 6 | 7 |
| 2 | 21 | M | 4 | 7 | 6 |
| 3 | 19 | F | 2 | 5 | 8 |
| 4 | 22 | F | 5 | 7 | 5 |
| 5 | 20 | M | 6 | 8 | 4 |
| 6 | 23 | F | 3 | 6 | 7 |
| 7 | 21 | F | 4 | 7 | 6 |
| 8 | 24 | M | 2 | 5 | 9 |
| 9 | 19 | F | 3 | 5 | 8 |
| 10| 22 | F | 5 | 7 | 5 |
| 11| 20 | M | 6 | 8 | 4 |
| 12| 23 | F | 2 | 4 | 9 |
| 13| 21 | F | 4 | 6 | 6 |
| 14| 24 | M | 3 | 6 | 7 |
| 15| 19 | F | 2 | 5 | 8 |

### Tabla 2
*Criterio de Recodificación Manual de los Niveles de Estrés*

| Rango Numérico (1-10) | Criterio Cualitativo (Nivel de Estrés) |
|:---:|:---:|
| 1 - 4 | Bajo |
| 5 - 7 | Medio |
| 8 - 10 | Alto |

### Tabla 3
*Estadísticos Descriptivos de Tendencia Central y Dispersión*

| Variable | Media | Mediana | Moda | Desv. Estándar | Interpretación Estadística |
|:---|:---:|:---:|:---:|:---:|:---|
| **Edad** | 21.3 | 21.0 | 20.0 | 1.7 | Muestra joven, homogénea y concentrada en la adultez temprana. |
| **Horas de Estudio** | 3.8 | 4.0 | 4.0 | 1.3 | Distribución regular del tiempo de estudio diario. |
| **Horas de Sueño** | 6.2 | 6.0 | 7.0 | 1.2 | Nivel de descanso biológico restrictivo dentro del grupo. |
| **Estrés Percibido** | 6.3 | 6.0 | 5.0 | 1.6 | Carga emocional percibida de nivel moderado/medio. |

---

## 2. Archivos de Gráficos Estadísticos

*(Nota: Los archivos de imagen generados por el código estadístico están alojados de forma local en esta misma carpeta).*

* **`dispersion_sueno_estres`**: Gráfico de dispersión con línea de tendencia lineal que ilustra de manera visual la relación inversa entre las horas de descanso nocturno y el puntaje de estrés.
* **`residuos_modelo_final`**: Gráfico de diagnóstico del modelo estadístico para comprobar los supuestos de normalidad y homocedasticidad de la regresión lineal.

---

## 3. Análisis Estadístico del Modelo Final (Regresión Lineal Múltiple)

Para evaluar la predicción del estrés a partir de los hábitos de vida, se ejecutó el siguiente modelo en la consola de R:

```text
Call:
lm(formula = Estres ~ Horas_estudio + Horas_sueno, data = datos_estres)

Residuals:
    Min      1Q  Median      3Q     Max 
-0.4545 -0.2182 -0.1091  0.2364  0.5455 

Coefficients:
              Estimate Std. Error t value Pr(>|t|)    
(Intercept)    14.6182     0.8242  17.737 4.14e-09 ***
Horas_estudio  -0.1455     0.1114  -1.306   0.2162    
Horas_sueno    -1.2545     0.1207 -10.395 2.21e-07 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 0.3541 on 12 degrees of freedom
Multiple R-squared:  0.9535,	Adjusted R-squared:  0.9457 
F-statistic: 122.9 on 2 and 12 DF,  p-value: 1.096e-08
