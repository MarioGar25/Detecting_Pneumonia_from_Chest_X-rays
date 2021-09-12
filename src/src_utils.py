import os

def descompress_data(zip, file = None, folder = None):
    '''
    This function descompress a .csv file. And drop de .zip
    Input: File .zip
    Output: File.csv (.zip deleted)

        Params
    -----------------------------------------
        zip --> File .zip
        folder --> Target folder 
    '''
    #take csv.file name
    csv_file = zip.split(".")[0]

    #descompress .zip
    descompress_zip = f"unzip {zip}"
    print("Descompressing files")
    
    #remove .zip 
    remove_zip = f"rm -rf {zip}"
    print ("removing .zip")

    #realize before actions
    for i in [descompress_zip, remove_zip]:
        os.system(i)
    
    #move file to folder
    move_file = f"mv {file} {folder}/{file}"
    os.system(move_file)
    return f"Your file is descompressed. Great!!"
