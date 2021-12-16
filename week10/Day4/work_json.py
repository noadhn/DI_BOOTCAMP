import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

sample_py = json.loads(sampleJson)
salary = sample_py['company']['employee']['payable']['salary']
sample_py['company']['employee']['birth_date'] = ''
print(salary)
print(sample_py['company'])

with open('sample.json', "w") as json_sample:
    json.dump(sample_py, json_sample, indent=2)


