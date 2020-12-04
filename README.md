# Julie-Julie README and LOG

!!!CRITICAL!!!
As of Dec 4 2020 the Vosk Aspire model no longer works.  Use the 1 GB Danzu model instead.
This model works with vosk==0.3.10
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

New Virtual Assistant with Elmo Model for Querying Downloaded Text.

I'm not sure that Elmo is the best choice for question answer.  It's slow.  I'm trying to find something much faster.  I'm looking into BERT right now.  11-21-20  

Wow!  I found a lot of errors.  This always happens when I test new documentation with a new build.  This is ongoing documentation.  If you have trouble.  Check back in a few days.  I may have fixed the instructuions by then.  As of 11-17-2020, this doc should work fine, but I will be making additions, as this repo is not done yet.  I update this as I work, but there are almost always errors.  I find them later when I put myself into reader mode and build this software using this documentation.  I'll post the date of each time I test the documentation.

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

I've been struggling a bit with gTTS.  I had thought that one needed to use an older version and sudo for the installation.  I've since changed my mind.  I can't tell you why I was having trouble with gTTS, but it's no longer the case.  I also read that one should never use sudo with pip, as you can over-write operating system packages.  Is this true?  I want to err on the side of safety.

pip3 install gTTS 

There are changes to pip's wrapper so add the --use-feature=2020-resolver switch until pip's programmers make all their changes -- at least that's what the pip wrapper currently spits out occcassionally when installing packages.

Then create a virtual environment:  

conda create --name Julie-Julie python=3.6.2


conda activate Julie-Julie


pip list


pip3 install gTTS 

pip list

This should take care of the packages necessary for text to speech (TTS).

Next is speech to text (STT):

Install the alphacep's vosk-api software from github.
The command is 
git clone https://github.com/alphacep/vosk-api

I always clone this package so I have the example files handy.  cd to where you store code.  I use ~/Code.  

Mkdir ~/Code 
cd ~/Code

for SSH use:

git clone git@github.com:alphacep/vosk-api.git  

Or for HTTPS use:

git clone https://github.com/alphacep/vosk-api.git

Documentation for vosk is on their website:  https://alphacephei.com/vosk/
Always read the documentation when installing a package.  Things change, and they may have updated their proceedures whil I may not have updated mine.

pip3 install vosk==0.3.10 

pip list

Now get and install the kaldi model used by vosk.  You can find it at 
https://alphacephei.com/vosk/models
Download the vosk-model-en-us-aspire-0.2 (this model is no longer working)
Download this instead and keep a copy somewhere off your system:  
https://alphacephei.com/vosk/models/vosk-model-en-us-daanzu-20200905.zip
This takes a long time.  It's a large model. On my system this goes into ~/downloads/

cd ~/Downloads
unzip vosk-model-en-us-daanzu-20200905.zip

mv ~/Downloads/vosk-model-en-us-daanzu-20200905
 ~/Code/Julie-Julie/

cd ~/Code/Julie-Julie
mv vosk-model-en-us-daanzu-20200905
 model/ 

Now install pyaudio:

conda install pyaudio    (use conda as pip usually fails. I'm not sure why.)

Let's test our vosk installation:

python ./test_microphone.py

Now install mpg123, and we are done with the foundations for TTS and STT.

sudo apt install mpg123

Add additional packages for modules:
pip install pyautogui --use-feature=2020-resolver
pip install wikipedia --use-feature=2020-resolver

To setup your music I make a folder called music at ~/Music.  Here's a path to a song:  /home/bard/Music/Music/SoundGarden/Unknown\ Album/Black\ Hole\ Sun.mp3

Music needs to be listed in the mymusiclist.txt file.
If you want/have music in another location, you will need to modify the mymusiclist.txt file to point to it.   The command "Julie-Julie play music" will play 3 songs.  This can be changed in the julie-julie.py file.  See below:

def main():
    # Initialize.
    myVars()
    playcounter = 1
    # This is where to set the number of songs
    # to play when you say "Julie play music."
    songs2play = 2


More to be done here . . .  Checked to this point on 11/17/2020

I'm going to clean up my code at this point.  I have a lot of code from other projects that I want to integrate in, but that code complicates the repo.  I'm going to move it into a research-storage-attic/ directory just to get it out of the way for now.  After I will start setting up and testing each action component.  For example, I need to put my music files into the correct path.   


Eventually, I'll be using this model:  https://www.youtube.com/watch?v=qJHDuYm8XGk&t=330s
