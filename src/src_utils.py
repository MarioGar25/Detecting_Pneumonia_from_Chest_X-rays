import os
import tensorflow as tf

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

def load_transform(image, label, train = True):
    image = tf.io.read_file(image)
    image = tf.io.decode_jpeg(image, channels = 3)
    image = tf.image.resize(image, [224, 224], method = "nearest")

    if train:
        image = tf.image.random_flip_left_right(image)
    
    return image, label 

def get_dataset(paths, labels, batch_size, train = True):
    image_paths = tf.convert_to_tensor(paths)
    labels = tf.convert_to_tensor(labels)

    image_dataset = tf.data.Dataset.from_tensor_slices(image_paths)
    label_dataset = tf.data.Dataset.from_tensor_slices(labels)

    dataset = tf.data.Dataset.zip((image_dataset, label_dataset)).shuffle(1000)

    dataset = dataset.map(lambda image, label: load_transform(image, label, train)).repeat().shuffle(20480).batch(batch_size)

    return dataset
