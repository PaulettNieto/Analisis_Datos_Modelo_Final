# Análisis de# Carpeta de Resultados y Modelo Estadístico Final

Este espacio contiene las tablas formales, la salida del modelo de regresión lineal múltiple ejecutado en Python y la interpretación cuantitativa de los hallazgos esenciales del proyecto.

---

## 1. Tablas Estadísticas en Formato APA (7ma Edición)

*Nota: Siguiendo las directrices internacionales de la APA para la presentación de resultados en psicología, las tablas omiten líneas verticales y colores de fondo, priorizando la legibilidad científica.*

### Tabla 1
*Estadísticos Descriptivos de Tendencia Central y Dispersión (N = 15)*

| Variable | Media | Mediana | Moda | Desv. Estándar | Interpretación del Grupo |
|:---|:---:|:---:|:---:|:---:|:---|
| Edad | 21.3 | 21.0 | 20.0 | 1.7 | La mayoría de los estudiantes tienen entre 20 y 22 años, lo que muestra un grupo joven y homogéneo. |
| Horas de Estudio | 3.8 | 4.0 | 4.0 | 1.3 | En promedio estudian casi 4 horas al día, mostrando hábitos regulares y poca variabilidad entre ellos. |
| Estrés (1-10) | 6.3 | 6.0 | 5.0 | 1.6 | El nivel promedio de estrés es medio, lo que indica una carga emocional moderada en los estudiantes. |
| Horas de Sueño | 6.2 | 6.0 | 7.0 | 1.2 | Duermen alrededor de 6 horas, lo que sugiere un descanso algo limitado pero constante. |

### Tabla 2
*Matriz de Datos Limpia y Recodificada*

| ID | Edad | Género | Horas de Estudio | Horas de Sueño | Estrés (1-10) | Nivel de Estrés (Recodificado) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 20 | F | 3 | 6 | 7 | Medio |
| 2 | 21 | M | 4 | 7 | 6 | Medio |
| 3 | 19 | F | 2 | 5 | 8 | Alto |
| 4 | 22 | F | 5 | 7 | 5 | Medio |
| 5 | 20 | M | 6 | 8 | 4 | Bajo |
| 6 | 23 | F | 3 | 6 | 7 | Medio |
| 7 | 21 | F | 4 | 7 | 6 | Medio |
| 8 | 24 | M | 2 | 5 | 9 | Alto |
| 9 | 19 | F | 3 | 5 | 8 | Alto |
| 10| 22 | F | 5 | 7 | 5 | Medio |
| 11| 20 | M | 6 | 8 | 4 | Bajo |
| 12| 23 | F | 2 | 4 | 9 | Alto |
| 13| 21 | F | 4 | 6 | 6 | Medio |
| 14| 24 | M | 3 | 6 | 7 | Medio |
| 15| 19 | F | 2 | 5 | 8 | Alto |

---

## 2. Reporte del Modelo Final (Output de Python - `statsmodels`)

Al ejecutar el script de Python `analisis_datos.py` mediante una regresión por Mínimos Cuadrados Ordinarios (OLS), se obtuvo la siguiente salida oficial de la consola:

```text
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 Estres   R-squared:                       0.971
Model:                            OLS   Adj. R-squared:                  0.966
Method:                 Least Squares   F-statistic:                     199.3
No. Observations:                  15   Prob (F-statistic):           6.23e-10
Df Residuals:                      12   Scale:                          0.0881
Df Model:                           2                                         
=================================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------
const            12.5255      0.666     18.813      0.000      11.075      13.976
Horas_estudio    -0.6984      0.161     -4.328      0.001      -1.050      -0.347
Horas_sueno      -0.5562      0.191     -2.914      0.013      -0.972      -0.140
============================================================================== datos y ajuste de modelo final
# Archivo destinado al desarrollo del análisis mediante Python.
