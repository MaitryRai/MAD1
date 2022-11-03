program1:

TEMPLATE="""Hello World! This is {name}."""
def main():
    print(TEMPLATE.format(name="Maitry"))
if __name__=="__main__":
    main()
    

program2:

TEMPLATE="""This is {p:+} and this is {n:+}"""
def main():
  print(TEMPLATE.format(p=5,n=-7))
if __name__=="__main__":
    main()
