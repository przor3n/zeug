#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file will have a sketch of a Zeug that will be called FirefoxZeug.
It will do:
- read what to do (scenario)
- read a list of sentences to translate (each line as sentence, can be csv)
- operate browser according to loaded scenario
- write log what it did
- return output

The scenario that will be run will do:
- load cookie if present
- enter deepl.com/translator url
- wait some time
- select input and output language as user desired
- wait some time
- for each sentence in loaded list of sentences:
    - wait some time
    - paste it into input
    - wait some time
    - read output
    - and put output into a list with input sentence and put into a csv file
    - wait fixed time (i think about something like perlin noise or smfing related to length
        of the sentence or sum of the letters)
- save output file into designated storage place and medium
- store cookie
"""
import random
from time import sleep

"""
I will use Germanium as a overlay on selenium for python
"""
from germanium.static import *
from selenium.webdriver.firefox.webdriver import WebDriver

__all__ = []

"""
Here are constants used in program
"""
URL = "https://www.deepl.com/translator"

# CSS Class of the input and output textarea
input= "css:.lmt__source_textarea"
output= "css:.lmt__target_textarea"

# CSS Classes of language selectors and the lists of languages
input_language_select_class = "css:.lmt__language_select--source .lmt__language_select__opener"
input_language_list_class = "css:.lmt__language_select--source ul"
outpt_language_select_class = "css:.lmt__side_container--target .lmt__language_select__opener"
outpt_language_list_class = "css:.lmt__side_container--target ul"

left_select = {
    'click': input_language_select_class,
    'language': lambda lang: input_language_list_class + " " + LANGUAGE_DICT[lang]
}

right_select = {
    'click': outpt_language_select_class,
    'language': lambda lang: input_language_list_class + " " + LANGUAGE_DICT[lang]
}

"""
Bellow is the list of languages usd in deepl.com
<ul>
    <li dl-value="auto">Any language (detect)</li>
    <li dl-value="EN">English</li>
    <li dl-value="DE">German</li>
    <li dl-value="FR">French</li>
    <li dl-value="ES">Spanish</li>
    <li dl-value="IT">Italian</li>
    <li dl-value="NL">Dutch</li>
    <li dl-value="PL">Polish</li>
</ul>
"""
LANGUAGE_LIST=['auto', 'EN', 'DE', 'FR', 'ES', 'IT', 'NL', 'PL']
LANGUAGE_DICT= dict(zip(LANGUAGE_LIST, LANGUAGE_LIST))

"""
This class is getting the random number
"""
class HumanRandom:
    START = 10
    BASE = 4

    def random_number(self):
        return random.randint(-3, 4)

    # This is a function that will be a noise generator
    def noise(self):
        self.START = int((self.START + self.random_number())/2) + self.BASE
        return self.START


"""
I will use directive wd of the Germanium open_browser function.
This way I can load easly customizable firefox instance.
TODO: can I turn off the robot signature of firefox
TODO: does ff has a robot signature?
"""
ffdriver = WebDriver(firefox_binary='/usr/bin/firefox')

"""
Here I open browser and load URL.
"""
human = HumanRandom()
open_browser(wd=ffdriver)
go_to(URL)

"""
Instructions to follow:

left_select:
    click: 
    language: function (lang) { return selector + lang }
    
right_select:
    click:
    language: function (lang) { return selector + lang }


select language select:
 click on select.click
 wait like human
 click on select.language(lang)

select language left_select

wait like human

select language right_select

for sentence in sentences:
    paste sentence to input_textarea
    wait like human
    save read output_textarea

translation = zip(sentences, saved output)
save translation to csv
"""

def select_language(lang, select):
    click(select['click'])
    sleep(human.noise())
    click(select['language'](lang))


select_language('EN', left_select)
sleep(human.noise())
select_language('PL', right_select)

sentences = []
translation = []

for sentence in sentences:
    type_keys(sentence, input)
    sleep(human.noise())
    translation.append(get_text(output))

# return translation