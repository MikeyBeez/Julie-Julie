# Julie-Julie
New Virtual Assistant with Elmo Model for Querying Downloaded Text.

I'm building this from scratch on Pop!_OS 20.10, but I'm using code from my Juliet repository.  Ubuntu 20.10, 20.04, 18.* should also work fine -- as well as many other linuxes.apt list

INSTALLATION

Since I use gTTS as and operating system level utility.  You probably should too -- see my GoogSpeech Github repository. You must also, however, install gTTS in the virtual environment you create below.  Otherwise: import gtts (lower case once programming in python -- go figure) or your python programs will fail.  

Install gTTS in the base environment:

pip install gTTS --use-feature=2020-resolver

There are changes to pip's wrapper so add the --use-feature=2020-resolver switch until pip's programmers make all their changes.

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

pip install gTTS --use-feature=2020-resolver
pip list

OUTPUT:
Package        Version
-------------- -------------------
beautifulsoup4 4.9.3
certifi        2020.6.20
chardet        3.0.4
click          7.1.2
gTTS           2.1.2
gTTS-token     1.1.4
idna           2.10
pip            20.2.4
requests       2.25.0
setuptools     50.3.1.post20201107
six            1.15.0
soupsieve      2.0.1
urllib3        1.26.2
wheel          0.35.1

This should take care of the packagee necessary for text to speech (TTS).

Next is speech to text (STT):

Install the alphacep's vosk-api software from github.
The URL is https://github.com/alphacep/vosk-api
I always clone this package so I have the example files handy.  cd to where you store code.  I use ~/Code.  

Mkdir ~/Code 
cd ~/Code

for SSH use:

git clone git@github.com:alphacep/vosk-api.git  

Or for HTTPS use:

git clone https://github.com/alphacep/vosk-api.git

Documentation for vosk is on their website:  https://alphacephei.com/vosk/
Always read the documentation when installing a package.  Things change, and they may have updated their proceedures whil I may not have updated mine.

pip3 install vosk --use-feature=2020-resolver
pip list

OUTPUT:
Package        Version
-------------- -------------------
beautifulsoup4 4.9.3
certifi        2020.6.20
chardet        3.0.4
click          7.1.2
gTTS           2.1.2
gTTS-token     1.1.4
idna           2.10
pip            20.2.4
requests       2.25.0
setuptools     50.3.1.post20201107
six            1.15.0
soupsieve      2.0.1
urllib3        1.26.2
vosk           0.3.15
wheel          0.35.1

Now get and install the kaldi model used by vosk.  You can find it at 
https://alphacephei.com/vosk/models
Download the vosk-model-en-us-aspire-0.2
This takes a long time.  It's a large model. On my system this goes into ~/downloads/

cd ~/Code
mkdir Julie-Julie
cd Julie-Julie
mkdir models

unzip the model and move it to the models directory:

unzip vosk-model-en-us-aspire-0.2.zip

You will now have a vosk-model-en-us-aspire-0.2 directory.  
Move it into your models directory:

mv ~/Downloads/vosk-model-en-us-aspire-0.2 ~/Code/Julie-Julie/model
cd ~/Code/Julie-Julie/

Now install pyaudio:

conda install pyaudio    (use conda as pip usually fails. I'm not sure why.)

Let's test our vosk installation:

cp ~/Code/vosk-api/python/example/test_microphone.py .

Now install mpg123, and we are done with the foundations for TTS and STT.

sudo apt install mpg123



