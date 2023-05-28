# Studious v1.00
A simple Python study program initially written as a prepatory tool for the CompTIA Security+ Certification.

## Installation:
```
git clone https://github.com/SentinalMax/Studious.git
```
```
cd Studious
```
```
chmod +x studious.py
```
---
## **ADD** Mode
### To *enable* 'ADD Mode' simply type 'add' after running the following:
```
python studious.py OR python3 studious.py
```
### You'll then want to follow the prompts and input your **question**, the number of possible **answers**, type / paste each answer, and select the **correct** answer so the program knows how to grade your performance.
---

## **STUDY** Mode
### Same steps as above except you'll want to type '**study**' instead of 'add'.
- You will then be prompted with the questions that you've input.
- If you'd like you can **clear** any questions by deleting everything between the `"problems": []` braces.
```
{
    "problems": [
        <DELETE ANYTHING IN HERE>
    ]
}
```
- Be **SURE** you have no syntactical errors in the *.JSON* file. 
