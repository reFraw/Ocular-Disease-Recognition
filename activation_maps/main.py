import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import argparse
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2

from tqdm import tqdm


def arg_parser():
	parser = argparse.ArgumentParser(prog="AME", description="Activation Maps Extractor")
	group = parser.add_argument_group("Arguments")

	# REQUIRED ARGUMENT
	group.add_argument("-m", "--model", type=str, required=True,
						help="Path to saved model.")

	group.add_argument("-o", "--output", type=str, required=True,
						help="Path where output images are saved.")

	# OPTIONAL ARGUMENTS
	group.add_argument("-i", "--image", type=str, required=False,
						help="Path to test image.")

	group.add_argument("--summary", dest="summary", action="store_true",
						help="Print the model summary.")
	group.set_defaults(summary=False)

	arguments = parser.parse_args()

	return arguments 


def make_dirs(model_name):

	base_path = "output/"
	path = os.path.join(base_path, model_name)

	if not os.path.exists(path):
		os.makedirs(path)

	return path


def process_image(image_path, size, channels):

	image = cv2.imread(image_path)
	image = cv2.resize(image, size)

	if channels == 1:
		tensor_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		tensor_image = np.expand_dims(tensor_image, axis=0)
		tensor_image = tensor_image.reshape(-1, size[0], size[0], channels)

	elif channels == 3:
		tensor_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		tensor_image = np.expand_dims(tensor_image, axis=0)
		tensor_image = tensor_image.reshape(-1, size[0], size[0], channels)

	return tensor_image



if __name__ == "__main__":

	arguments = arg_parser()

	# Loading the model and printing the model summary
	print("\n[INFO] Loading model...")
	model = tf.keras.models.load_model(arguments.model)
	base_path = make_dirs(arguments.output)
	if arguments.summary:
		print("[INFO] Print model summary...\n")
		model.summary()

	# Extracting convolutional layers 
	conv_layers = []
	print("[INFO] Extract Convolutional Layers..")
	for layer in model.layers:
		if len(layer.output_shape) == 4 and len(layer.weights) != 0:
			conv_layers.append(layer.name)
	
	# Extract the input dimensions and number of channels
	# for image preprocessing.
	input_shape = model.layers[0].output_shape[0]
	image_size = (input_shape[1], input_shape[2])
	channels = input_shape[3]

	# Loading test image and apply preprocessing
	print("[INFO] Loading image ...")
	tensor_image = process_image(arguments.image, image_size, channels)

	# Extracting feature maps from each convolutional layer
	for conv_layer in tqdm(conv_layers):

		layer = model.get_layer(conv_layer)
		layer_output = layer.output
		maps_number = layer.output_shape[-1]

		layer_model = tf.keras.models.Model(inputs=model.input, outputs=layer_output)
		activation_maps = layer_model.predict(tensor_image)

		conv_layer_savepath = os.path.join(base_path, conv_layer)

		if not os.path.exists(conv_layer_savepath):
			os.makedirs(conv_layer_savepath)

		for i in range(maps_number):
			save_name = "activation_map_{}_layer_{}.png".format(i+1, conv_layer)
			savepath = os.path.join(conv_layer_savepath, save_name)
			maps = activation_maps[0,:,:,i]
			maps = cv2.resize(maps, (512, 512))
			plt.imsave(savepath, maps)

