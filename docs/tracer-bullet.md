# Sección 1: La Bala Trazadora y el Enrutamiento de las Skills

## Introducción

Durante las etapas iniciales del proyecto se buscó minimizar los riesgos técnicos asociados al desarrollo de un sistema conversacional de voz.

Antes de implementar funcionalidades complejas se realizó un análisis del problema con el objetivo de comprender los componentes principales y sus dependencias.

---

## Refinamiento del Problema

Inicialmente el sistema fue concebido como un único proceso encargado de manejar todas las operaciones.

Sin embargo, durante la fase de análisis se identificaron cuatro responsabilidades claramente diferenciadas:

- Captura de audio
- Conversión de voz a texto (Speech-to-Text)
- Procesamiento mediante un modelo de lenguaje (LLM)
- Conversión de texto a voz (Text-to-Speech)

La separación temprana de estas responsabilidades permitió definir una arquitectura más organizada y escalable.

---

## Aplicación de la Estrategia de Bala Trazadora

Siguiendo el concepto de Tracer Bullet descrito durante el curso, se decidió implementar primero un flujo funcional simplificado de extremo a extremo.

El objetivo no era desarrollar todas las integraciones reales desde el principio, sino validar que la arquitectura general pudiera soportar correctamente la comunicación entre componentes.

El flujo inicial fue:

Micrófono → Speech-to-Text → LLM → Text-to-Speech → Altavoz

Todos los módulos fueron simulados inicialmente mediante funciones asíncronas.

---

## Resultados Obtenidos

La implementación temprana permitió validar:

- El flujo general del sistema.
- La viabilidad de asyncio como mecanismo de orquestación.
- La comunicación entre módulos.
- La estructura base del proyecto.

Gracias a esta estrategia fue posible obtener retroalimentación temprana y reducir significativamente el riesgo de errores arquitectónicos en etapas posteriores.