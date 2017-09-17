def search_employees(emps, child_age):
  employees = []
  for employee in emps:
      for child in employee["children"]:
          if child["age"] > 18:
              employees.append(employee["name"])
  return employees


def main():
    ivan = {
        "name": "ivan",
        "age": 34,
        "children": [{
            "name": "vasja",
            "age": 12,
        }, {
            "name": "petja",
            "age": 10,
        }],
    }
    darja = {
        "name": "darja",
        "age": 41,
        "children": [{
            "name": "kirill",
            "age": 21,
        }, {
            "name": "pavel",
            "age": 15,
        }],
    }
    emps1 = [ivan, darja]
    child_age1 = 18

    print(search_employees(emps1, child_age1))


main()
