#modulo speek-to-Text.
import whisper

model = whisper.load_model("base")
result = model.transcribe("mp3/voice.mp3")
print(result["text"])
