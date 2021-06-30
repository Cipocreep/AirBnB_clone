# AirBnB clone console project

## Description

This is the first step towards building the AirBnB clone, it uses a simple flow of serialization/deserialization to store data using File storage. This was entirely written in Python for a project for Holberton School.

## Usage

First step, clone this repository in order to obtain all the files in your local machine.

```bash
git clone https://github.com/OctaveC/AirBnB_clone
```

This program is used through a shell. You can run it in interactive mode, where you can exit using Ctrl+D or typing exit, and in non-interactive mode, which will exit right after the execution of the command.

```bash
./console.py
```
For non-interactive mode :
```bash
echo "help" | ./console.py
```

## Functional commands

- **create:** "create <class>" Creates a new instance of one of the available classes, which are BaseModel, User, City, State, Anemity, Place, and Review.
- **destroy:** "destroy <class> <instance id>" Deletes an instance of a class.
- **update:** "update <class> <instance id> <attribute name> <attribute value>" Updates the attributes of an instance of a class.
- **show:** "show <class> <instance id>" Prints the attributes of an instance of a class.
- **all:** "all <class>" Prints all instances of a class.
- **help:** "help <command>" displays information about one of the availables commands.
- **EOF:** (Ctrl + D) Exits the program.
- **quit:** Exits the program.

## Authors

[COLLOMBEL Octave](https://github.com/OctaveC)
