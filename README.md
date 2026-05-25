# VoiceDev Assistant 🎙️

## Descripción del Proyecto

VoiceDev Assistant es un proyecto académico orientado al desarrollo de un agente de voz conversacional utilizando Python puro y programación asíncrona con asyncio.

El objetivo principal es comprender profundamente la arquitectura interna de sistemas de voz en tiempo real similares a frameworks modernos como Pipecat y LiveKit Agents.

---

## Flujo del Sistema

Micrófono → Speech-to-Text → LLM → Text-to-Speech → Altavoz

---

## Tecnologías Utilizadas

- Python
- asyncio
- OpenAI API
- PyAudio
- python-dotenv

---

## Estructura del Proyecto

```bash
src/
├── audio/
├── stt/
├── tts/
├── llm/
└── main.py
```

---

## Ejecución del Proyecto

### 1. Clonar repositorio

```bash
git clone https://github.com/Jairmorenoest/voice-dev-assistant.git
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar aplicación

```bash
python src/main.py
```

---

## Flujo Arquitectónico y Ralph Loops

Este proyecto implementa un flujo de desarrollo inspirado en Claude Code y Ralph Loops.

### Prácticas aplicadas

- Desarrollo basado en Issues
- Commits iterativos vinculados a tickets
- Revisiones arquitectónicas intermedias
- Gestión de contexto mediante handoffs
- Arquitectura modular asíncrona
- Control humano de calidad sobre código generado autónomamente

---

## Estado Actual

🚧 Proyecto en desarrollo (fase intermedia)

### Funcionalidades actuales

- Simulación de captura de audio
- Simulación Speech-to-Text
- Flujo asincrónico inicial
- Simulación de respuestas LLM
- Simulación Text-to-Speech

---

## Próximas Mejoras

- Integración real con Whisper/OpenAI
- Captura de micrófono en tiempo real
- Implementación real de TTS
- Reproducción automática de audio
- Dashboard frontend para monitoreo

---

## Autor

Jair Moreno