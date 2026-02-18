import os
from crewai import Agent, Task, Crew, Process

# Configuración del Agente Investigador
# Especializado en metrología y análisis de latencia según el protocolo de Veracidad Estricta.
investigador = Agent(
    role='Analista de Frecuencias',
    goal='Monitorear la resolución del reloj del entorno y analizar desviaciones.',
    backstory='Ingeniero de Frecuencias encargado de transformar el caos en estructura lógica.',
    verbose=True,
    allow_delegation=False
)

# Definición de la Tarea
# Se busca validar la resolución del reloj del sistema con un objetivo de 384ns.
tarea_analisis = Task(
    description='Validar la resolución del reloj del entorno actual. Comparar con el objetivo de 384ns.',
    agent=investigador,
    expected_output='Informe técnico detallado en formato markdown sobre la estabilidad de frecuencia y latencia detectada.',
    output_file='reporte_frecuencias.md'
)

# Formación del Crew (Nodo)
nodo_soberano = Crew(
    agents=[investigador],
    tasks=[tarea_analisis],
    process=Process.sequential
)

if __name__ == "__main__":
    print("Iniciando ejecución del Nodo Soberano...")
    nodo_soberano.start()