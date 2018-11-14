#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 11:36:04 2018

@author: skoebric
"""

import ipywidgets as widgets
import all_EVLoadModel
import warnings
import pickle
warnings.filterwarnings("ignore")

from IPython.core.display import display, HTML
display(HTML("<style>.container { width:85% !important; }</style>"))
display(HTML("<style>.output_wrapper, .output {height:auto !important; max-height:5000px;}.output_scroll {box-shadow:none !important; webkit-box-shadow:none !important;}</style>"))

get_ipython().run_line_magic('matplotlib', 'inline')

style = {'description_width': 'initial'}
   
numevswidget = widgets.Text(
                    value='300000',
                    description='Number of EVs:',
                    disabled=False,
                    style = style)
 

pctnodelayslider = widgets.FloatSlider(
                    value = .8,
                    min=0,
                    max=1,
                    step = .05,
                    description = 'Percent No Delay:',
                    disabled = False,
                    continuous_update = False,
                    orientation = 'horizontal',
                    readout = True,
                    readout_format = '.0%',
                    style = style)

pcttouslider = widgets.FloatSlider(
                    value = .2,
                    min=0,
                    max=1,
                    step = .05,
                    description = 'Percent Time of Use:',
                    disabled = False,
                    continuous_update = False,
                    orientation = 'horizontal',
                    readout = True,
                    readout_format = '.0%',
                    style = style)

pctshiftslider = widgets.FloatSlider(
                    value = 0,
                    min=0,
                    max=1,
                    step = .05,
                    description = 'Percent Shiftable:',
                    disabled = False,
                    continuous_update = False,
                    orientation = 'horizontal',
                    readout = True,
                    readout_format = '.0%',
                    style = style)

pctmaxdelayslider = widgets.FloatSlider(
                    value = 0,
                    min=0,
                    max = 1,
                    step = .05,
                    description = 'Percent Max Delay:',
                    disabled = False,
                    continuous_update = False,
                    orientation = 'horizontal',
                    readout = True,
                    readout_format = '.0%',
                    style = style)

pctminpowerslider = widgets.FloatSlider(
                    value = 0,
                    min=0,
                    max=1,
                    step = .05,
                    description = 'Percent Min Power:',
                    disabled = False,
                    continuous_update = False,
                    orientation = 'horizontal',
                    readout = True,
                    readout_format = '.0%',
                    style = style)

with open('respondents.pkl', 'rb') as infile:
    balancelist = pickle.load(infile)

balancewidget = widgets.Select(
                    options = sorted(balancelist),
                    value = 'MISO',
                    rows = 15,
                    description = 'Balancing Authority:',
                    disabled = False,
                    layout={'width':'600px'},
                    style = style
                    )

daywidget = widgets.Dropdown(
        options = ['Proportional Blend', 'Weekdays Only', 'Weekends Only'],
        description = 'Day of Week:',
        value = 'Proportional Blend',
        disabled = False,
        style = style)

def showbasicwidgets():
    def classcreator(balance, num_evs, pct_nodelay, pct_tou, pct_shift, pct_maxdelay, pct_minpower, dayofweek):
        c = all_EVLoadModel.EVLoadModel(balance = balance)
        c.plotall(num_evs = num_evs, pct_nodelay = pct_nodelay, pct_tou = pct_tou, pct_shift = pct_shift,
                  pct_maxdelay = pct_maxdelay, pct_minpower = pct_minpower, dayofweek = dayofweek)

    sliderbox1 = widgets.HBox([pctnodelayslider,pcttouslider])
    sliderbox2 = widgets.HBox([pctshiftslider,pctmaxdelayslider])
    sliderbox3 = widgets.HBox([pctminpowerslider])
    vbox = widgets.VBox([balancewidget, numevswidget,sliderbox1,sliderbox2,sliderbox3,daywidget])
    
    widgetout = widgets.interactive_output(classcreator, {'balance':balancewidget,
                                                          'num_evs':numevswidget,
                                                          'pct_nodelay':pctnodelayslider,
                                                          'pct_tou':pcttouslider,
                                                          'pct_shift':pctshiftslider,
                                                          'pct_maxdelay':pctmaxdelayslider,
                                                          'pct_minpower':pctminpowerslider,
                                                          'dayofweek':daywidget})
    display(vbox, widgetout)
#    

    
showbasicwidgets()
