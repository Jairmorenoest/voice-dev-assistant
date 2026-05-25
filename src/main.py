import asyncio

async def record_audio():
    print("🎤 Grabando audio...")
    await asyncio.sleep(2)
    return "audio_data"

async def speech_to_text(audio):
    print("🔍 Convirtiendo voz a texto...")
    await asyncio.sleep(1)
    return "Hola, ¿cómo estás?"

async def call_llm(text):
    print("🧠 Procesando respuesta con LLM...")
    await asyncio.sleep(1)
    return "Estoy bien, ¿en qué puedo ayudarte?"

async def text_to_speech(response):
    print("🔊 Convirtiendo respuesta a voz...")
    await asyncio.sleep(1)

async def main_loop():
    while True:
        print("\n🎙️ Esperando interacción del usuario...\n")

        audio = await record_audio()

        text = await speech_to_text(audio)
        print(f"👤 Usuario: {text}")

        response = await call_llm(text)
        print(f"🤖 Asistente: {response}")

        await text_to_speech(response)

if __name__ == "__main__":
    asyncio.run(main_loop())