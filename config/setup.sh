#!/usr/bin/sh

# Testado em: 4.9.50-1-MANJARO

cd ../utils/
python concat.py
cd ..
python app.py
