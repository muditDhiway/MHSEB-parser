from parser import parseHSC, parseSSC, parseHSC_New, parseSSC_New

if __name__ == "__main__":
    HscOrSsc = "HSC" # can be 'HSC' or 'SSC'
    input_file = "inputDocs/demo" 
    output_file_name = "demo"  
    output_format = "json" # can be 'json' or 'csv'

    if HscOrSsc == "HSC":
        # parseHSC(input_file, output_file_name, output_format)
        parseHSC_New(input_file, output_file_name, output_format)
    else:
        # parseSSC(input_file, output_file_name, output_format)
        parseSSC_New(input_file, output_file_name, output_format)
    