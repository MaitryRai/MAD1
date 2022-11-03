"""Jinja2 is an external library, not built into python3. So, we install it.
To install:
Step1: Create a virtual environment : python3 -m venv .filename-env (in the terminal)
step2: Activating the virtual environment : Source .filename-env/bin/activate
step3: Installing jinja2 : pip3 install jinja2
step4: pip freeze>requirements.txt """

//The first program using jinja

from jinja2 import Template
TEMPLATE="""Hello there, this is {{name}} here!"""

def main():
  template=Template(TEMPLATE)
  print(template.render(name="Maitry"))
