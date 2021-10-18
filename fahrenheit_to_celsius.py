# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 20:38:09 2021

@author: Ingo Kodba
Python script that goes through text in files and converts fahrenheit temperatures to celsius temperatures. It is possible to change program to do the opposite.

Define your own prefix, lists of suffixes, path to directories of files, file extension of files and whether to convert F to C or C to F
There are multiple possible suffixes to define, so it's a list. For a match with specific suffix in old_suffixes, string with the same index in new_suffixes will be used to replace the old suffix. So in this example if the suffix string of the temperature equals °F or just °, it will be replaced with °C in both cases. In old_suffix list it is important to put longer strings first because otherwise in this example there would never be match with °F because it would match with ° immediately and go to the next word.
"""
import re
import os

prefix = ""
old_suffixes = ["°F", "°"]
new_suffixes = ["°C", "°C"]
read_directory = r'C:\Users\Krepana Krava\Documents\cookinga\text'
write_directory = r'C:\Users\Krepana Krava\Documents\cookinga\mext'
file_extension = '.html'
fahrenheit_to_celsius = True # True for F to C, False for C to F

text = ""
    
def celsius(fahrenheit):
    return int((int(fahrenheit) - 32) * 5/9)

def fahrenheit(celsius):
    return int((int(celsius) * 9/5) + 32)

#sampletext = "...bubbles. The second phase of the double act occurs only at higher temperatures (around 170° to 180°F), when a second powdered acid (typically sodium aluminum sulfate) reacts with the remaining sodium bicarbonate, producing another round of bubbles. The thickening action is a side effect of the starch used to ke..."

for filename in os.listdir(read_directory):
    if filename.endswith(file_extension):
        changes = False
        with open(os.path.join(read_directory, filename), encoding='utf-8') as f:
            text = f.read()

        text_splitted = text.split()
        
        for i, word in enumerate(text_splitted):
            
            for suffix_index, suffix in enumerate(old_suffixes):
            
                match = re.search(prefix+"\d+"+suffix, word)
                if match:
                    print(match.string, end=' ')
                    string_with_number = re.search("\d+", match.string[match.span()[0]:])
                    if string_with_number:
                        start = string_with_number.span()[0]
                        end = string_with_number.span()[1]
                        old_temp = string_with_number.string[start:end]
                        if fahrenheit_to_celsius:
                            new_temp = celsius(old_temp)
                        else:
                            new_temp = fahrenheit(old_temp)
                        # replace old string with new string
                        text_splitted[i] = re.sub(match.string[match.span()[0]:match.span()[1]], str(new_temp)+new_suffixes[suffix_index], word)
                        changes = True
                        print(text_splitted[i])
                        break
                
        if changes:
            text = ' '.join(text_splitted)
            with open(os.path.join(write_directory, filename), 'w', encoding='utf-8') as f:
                f.write(text)
        