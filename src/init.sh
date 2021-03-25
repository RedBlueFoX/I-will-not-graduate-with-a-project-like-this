#!/usr/bin/env bash
while true; do
    read -p "Create source files?" yn
    case $yn in
        [Yy]* ) touch main.py
				mkdir script_builder
				touch ./script_builder/generator.py
				mkdir text_generator
				touch ./text_generator/generator.py
				touch ./text_generator/discriminator.py
				touch ./text_generator/train.py
				mkdir client
				touch ./client/index.html
				mkdir ./client/javascript
				touch ./client/javascript/main.js
			 	break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
