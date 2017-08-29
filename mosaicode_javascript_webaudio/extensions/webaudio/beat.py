#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Beat(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.help = "Beat"
        self.label = "BeatValue"
        self.color = "150:150:250:150"
        self.out_ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "label":"Float",
                "name":"float"}
            ]
        self.in_ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "label":"Start",
                "name":"start"},
                {"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "label":"Stop",
                "name":"stop"}
            ]
        self.group = "Interface"

        self.properties = [{"name": "value",
                            "label": "Value",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 20000,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "time",
                            "label": "Time (ms)",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 20000,
                            "step": 1,
                            "value": 1000
                            }
                           ]

        self.codes["declaration"] = """
// block_$id$ = Float Value
var block_$id$_timeout;
var block_$id$_value = $prop[value]$;
var block_$id$_time = $prop[time]$;
var $out_ports[float]$ = [];

var $in_ports[start]$ = function(value){
    timeout_$id$_value();
    return true;
    };

var $in_ports[stop]$ = function(value){
    clearTimeout(block_$id$_timeout);
    return true;
    };

"""
        self.codes["execution"] = """
function timeout_$id$_value(){
    for (var i = 0; i < $out_ports[float]$.length ; i++){
        $out_ports[float]$[i](block_$id$_value);
    }
    block_$id$_timeout = setTimeout(timeout_$id$_value, block_$id$_time);
};
"""
        self.codes["onload"] = """"""