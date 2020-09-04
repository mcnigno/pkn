
from 


project_number = "A8RX"
entity = "TSC"
unit = ["001","002","003"]
doctype = ["PID", "SRN", "DWG"]
discipline = ["3NA", "4FG", "5DF"]
serial = "001"

t-e+w# A8RX-TSC-001-3NA-PID-001

matrix = {
    "A8RX-TSC-001-3NA-PID" : 1,
    "A8RX-TSC-002-3NA-DWG" : 1
}
# if the combination is in matrix add one to the counter and give me back the whole combination (matrix+counter)
# if not create a new one and set to 1 the counter

def askcode(project_number, entity, unit, doctype, discipline):
    base_data = "-".join([project_number, entity, unit, doctype, discipline])
    if base_data in matrix:
        print("ok")
        print(matrix[base_data])

        matrix[base_data] += 1
        code = base_data + "-" + str(matrix[base_data])
        print(code)


    else:
        print("it is not there")
        

askcode("A8RX", "TSC", "001", "3NA",  "PID")

