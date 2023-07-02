from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import os
import shutil

# download and load all models
preload_models()

prompt_array = [
""" 
    Hello, my name is Clive. And, uh and I like pizza. [laughs] But I also have other interests such as playing tic tac toe.
""",
""" 
    um What else - [laughs] I also like solving rubix cubes. it um - makes me very happy. 
""" ,
""" 
    What else can I add hmmm - I guess thats all. [laughs] This was fun. 
""" 
]

new_folder_index=1
combined_folder_name=f"new-voices-{new_folder_index}"
os.mkdir(combined_folder_name)
currentPath=os.getcwd()
newDestination=f"{currentPath}/{combined_folder_name}"


index = 0
while index < len(prompt_array):
    print(f"loop = {index}")

    filename=f"{index}-audio.wav"
    sourcePath = f"{currentPath}/{filename}"
    destinationPath = f"{newDestination}/{filename}"

    audio_array = generate_audio(prompt_array[index], history_prompt="en_speaker_9")
    write_wav(filename, SAMPLE_RATE, audio_array)
    if os.path.isfile(sourcePath):
        shutil.copy(sourcePath, destinationPath)
        os.remove(sourcePath)
    index += 1
