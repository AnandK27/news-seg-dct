# jpeg-encoding
##Input Image
-Put the input images in the /input directory and run the resize.py file to resize them into dimensions divisible by 8.
-The resized input images are saved in /input_rs directory

##Encoding Steps
-RGB -> YCbCr
-YCbCr -> DCT -> Quantization
-Quantized blocks -> Zigzag
-Zigzag array -> Run length encoding -> Huffman encoding -> Written into the output file in /output directory

##Decoding Steps
-Huffman decoding -> Run Length Decoding 
-Unzigzag -> Dequantization -> inverse DCT
-YCbCr->RGB
