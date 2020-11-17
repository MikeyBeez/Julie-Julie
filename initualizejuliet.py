import os

##############################################################
# Check Model.


def CheckMyModel():
    if not os.path.exists("model"):
        print("Please download the model from https://github.com/alphacep/kaldi-android-demo/releases")
        print("and unpack as 'model' in the current folder.")
        exit(1)
##############################################################
# End Check Model.
