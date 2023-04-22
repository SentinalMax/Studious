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
chmod +x CompTIA-Prep.py
```
---
## **ADD** Mode
### To *enable* 'ADD Mode' simply type 'add' after running the following:
```
python CompTIA-Prep.py OR python3 CompTIA-Prep.py
```
### You'll then want to follow the prompts and input your **question**, the number of possible **answers**, type / paste each answer, and select the **correct** answer so the program knows how to grade your performance.
---

## **STUDY** Mode
### Same steps as above except you'll want to type '**study**' instead of 'add'.
- You will then be prompted with the questions that you've input as well as any questions in the *.JSON* file that might be left over from my studying.
- If you'd like you can **clear** any questions by deleting everything between the `"problems": []` braces.
```
{
    "problems": [
        <DELETE ANYTHING IN HERE>
    ]
}
```
- Be **SURE** you have no syntactical errors in the *.JSON* file. 
