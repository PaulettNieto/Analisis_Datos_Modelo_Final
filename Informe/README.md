# Análisis de Estrés Académico

Este apartado contiene la documentación detallada del proceso desarrollado, la metodología aplicada y los resultados del modelo estadístico final para el proyecto sobre hábitos de estudio, descanso y nivel de estrés en estudiantes de psicología.

---

## 1. Metodología Aplicada y Proceso Desarrollado

### Recolección y Limpieza de Datos
* **Muestra:** Se trabajó con una base de datos de 15 estudiantes de la carrera de Psicología (Ciclo IV) de la Universidad Privada San Juan Bautista.
* **Depuración:** Se realizó un proceso de control de calidad en Excel para asegurar la integridad de la información, verificando la ausencia de valores faltantes (missings), errores de registro o datos inconsistentes.
* **Recodificación de Variables:** La variable original de estrés (medida en una escala numérica continua del 1 al 10) fue recodificada en una variable categórica para facilitar su interpretación en tres niveles jerárquicos: Bajo (1-4), Medio (5-7) y Alto (8-10).

---

## 2. Análisis Estadísticos Realizados

### Análisis Descriptivo (Tendencia Central)
El procesamiento descriptivo de la muestra arrojó las siguientes métricas clave:
* **Edad:** Promedio de 21.3 años (Desv. Est. = 1.7), evidenciando un grupo joven y homogéneo.
* **Hábitos de Estudio:** Promedio de 3.8 horas diarias de estudio independiente.
* **Hábitos de Descanso:** Promedio de 6.2 horas de sueño diarias.
* **Estrés Percibido:** Promedio general de 6.3 puntos, ubicando a la mayor parte de la muestra en un nivel de estrés moderado o medio.

### Ajuste del Modelo Final (Análisis Inferencial)
Para ir más allá de la descripción básica, se aplicó un **Modelo de Regresión Lineal Múltiple**. Este modelo estadístico permite evaluar matemáticamente cómo las variables predictoras (Horas de Sueño y Horas de Estudio) impactan directamente sobre la variable dependiente (Nivel de Estrés).

---

## 3. Interpretación de los Resultados Obtenidos

Los hallazgos del modelo final demostraron lo siguiente:

1. **El impacto crítico del descanso:** Se identificó una relación inversa y estadísticamente significativa ($p < 0.05$) entre las horas de sueño y el estrés. A nivel matemático, por cada hora extra de sueño biológico que el estudiante logra recuperar, el nivel de estrés disminuye notablemente. Los estudiantes en el rango crítico de estrés Alto (8-9 puntos) coinciden de manera sistemática con un descanso inferior a las 5 horas diarias.
2. **El rol del estudio:** Las horas de estudio independiente mostraron funcionar como un factor protector moderado, sugiriendo que una distribución organizada del tiempo de estudio mitiga la acumulación de carga emocional en comparación con aquellos que estudian de forma desorganizada.
3. **Conclusión del análisis:** Los resultados confirman que el agotamiento y el estrés en la vida universitaria no dependen únicamente de la exigencia académica en sí, sino de la privación de descanso físico, lo que resalta la urgencia de aplicar estrategias de autocuidado y manejo del tiempo en la formación de los futuros profesionales de la salud mental.
