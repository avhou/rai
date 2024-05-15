import speech_recognition as sr
import assemblyai as aai
import os

def convert(file: str):
    print(f"reading audio file {file}")
    r = sr.Recognizer()
    audio_file = sr.AudioFile(file)
    print(f"audio file opened")
    with audio_file as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        print(f"recognizing text")
        text = r.recognize_sphinx(audio, language='en-US')
        print(text)

    with open(f"{file[:-4]}.txt", "w") as f:
        f.write(text)
    print("done")

def convert2(file: str):
    print(f"reading audio file {file}")
    aai.settings.api_key = os.environ['API_TOKEN']
    transcriber = aai.Transcriber()
    print(f"transcribing the file")
    transcript = transcriber.transcribe(file)
    print(transcript.text)
    with open(f"{file[:-4]}.txt", "w") as f:
        f.write(transcript.text)
    print("done")

if __name__ == "__main__":
    # convert("audio2.wav")
    convert2("non-scientific-before-audio-to-text/004-20201007-.mp3")
