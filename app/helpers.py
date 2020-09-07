def sequencer():  
    # main setting
    separator = "-"
    serial_digits = 4
    # projects table
    prj = {}
    # main codec elements table for prj
    prj_fields = {
        "unit": 3,
        "doctype": 3,
        "matclass": 3
    }
    # any element has many sub elements

    # extra codec information table for prj
    # this options will be added to the matrix.
    prj_extra_fields = {
        "partner": 3,
        "mr": 0,
    }

    # matrix table
    matrix = {}

