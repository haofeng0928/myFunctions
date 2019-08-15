import tensorflow as tf

# # 单次迭代器仅支持对数据集进行一次迭代，不需要显式初始化。
# # 单次迭代器可以处理现有的基于队列的输入管道支持的几乎所有情况，但不支持参数化。
# dataset = tf.data.Dataset.range(10)
# iterator = dataset.make_one_shot_iterator()
# next_element = iterator.get_next()
# with tf.Session() as sess:
#     for i in range(10):
#         value = sess.run(next_element)
#         print(value)


# # 可初始化迭代器需要先运行显式 iterator.initializer 指令，才能使用。
# # 虽然有些不便，但它允许使用一个或多个 tf.placeholder() 张量。
# max_value = tf.placeholder(tf.int64, shape=[])
# dataset = tf.data.Dataset.range(max_value)
# iterator = dataset.make_initializable_iterator()
# next_element = iterator.get_next()
# with tf.Session() as sess:
#     # Initialize an iterator over a dataset with 10 elements.
#     sess.run(iterator.initializer, feed_dict={max_value: 10})
#     for i in range(10):
#         value = sess.run(next_element)
#         print(value)
#
#     # Initialize the same iterator over a dataset with 5 elements.
#     sess.run(iterator.initializer, feed_dict={max_value: 5})
#     for i in range(5):
#         value = sess.run(next_element)
#         print(value)


# # 可重新初始化迭代器可以通过多个不同的 Dataset 对象进行初始化。
# # 例如，您可能有一个训练输入管道，它会对输入图片进行随机扰动来改善泛化；
# # 还有一个验证输入管道，它会评估对未修改数据的预测。
# # 这些管道通常会使用不同的 Dataset 对象，这些对象具有相同的结构。
# training_dataset = tf.data.Dataset.range(10).map(lambda x: x + tf.random_uniform([], -10, 10, tf.int64))
# validation_dataset = tf.data.Dataset.range(5)
#
# iterator = tf.data.Iterator.from_structure(training_dataset.output_types, training_dataset.output_shapes)
# next_element = iterator.get_next()
#
# training_init_op = iterator.make_initializer(training_dataset)
# validation_init_op = iterator.make_initializer(validation_dataset)
#
# with tf.Session() as sess:
#     for _ in range(2):
#         sess.run(training_init_op)
#         for _ in range(10):
#             sess.run(next_element)
#         sess.run(validation_init_op)
#         for _ in range(5):
#             sess.run(next_element)


# 可feeding迭代器可以与tf.placeholder一起使用，通过熟悉的feed_dict机制来选择每次调用tf.Session.run时所使用的Iterator。
# 它提供的功能与可重新初始化迭代器的相同，但在迭代器之间切换时不需要从数据集的开头初始化迭代器。
# 例如，可以使用tf.data.Iterator.from_string_handle定义一个可在两个数据集之间切换的可feeding迭代器：
training_dataset = tf.data.Dataset.range(10).map(lambda x: x + tf.random_uniform([], -10, 10, tf.int64)).repeat()
validation_dataset = tf.data.Dataset.range(5)

handle = tf.placeholder(tf.string, shape=[])
iterator = tf.data.Iterator.from_string_handle(handle, training_dataset.output_types, training_dataset.output_shapes)
next_element = iterator.get_next()

# You can use feedable iterators with a variety of different kinds of iterator
training_iterator = training_dataset.make_one_shot_iterator()
validation_iterator = validation_dataset.make_initializable_iterator()

with tf.Session() as sess:
    training_handle = sess.run(training_iterator.string_handle())
    validation_handle = sess.run(validation_iterator.string_handle())
    for _ in range(2):
        sess.run(next_element, feed_dict={handle: training_handle})
    sess.run(validation_iterator.initializer)
    for _ in range(2):
        sess.run(next_element, feed_dict={handle: validation_handle})

