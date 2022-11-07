'''Separating TEMPLATE from the code that uses TEMPLATE.'''

from jinja2 import Template


forbes_data=[{"Name":"Raghuram G Rajan","Domain":"Economic Policy","Country":"India"}, {"Name":"Raj Chetty","Domain":"Data & Policy","Country":"USA"},
             {"Name":"Rishi Sunak","Domain":"Politics","Country":"Britain"}, {"Name":"Chinmay Tumbe","Domain":"Social Policy","Country":"India"},
             {"Name":"Sundar Pichai","Domain":"Technology","Country":"USA"}]


def main():
  my_file1=open("template.jinja.html")
  TEMPLATE=my_file1.read()
  my_file1.close()
  
  template=Template(TEMPLATE)
  content=template.render(forbes_data=forbes_data)
  
  my_file=open("forbes.html",'w')
  my_file.write(content)
  my_file.close()
  
if __name__=="__main__":
     main()
