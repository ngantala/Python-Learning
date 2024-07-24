route53_record = [
  {
  "name": "x.example.com",
  "type": "TXT",
  "value": "yah00=12133ldkldjd"
  },
  {
  "name": "y.example.com",
  "type": "TXT",
  "value": "yahoo=23313213"
  }
]
print(route53_record[0]["value"])

