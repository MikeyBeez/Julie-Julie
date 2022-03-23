# Julie-Julie LOG

June 5, 2021:  There have been quite a few hurdles to cross over the past few months.  I have been struggling with my unusual equipment, especially my Nvidia Tesla k-80.  At last I have gotten my computer systems working together.  I hope to have a number of microservices running.  To that end, I have been studying Docker.  



Feb 12, 2021:  It's been a while since I've made changes here.  That's because I've been searching for the right model to use.  I've been studying Facebook's Parlai pipeline for language tasks. So far the Wizard of Wikipedia seems the most helpful, but I think I want something that will download text and analyze it.   For now, there are no new changes.

Jan 7, 2021:  I added some code to Juliebrain, including a function definition called netcat.  This code is used for a socket connection.  There is also a new chat action that communicates with Huggingface's transfer-learning-conv-ai.  Of course the code for transfer-learning-conv-ai needed to be changed to accept the socket connection.  I'm including the modified file in this repo.  The file is called interact.py.  I'm commenting all the changes.  
Dec 20, 2020.  I realized that My installation instructions are incomplete.  I haven't included cloning the repository, and although people should know how to de this, I feel I should give instructions for completeness' sake.  I've added them below.


Dec 5, 2020 I made the mistake of saving a tar file of the model.  The mdel changed along with the software, so I had the wrong version of the model.  Aspire works fine.


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

INSTALLATION:

First fork the repository.  There is a button on the top right of the github page to do this.  Once that's done, the ownership should change to your github account name on the top left.  Then press the code button.  Choose https if you haven't already set up ssh.  Choose ssh if you have set it up.  Or setup ssh (recommended.)  Press the clipboard to copy the url to your clipboard.  Now open a terminal and run git clone <paste your clipboard here>  That's usually ctrl shift v.

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
Download the vosk-model-en-us-aspire-0.2 
or Download this instead:  
https://alphacephei.com/vosk/models/vosk-model-en-us-daanzu-20200905.zip
This takes a long time.  It's a large model. On my system this goes into ~/downloads/

cd ~/Downloads
uzip vosk-model-en-us-aspire-0.2
or
unzip vosk-model-en-us-daanzu-20200905.zip

mv ~/Downloads/vosk-model-en-us-aspire-0.2
 ~/Code/Julie-Julie/

or

mv ~/Downloads/vosk-model-en-us-daanzu-20200905
 ~/Code/Julie-Julie/

cd ~/Code/Julie-Julie

mv vosk-model-en-us-aspire-0.2
  model/

or 

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
