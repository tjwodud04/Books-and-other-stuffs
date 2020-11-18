import tensorflow as tf

def linear_layer(x):
  return 3 * x + 2

@tf.function
def simple_nn(x):
  return tf.nn.relu(linear_layer(x))

def simple_function(x):
	return 3*x

print(tf.autograph.to_code(simple_nn.python_function, experimental_optional_features=None))

'''
def tf__simple_nn(x):
    do_return = False
    retval_ = ag__.UndefinedReturnValue()
    with ag__.FunctionScope('simple_nn', 'fscope', ag__.ConversionOptions(recursive=True, user_requested=True, optional_features=(), internal_convert_user_code=True)) as fscope:
        try:
            do_return = True
            retval_ = fscope.mark_return_value(ag__.converted_call(tf.nn.relu, (ag__.converted_call(linear_layer, (x,), None, fscope),), None, fscope))
        except:
            do_return = False
            raise
    (do_return,)
    return ag__.retval(retval_)

Process finished with exit code 0
'''