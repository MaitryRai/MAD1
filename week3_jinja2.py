'''First Jinja2 program to generate html output for a given data'''

from jinja2 import Template

Forbes_data={"Name":"Raghuram G Rajan","Domain":"Economic Policy","Country":"India"}

TEMPLATE="""
<!DOCTYPE html>
<html>
<head>
   <meta charset="utf-8"/>
   <title>Forbes</title>
</head>
<body>
  <h1>Person Of The Year</h1>
  <table>
     <thead>
     <tr>
       <th>Name</th>
       <th>Domain</th>
       <th>Country</th>
      </tr>
     </thead>
     <tbody>
       <tr>
         <td>{{Forbes_data["Name"]}}</td>
         <td>{{Forbes_data["Domain"]}}</td>
         <td>{{Forbes_data["Country"]}}</td>
       </tr>
     </tbody>
  </table>
</body>
</html> """



def main():
  template=Template(TEMPLATE)
  print(template.render(Forbes_data=Forbes_data))

if __name__=="__main__":
  main()
