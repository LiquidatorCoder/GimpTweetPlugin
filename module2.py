#!/usr/bin/env python

from gimpfu import *
from datetime import datetime
import random
import requests
from bs4 import BeautifulSoup 
"""
un=random.randint(1,10)
URL = "http://quotes.toscrape.com/"
URL = URL+"page/"+str(un)+"/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
quotes=[]
content=soup.findAll('div',{"class","quote"})
for data in content:
    quote=data.find('span',{'class','text'}).text
    author=data.find('small',{'class','author'}).text
    quote=quote+" - "+author
    quotes.append(quote)
qn=random.randint(1,10)"""
r=random.randint(150,225)
g=random.randint(150,225)
b=random.randint(150,225)
"""r=21
g=32
b=43"""

def Content(image, drawable, arg):
        quote=arg
        #quote="The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking. - Albert Einstein"
        quote=quote.split(" ")
        c=0
        c2=0
        sentence=""
        for word in quote:
            if c!=3:
                sentence = sentence + word + " "
                c+=1
                c2+=1
            else:
                sentence = sentence + "\n" + word + " "
                c=0
                c2+=1
	w = 3648
	h = 3648
	new_image =pdb.gimp_image_new(w, h, 0) #returns an IMAGE type
	pdb.gimp_display_new(new_image)
	
	new_layer = pdb.gimp_layer_new(new_image, w, h, 1, "Background", 100, 1) #returns a LAYER type
	pdb.gimp_image_insert_layer(new_image, new_layer, None, 0)
	
	#pdb.gimp_image_crop(image, 1200, 1200, 0, 0)
	
	image = new_image
	drawable = new_layer

	pdb.gimp_image_select_rectangle(image, 0, 0, 0, w, h)
	#pdb.gimp_context_set_foreground((240,56,107))
	pdb.gimp_context_set_foreground((r,g,b))
	pdb.gimp_edit_bucket_fill(drawable, 0, 0, 100, 255, 0, 0, 0)
	pdb.gimp_selection_none(image)
	
	new_layer = pdb.gimp_layer_new(new_image, w, h, 1, "Round Box", 100, 1) #returns a LAYER type
	pdb.gimp_image_insert_layer(new_image, new_layer, None, 0)
	
	image = new_image
	drawable = new_layer
	
	pdb.gimp_image_select_round_rectangle(image, 0, 100, 100, w-200, h-200, 100, 100)
	#pdb.gimp_context_set_foreground((255,83,118))
	pdb.gimp_context_set_foreground((r-30,g-30,b-30))
	#pdb.gimp_context_set_background((255,120,160))
	pdb.gimp_context_set_background((r+30,g+30,b+30))
	pdb.gimp_drawable_edit_gradient_fill(drawable, 0, 0, True, 1, 1, True, 1000, 3148, 1000, 500)
	#pdb.gimp_edit_bucket_fill(drawable, 0, 0, 100, 255, 0, 500, 500)
	pdb.gimp_selection_none(image)

        for i in range(random.randint(1,3)):
            new_layer = pdb.gimp_layer_new(new_image, w, h, 1, "Circle"+str(i), 100, 1) #returns a LAYER type
            pdb.gimp_image_insert_layer(new_image, new_layer, None, 0)
	
            image = new_image
            drawable = new_layer

            size=random.randint(400,1500)
            cx=random.randint(1500,w-size-200)
            cy=random.randint(200,w-size-200)
            pdb.gimp_image_select_ellipse(image, 0, cx, cy, size, size)
            pdb.gimp_context_set_foreground((r-10,g-10,b-10))
            pdb.gimp_context_set_background((r+10,g+10,b+10))
            pdb.gimp_drawable_edit_gradient_fill(drawable, 0, 0, True, 1, 1, True, cx+(size/2), cy+(3*size/4), cx+(size/2), cy+(size/4))
            pdb.gimp_selection_none(image)

	new_layer = pdb.gimp_layer_new(new_image, w, h, 1, "Text", 100, 1) #returns a LAYER type
	pdb.gimp_image_insert_layer(new_image, new_layer, None, 0)
	
	image = new_image
	drawable = new_layer

	if c2>=30 and c2<45:
            ts=200
        elif c2>=45:
            ts=120
        else:
            ts=300
	#pdb.gimp_context_set_foreground((248,192,200))
	pdb.gimp_context_set_foreground((r/2,g/2,b/2))
	text_layer = pdb.gimp_text_fontname(image, drawable, 350, 600, sentence, 100, True, ts, 1, "BigNoodleTitling")
	pdb.gimp_selection_none(image)
	
	layer = pdb.gimp_file_load_layer(image, "logo.png")
	pdb.gimp_image_insert_layer(new_image, layer, None, 0)
	drawable = pdb.gimp_drawable_transform_perspective_default(layer, 3048, 3148, 3548, 3148, 3048, 3648, 3548, 3648, True, 0)
	#pdb.gimp_layer_resize(layer, 500, 500, 0, 0)
	
	#layer = pdb.gimp_image_flatten(image)
	#pdb.file_jpeg_save(new_image, layer, 'post.jpg', 'post.jpg', 1, 0, 0, 1, 'post to post', 2, 1, 0, 0)

register(
    "python-fu-POST-GENERATOR",
    "Creates content to post",
    "This script can be used to create content to post",
    "Abhay Maurya", "Abhay Maurya", "2019",
    "Post Generator",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [   # basic parameters are: (UI_ELEMENT, "variable", "label", Default)
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
        (PF_STRING, "arg", "Input Text", "Text to post") 
        # PF_SLIDER, SPINNER have an extra tuple (min, max, step)
        # PF_RADIO has an extra tuples within a tuple:
        # eg. (("radio_label", "radio_value), ...) for as many radio buttons
        # PF_OPTION has an extra tuple containing options in drop-down list
        # eg. ("opt1", "opt2", ...) for as many options
        # see ui_examples_1.py and ui_examples_2.py for live examples
    ],
    [],
    Content, menu="<Image>/File")  # second item is menu location

main()
