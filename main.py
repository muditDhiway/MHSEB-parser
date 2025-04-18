from parser import parseHSC, parseSSC, parseHSC_New, parseSSC_New

if __name__ == "__main__":
    HscOrSsc = "SSC" # can be 'HSC' or 'SSC'
    input_file = "output/generated_entries_ssc.txt" 
    output_file_name = "generated_entries_ssc_new"  
    output_format = "csv" # can be 'json' or 'csv'

    if HscOrSsc == "HSC":
        # parseHSC(input_file, output_file_name, output_format)
        parseHSC_New(input_file, output_file_name, output_format)
    else:
        # parseSSC(input_file, output_file_name, output_format)
        parseSSC_New(input_file, output_file_name, output_format)
    