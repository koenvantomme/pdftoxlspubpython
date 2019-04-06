# https://pdftables.com/pdf-to-excel-api
import pdftables_api

# get yoour api key at https://pdftables.com/pdf-to-excel-api 
api_key= 'xxxxxx'

input = 'xxxx.pdf'
output= 'xxxx.xls'

c = pdftables_api.Client(api_key)
c.xlsx(input, output) 

#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML
