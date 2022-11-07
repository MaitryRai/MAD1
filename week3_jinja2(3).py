'''We dynamically create HTML table by substituting more than one row in our TEMPLATE'''

from jinja2 import Template

forbes_data=[{"Name":"Raghuram G Rajan","Domain":"Economic Policy","Country":"India"},
             {"Name":"Raj Chetty","Domain":"Data & Policy","Country":"USA"},
             {"Name":"Rishi Sunak","Domain":"Politics","Country":"Britain"},
             {"Name":"Chinmay Tumbe","Domain":"Social Policy","Country":"India"}
            {"Name":"Sundar Pichai","Domain":"Technology","Country":"USA"}]

TEMPLATE='''
<!DOCTYPE html>
 <html>
 <head>
 <meta=charset="utf-8"/>
 <title>Forbes</title>
 </head>
 <body>
   <h1>People Of The Year</h1>
   <table>
    <thead>
       <tr>
         <th>Name</th>
         <th>Domain</th>
         <th>Country</th>
       </tr>
    </thead>
    <tbody>
       {% for person in forbes_data %}
       <tr>
         <td>person["Name"] </td>
         <td>person["Domain"] </td>
         <td>person["Country"]</td>
       </tr>
       {% endfor %}
    </tbody>
   </table>
 </body>
 </html>
''''

def main():
  template=Template(TEMPLATE)
  print(template.render(forbes_data=forbes_data))

if __name__=="__main__":
    main()
