# Sección 2: Anatomía de la Complejidad

## Introducción

Para evaluar la calidad del software desarrollado se utilizaron los conceptos presentados por John Ousterhout en el libro *A Philosophy of Software Design*.

Los principales conceptos analizados fueron:

- Deep Modules
- Shallow Modules
- Information Leakage

---

# Módulos Profundos (Deep Modules)

Un módulo profundo es aquel que proporciona una interfaz simple mientras oculta una cantidad considerable de complejidad interna.

Dentro del proyecto VoiceDev Assistant, el principal candidato a módulo profundo es el orquestador asíncrono.

La función principal coordina:

- Captura de audio
- Conversión de voz a texto
- Procesamiento mediante IA
- Conversión de texto a voz

A pesar de la cantidad de tareas realizadas, la interfaz de uso permanece simple y comprensible.

---

# Módulos Superficiales (Shallow Modules)

Durante el desarrollo surgió el riesgo de fragmentar excesivamente el sistema en múltiples archivos con muy poca funcionalidad.

Este enfoque habría generado:

- Mayor complejidad accidental
- Dependencias innecesarias
- Dificultad para mantener el sistema

Para evitar este problema se decidió consolidar responsabilidades relacionadas dentro de módulos más significativos.

---

# Information Leakage

La fuga de información ocurre cuando detalles internos de implementación se exponen innecesariamente a otros componentes del sistema.

Durante el proyecto se identificó el riesgo de exponer directamente detalles de futuras APIs externas a los módulos superiores.

Para evitarlo se adoptó una estrategia de separación entre:

- Capa de interfaz
- Servicios de negocio
- Integraciones externas

Esta decisión permite reemplazar proveedores externos sin afectar el resto del sistema.

---

# Conclusiones

La arquitectura actual mantiene un nivel aceptable de modularidad y ocultamiento de información.

Aunque el proyecto aún puede evolucionar hacia módulos más profundos, las decisiones adoptadas reducen significativamente la complejidad futura.