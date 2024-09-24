##phi3 Model Query  

#Introduction

This program allows you to read a prompt from a seperate text file, pass them to the phi3 model and store the model's answers in another seperate file.

#Needed 
01. Phi3 - You must have Olllama installed, which allows you to run phi3, locally.
    *To install Olllama, follow the instructions in their official website (https://ollama.com)
    *Download phi3 through Ollama

02. Python - Ensure you have Pythhon installed in your machine.

#Steps
01. Make sure that all the files are in your working directory.
02. 'prompts.txt' should have the prompts line by line.
03. 'responses.txt' should be a blank text file for the model to output answers into.

#To run the program enter the following command into the terminal
python3 phi3_query.py

#List of files,
01.Phi3_query.py       //main script
02.prompts.txt         //contains prompts
03.responses.txt       //outputs responses
04.README.md           //instructions
05.requirements.yaml   //environment