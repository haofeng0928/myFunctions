import os
import math
import six

import tensorflow as tf
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from bucketdata import BucketData

# tf.enable_eager_execution()

# data path
root_dir = r'D:\myData\huawei_datetext'
train_img_dir = r'D:\myData\huawei_datetext\train_img'
train_label_path = r'D:\myData\huawei_datetext\train_txt_1.txt'
lexicon_path = r'D:\myData\huawei_datetext\date_lexicon.txt'
tfrecord_path = r'D:\myData\huawei_datetext\train_txt_1.tfrecord'

# bucket
img_width_range = [12, 320]
word_len = 30
img_height = 32
bucket_specs = [(int(math.ceil(img_width_range[1] / 4)), int(word_len + 2))]  # 80, 32
min_bucket, max_bucket = img_width_range
bucket = [[] for _ in range(10)]
bucket_data = {i: BucketData() for i in range(100, 500, 100)}


def write_tfrecord(img_label, tfrecord_path):
    with tf.python_io.TFRecordWriter(tfrecord_path) as writer:
        for item in img_label:
            # # img = tf.io.read_file(item[0])
            # img_raw = tf.gfile.GFile(item[0], 'rb').read()
            # print(img_raw, type(img_raw))
            # img = tf.image.decode_jpeg(img_raw)
            # # plt.imshow(img)
            # # plt.show()
            #
            # # resize
            # h, w, c = img.get_shape()
            # img = tf.image.convert_image_dtype(img, dtype=tf.float32)
            # img = tf.image.resize(img, (32, int(w) * int(h) // 32))
            # img = tf.image.convert_image_dtype(img, dtype=tf.uint8)
            # # plt.imshow(img)
            # # plt.show()
            #
            # img = tf.image.rgb_to_grayscale(img)
            # # plt.imshow(img, cmap='gray')
            # # plt.show()
            #
            # img = tf.image.encode_jpeg(img)
            # print(type(img))
            # img = img.encode()
            # label = item[1].encode()

            img_raw = Image.open(item[0])
            w, h = img_raw.size
            img_resize = img_raw.resize((32 * w // h, 32))
            size = img_resize.size
            img_gray = img_resize.convert('L')
            img = img_gray.tobytes()
            label = item[1].encode()

            feature = {
                'image': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img])),
                'label': tf.train.Feature(bytes_list=tf.train.BytesList(value=[label])),
                'height': tf.train.Feature(int64_list=tf.train.Int64List(value=[size[1]])),
                'width': tf.train.Feature(int64_list=tf.train.Int64List(value=[size[0]])),
                'channel': tf.train.Feature(int64_list=tf.train.Int64List(value=[1])),
            }
            example = tf.train.Example(features=tf.train.Features(feature=feature))
            string = example.SerializeToString()  # 序列化为字符串
            writer.write(string)


def read_tfrecord(tfrecord_path):

    def ParseAndProcess(record):
        features = [('image', tf.VarLenFeature(tf.string)),
                    ('label', tf.VarLenFeature(tf.string)),
                    ('height', tf.VarLenFeature(tf.int64)),
                    ('width', tf.VarLenFeature(tf.int64)),
                    ('channel', tf.VarLenFeature(tf.int64)),
                    ]
        # features = [('image', tf.FixedLenFeature([], tf.string)),
        #             ('label', tf.FixedLenFeature([], tf.string)),
        #             ('height', tf.FixedLenFeature([], tf.int64)),
        #             ('width', tf.FixedLenFeature([], tf.int64)),
        #             ('channel', tf.FixedLenFeature([], tf.int64)),
        #             ]
        example = tf.parse_single_example(record, dict(features))
        res = {k: v.values for k, v in six.iteritems(example)}
        return res['image'], res['label'], res['height'], res['width'], res['channel']

    def element_length_fn(image, label, height, width, channel):
        width = tf.cast(width, dtype=tf.int32)
        return width

    dataset = tf.data.Dataset.list_files(tfrecord_path, shuffle=True)
    dataset = dataset.apply(
        tf.data.experimental.parallel_interleave(tf.data.TFRecordDataset, cycle_length=1, sloppy=True))
    dataset = dataset.map(ParseAndProcess, num_parallel_calls=10)
    dataset = dataset.shuffle(512)

    bucket_boundaries = [100, 200, 300, 400, 500]
    dataset = dataset.apply(
        tf.data.experimental.bucket_by_sequence_length(
            element_length_func=element_length_fn,
            bucket_boundaries=bucket_boundaries,
            bucket_batch_sizes=[1] * (len(bucket_boundaries)+1),
            no_padding=True,
        ))
    # dataset = dataset.prefetch(buffer_size=1)  # 预取buffer_size个batch
    # dataset = dataset.repeat()
    iterator = dataset.make_one_shot_iterator()
    output_batch = iterator.get_next()

    return output_batch[0], output_batch[1], output_batch[2], output_batch[3], output_batch[4]


if __name__ == '__main__':
    if not os.path.exists(tfrecord_path):
        print('tfrecord already exists.')
    else:
        # dataset
        with open(train_label_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            img_label = [list(line.strip().split()) for line in lines]
            for item in img_label:
                item[0] = os.path.join(train_img_dir, item[0])
            # for i in img_label[:10]:
            #     print(i)

        # write
        print('Generating tfrecord....')
        write_tfrecord(img_label, tfrecord_path)
        print('tfrecord is completed.')

    # read
    with tf.Session() as sess:
        batches = 5000
        for i in range(batches):
            (image, label, height, width, channel) = read_tfrecord(tfrecord_path)
            (image, label, height, width, channel) = sess.run([image, label, height, width, channel])

            # print('batch {} / {}'.format(i+1, batches))
            # print('image: ', image)
            # print('label: ', label)
            # print('height: ', height)
            print('width: ', width)
            # print('channel: ', channel)


