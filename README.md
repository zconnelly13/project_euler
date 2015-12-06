Project Euler Solutions
=============

![Build Status](https://travis-ci.org/zconnelly13/project_euler.svg?branch=master)

Solutions to some of the problems found here, https://projecteuler.net/ in python!

### Setup

Install virtualenv

```
pip install virtualenv
```

Create a new virtualenv, activate it, and install requirements

```
virtualenv venv
source venv/bin/activate
pip install -r setup/requirements.txt
```

### Running the Code

To "solve" a problem run

```
python problem_*.py
```

Where * is the number of the problem

### Tests

To test that all of the problem.py files still work, run

```
python test.py
```

this is necessary because some of the problem share code
particularly in `tools/`

This takes a while as some of the scripts take longer to run than others
