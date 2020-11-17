# Julie-Julie
New Virtual Assistant with Elmo Model for Querying Downloaded Text.

I'm building this from scratch on Pop!_OS 20.10, but I'm using code from my Juliet repository.  Ubuntu 20.10, 20.04, 18.* should also work fine -- as well as many other linuxes.

apt list

I use miniconda for virtual environments.  You will need this for pyaudio as pip can't install it.  Anaconda also works.  
Here's the 64 bit Linux installer you need.  It will download automatically: 
https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
Here's the link to miniconda documentation:
https://docs.conda.io/en/latest/miniconda.html

You don't need to know much about this to run the commands in my instructions, but you should understand that you are segregating python packages for this application by creating a virtual environment -- then activating it.  

INSTALLATION

There are a lot of tricky bits in here; so I don't recommend using pip install -r requirements.txt.  I include this file as a version record, however.  Check it against a pip list to find inconsistencies, if you are having trouble.  

Since I use gTTS as and operating system level utility.  You probably should too -- see my GoogSpeech Github repository. You must also, however, install gTTS in the virtual environment you create below.  Otherwise: import gtts (lower case once programming in python -- go figure) or your python programs will fail.  

Install gTTS in the base environment:

sudo pip3 install gTTS==1.2.2 

gTTS 2.0 sucks and causes latency problems.

There are changes to pip's wrapper so add the --use-feature=2020-resolver switch until pip's programmers make all their changes.

Then create a virtual environment:  

conda create --name Julie-Julie python=3.6.2


conda activate Julie-Julie


pip list


sudo pip3 install gTTS==1.2.2 --use-feature=2020-resolver
pip list

This should take care of the packages necessary for text to speech (TTS).

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

Start doing customization:

Get the python you are using in your virtual environment:
which python

Here's what I get.  

/home/bard/miniconda3/envs/Julie-Julie/bin/python

Put this into the startJulie-Julie.sh

/home/bard/miniconda3/envs/Julie-Julie/bin/python /home/bard/Code/Julie-Julie

Add additional packages for modules:
pip install pyautogui --use-feature=2020-resolver
pip install wikipedia --use-feature=2020-resolver




Eventually, I'll be using this model:  https://www.youtube.com/watch?v=qJHDuYm8XGk&t=330s
