import tensorflow as tf
from google.protobuf.json_format import MessageToJson
...

def crop_dataset():
    pass


if __name__ == '__main__':

    for example in tf.python_io.tf_record_iterator("datasets/WaterDrop/train.tfrecord"):
        # print(tf.train.Example.FromString(example))
        jsonMessage = MessageToJson(tf.train.Example.FromString(example))
        print(jsonMessage)