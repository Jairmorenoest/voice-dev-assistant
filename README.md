# VoiceDev Assistant 🎙️

## Descripción
VoiceDev Assistant es un agente de voz conversacional desarrollado en Python utilizando asyncio. Su objetivo es entender la arquitectura interna de sistemas de voz en tiempo real sin depender de frameworks complejos.

## Flujo del Sistema
Micrófono → Speech-to-Text → LLM → Text-to-Speech → Altavoz

## Tecnologías
- Python
- asyncio
- APIs de IA (STT, TTS, LLM)

## Cómo ejecutar el proyecto

1. Clonar repositorio:
git clone https://github.com/Jairmorenoest/voice-dev-assistant.git

2. Instalar dependencias:
pip install -r requirements.txt

3. Ejecutar:
python src/main.py

## Flujo de trabajo con Claude Code

Este proyecto sigue el enfoque descrito en el artículo "Running Your AFK Agent":

- Claude Code se utiliza para generar código
- Se crean issues antes de implementar
- Desarrollo iterativo basado en tareas
- Código modular desde el inicio

## Estado del Proyecto
🚧 En desarrollo (fase inicial)

## Autor
Jair Moreno