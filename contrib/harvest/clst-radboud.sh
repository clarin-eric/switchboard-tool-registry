#!/bin/bash

# Script to automatically harvest switchboard registry entries from CLAM webservices/webapps hosted by the
# Centre of Language and Speech Technology, Radboud University Nijmegen


ROOT=$(git rev-parse --show-toplevel)

cd $ROOT/contrib/harvest

if [ ! -d clst-radboud-env ]; then
    echo "Creating virtual environment..."
    virtualenv --python=python3 clst-radboud-env
fi


#activate the virtual environment
source clst-radboud-env/bin/activate

#install the software  (no-op if already installed/up to date)
pip install --no-cache-dir -U git+https://github.com/proycon/clam2switchboard.git

cd $ROOT/tools

clam2switchboard --ignore --url https://webservices.cls.ru.nl/frog -l nld --task "NLP suite for Dutch" #I don't like this task's title, Frog supports multiple tasks (see https://github.com/clarin-eric/switchboard/issues/67 and https://github.com/clarin-eric/switchboard-tool-registry/issues/5)
clam2switchboard --ignore --url https://webservices.cls.ru.nl/ucto --logo clst.png --task "Tokenisation"
clam2switchboard --ignore --url https://webservices.cls.ru.nl/piereling --task "Data Conversion"
clam2switchboard --ignore --url https://webservices.cls.ru.nl/alpino -l nld --task "Dependency Parsing"
clam2switchboard --ignore --url https://webservices.cls.ru.nl/colibricore --task "N-Gramming"
clam2switchboard --ignore --url https://webservices.cls.ru.nl/eng_ASR -l eng --logo clst.png --task "Speech Recognition"
clam2switchboard --ignore --url https://webservices.cls.ru.nl/oralhistory -l nld --logo clst.png --task "Speech Recognition"
clam2switchboard --ignore --url https://webservices.cls.ru.nl/spreek2schrijf -l nld --logo clst.png --task "Speech Recognition"
clam2switchboard --ignore --url https://webservices.cls.ru.nl/forcedalignment2 -l nld --logo clst.png --task "Speech Recognition"
clam2switchboard --ignore --url https://webservices.cls.ru.nl/glem -l grc --logo clst.png --task "Lemmatization"
clam2switchboard --ignore --url https://webservices.cls.ru.nl/g2pservice  --logo clst.png --task "Grapheme to Phoneme Conversion"
clam2switchboard --ignore --url https://webservices.cls.ru.nl/t2t -l rus,ukr,ara  --logo clst.png --task "Transliteration"
clam2switchboard --ignore --url https://webservices.cls.ru.nl/valkuil -l nld --task "Spelling correction"
clam2switchboard --ignore --url https://webservices.cls.ru.nl/tscan -l nld --logo clst.png --task "Text Analytics"
clam2switchboard --ignore --url https://webservices.cls.ru.nl/piccl --langparam lang --logo clst.png --task "Text Normalisation" #not enough, needs multiple tasks








