# 🔐 Password Generator

A simple Python-based password generator that creates random passwords based on the length provided by the user.

## 📌 Features

* Generates passwords of any user-defined length
* Uses uppercase and lowercase letters
* Includes numbers
* Includes special characters
* Simple command-line interface
* Built using Python's built-in modules

## 🛠️ Technologies Used

* Python
* `random`
* `string`

## 📂 Project Structure

```text
Password_Manager/
│
├── password_generator.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Password_Manager.git
```

### 2. Open the project folder

```bash
cd Password_Manager
```

### 3. Run the program

```bash
python password_generator.py
```

## 💻 Example

```text
Enter Your Password Length : 12

Password : aB7@kP2#xQ9!
```

## 🧠 How It Works

The program combines:

* Letters using `string.ascii_letters`
* Numbers using `string.digits`
* Special characters using `string.punctuation`

It then randomly selects characters from the combined character set until the requested password length is reached.

## 📚 What I Learned

This project helped me practice:

* Python modules
* String manipulation
* User input
* Loops
* Random character selection
* Basic project structure
* Git & GitHub

## ⚠️ Note

This project is created for Python learning and practice purposes. The current version uses Python's `random` module and should not be considered suitable for generating passwords for highly sensitive or security-critical applications.

## 👨‍💻 Author

Aman
