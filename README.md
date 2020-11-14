# Julie-Julie
New Virtual Assistant with Elmo Model for Querying Downloaded Text.

I'm building this from scratch on Pop!_OS 20.10, but I'm using code from my Juliet repository.

INSTALLATION

Since I use gTTS as and operating system level utility.  You probably should too -- see my GoogSpeech Github repository. You must also, however, install gTTS in the virtual environment you create below.  Otherwise import gTTS in your python program will fail.  

Install gTTS in the base environment:

pip install gTTS

Then create a virtual environment:  

conda create --name Julie-Julie python=3.6.2
conda activate Julie-Julie
pip list

Here's what I'm seeing:


Package    Version
---------- -------------------
certifi    2020.6.20
pip        20.2.4
setuptools 50.3.1.post20201107
wheel      0.35.1

