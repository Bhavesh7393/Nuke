'''
Below are "onCreate" and "knobChanged" knob values for Vector Displacement Converter Gizmo.
'''

import nuke


# Force knob changes

sel = nuke.toNode("VectorDisplacementConverter1")
sel["z_in"].setRange(1,48) # Set Range (1, 48)
sel["z_in"].setDefaultValue([1]) # Set Deafult Value (1)
sel["z_in"].setFlag(0x0000000000000010) # Force Range (1, 48)
sel.knob("w_convert").setValue("<font color='red'>NO NEED TO CONVERT !") # Red Color Text
sel["z_out"].setRange(1,48) # Set Range (1, 48)
sel["z_out"].setDefaultValue([1]) # Set Deafult Value (1)
sel["z_out"].setFlag(0x0000000000000010) # Force Range (1, 48)
sel.knob("t_convert").setValue("<font color='red'>NO NEED TO CONVERT !") # Red Color Text


# "onCreate" knob values

nuke.toNode("VectorDisplacementConverter1").knob("onCreate").setValue('''
n = nuke.thisNode()
n["z_in"].setRange(1,48)
n["z_in"].setDefaultValue([1.0])
n["z_in"].setFlag(0x0000000000000010)
n["z_out"].setRange(1,48)
n["z_out"].setDefaultValue([1.0])
n["z_out"].setFlag(0x0000000000000010)
''')


# "knobChanged" knob values

nuke.toNode("VectorDisplacementConverter1").knob("knobChanged").setValue('''

#  Current node
n = nuke.thisNode()
k = nuke.thisKnob()

# World Checkbox
def w_vis(bool):
    n["w_line"].setVisible(bool)
    n["w_in"].setVisible(bool)
    n["w_zbrush_in"].setVisible(bool)
    n["w_out"].setVisible(bool)
    n["w_zbrush_out"].setVisible(bool)

# Tangent Checkbox
def t_vis(bool):
    n["t_line"].setVisible(bool)
    n["t_in"].setVisible(bool)
    n["t_out"].setVisible(bool)
    n["t_zbrush_in"].setVisible(bool)
    n["t_zbrush_out"].setVisible(bool)

# ZBrush Checkbox
def z_vis(bool):
    n["z_line"].setVisible(bool)
    n["z_in"].setVisible(bool)
    n["z_out"].setVisible(bool)

# Clear Selection
def clear():
    allNodes = nuke.allNodes()
    for node in allNodes:
        node.setSelected(True)
    nukescripts.remove_inputs()
    for node in allNodes:
        node.setSelected(False)

# Input Function
def input(input_shuffle, input_multiply):
    clear()
    nuke.toNode(input_shuffle).setInput(0, nuke.toNode("Input"))
    nuke.toNode(input_multiply).setInput(0, nuke.toNode(nuke.toNode("Input").dependent()[0]["name"].value()))
    nuke.toNode("Output").setInput(0, nuke.toNode("Input"))

# Output Function
def output(output_multiply, output_shuffle):
    nuke.toNode(output_multiply).setInput(0, nuke.toNode(nuke.toNode("Input").dependent()[0]["name"].value()).dependent()[0])
    nuke.toNode(output_shuffle).setInput(0, nuke.toNode(output_multiply))
    nuke.toNode("Output").setInput(0, nuke.toNode(output_shuffle))

# World Pulldown List
def world():
    if k.name() == "w_in" and k.value() == "Mudbox (World/Object)":
        input("in_ch_ZYX", "in_mul__X_YZ") # Input FlipAndSwitch 47
        n["w_zbrush_in"].setValue("47")
    elif k.name() == "w_in" and k.value() == "Arnold":
        input("in_ch_ZYX", "in_mul__X_YZ") # Input FlipAndSwitch 47
        n["w_zbrush_in"].setValue("47")
    elif k.name() == "w_in" and k.value() == "Clarisse":
        input("in_ch_ZYX", "in_mul__X_YZ") # Input FlipAndSwitch 47
        n["w_zbrush_in"].setValue("47")
    elif k.name() == "w_in" and k.value() == "Cycles":
        input("in_ch_YZX", "in_mul_X_YZ") # Input FlipAndSwitch 27
        n["w_zbrush_in"].setValue("27")
    elif k.name() == "w_in" and k.value() == "Karma":
        input("in_ch_ZYX", "in_mul__X_YZ") # Input FlipAndSwitch 47
        n["w_zbrush_in"].setValue("47")
    elif k.name() == "w_in" and k.value() == "Mantra":
        input("in_ch_ZYX", "in_mul__X_YZ") # Input FlipAndSwitch 47
        n["w_zbrush_in"].setValue("47")
    elif k.name() == "w_in" and k.value() == "Octane":
        input("in_ch_YZX", "in_mul__X_YZ") # Input FlipAndSwitch 31
        n["w_zbrush_in"].setValue("31")
    elif k.name() == "w_in" and k.value() == "Renderman":
        input("in_ch_ZYX", "in_mul_XYZ") # Input FlipAndSwitch 41
        n["w_zbrush_in"].setValue("41")
    elif k.name() == "w_in" and k.value() == "Redshift":
        input("in_ch_ZYX", "in_mul__X_YZ") # Input FlipAndSwitch 47
        n["w_zbrush_in"].setValue("47")
    elif k.name() == "w_in" and k.value() == "V-Ray (Object)":
        input("in_ch_ZYX", "in_mul__X_YZ") # Input FlipAndSwitch 47
        n["w_zbrush_in"].setValue("47")
    elif k.name() == "w_out" and k.value() == "Mudbox (World/Object)":
        output("out_mul__X_YZ", "out_ch_ZYX") # Output FlipAndSwitch 47
        n["w_zbrush_out"].setValue("47")
    elif k.name() == "w_out" and k.value() == "Arnold":
        output("out_mul__X_YZ", "out_ch_ZYX") # Output FlipAndSwitch 47
        n["w_zbrush_out"].setValue("47")
    elif k.name() == "w_out" and k.value() == "Clarisse":
        output("out_mul__X_YZ", "out_ch_ZYX") # Output FlipAndSwitch 47
        n["w_zbrush_out"].setValue("47")
    elif k.name() == "w_out" and k.value() == "Cycles":
        output("out_mul_X_YZ", "out_ch_ZXY") # Output FlipAndSwitch 27
        n["w_zbrush_out"].setValue("27")
    elif k.name() == "w_out" and k.value() == "Karma":
        output("out_mul__X_YZ", "out_ch_ZYX") # Output FlipAndSwitch 47
        n["w_zbrush_out"].setValue("47")
    elif k.name() == "w_out" and k.value() == "Mantra":
        output("out_mul__X_YZ", "out_ch_ZYX") # Output FlipAndSwitch 47
        n["w_zbrush_out"].setValue("47")
    elif k.name() == "w_out" and k.value() == "Octane":
        output("out_mul__X_YZ", "out_ch_ZXY") # Output FlipAndSwitch 31
        n["w_zbrush_out"].setValue("31")
    elif k.name() == "w_out" and k.value() == "Renderman":
        output("out_mul_XYZ", "out_ch_ZYX") # Output FlipAndSwitch 41
        n["w_zbrush_out"].setValue("41")
    elif k.name() == "w_out" and k.value() == "Redshift":
        output("out_mul__X_YZ", "out_ch_ZYX") # Output FlipAndSwitch 47
        n["w_zbrush_out"].setValue("47")
    elif k.name() == "w_out" and k.value() == "V-Ray (Object)":
        output("out_mul__X_YZ", "out_ch_ZYX") # Output FlipAndSwitch 47
        n["w_zbrush_out"].setValue("47")
    else:
        pass

# Tangent Pulldown List
def tangent():
    if k.name() == "t_in" and k.value() == "Mudbox Absolute Tangent":
        input("in_ch_YZX", "in_mul_XYZ") # Input FlipAndSwitch 25
        n["t_zbrush_in"].setValue("25")
    elif k.name() == "t_in" and k.value() == "Houdini/Arnold":
        input("in_ch_ZYX", "in_mul_XYZ") # Input FlipAndSwitch 41
        n["t_zbrush_in"].setValue("41")
    elif k.name() == "t_in" and k.value() == "Houdini/Karma":
        input("in_ch_ZYX", "in_mul_XYZ") # Input FlipAndSwitch 41
        n["t_zbrush_in"].setValue("41")
    elif k.name() == "t_in" and k.value() == "Houdini/Mantra":
        input("in_ch_ZYX", "in_mul_XYZ") # Input FlipAndSwitch 41
        n["t_zbrush_in"].setValue("41")
    elif k.name() == "t_in" and k.value() == "Houdini/Renderman":
        input("in_ch_ZYX", "in_mul_XYZ") # Input FlipAndSwitch 41
        n["t_zbrush_in"].setValue("41")
    elif k.name() == "t_in" and k.value() == "Maya/Arnold":
        input("in_ch_YZX", "in_mul_XYZ") # Input FlipAndSwitch 25
        n["t_zbrush_in"].setValue("25")
    elif k.name() == "t_in" and k.value() == "Maya/Renderman":
        input("in_ch_ZYX", "in_mul_X_Y_Z") # Input FlipAndSwitch 44
        n["t_zbrush_in"].setValue("44")
    elif k.name() == "t_in" and k.value() == "Clarisse":
        input("in_ch_ZYX", "in_mul_XYZ") # Input FlipAndSwitch 41
        n["t_zbrush_in"].setValue("41")
    elif k.name() == "t_in" and k.value() == "Cycles":
        input("in_ch_YZX", "in_mul_XYZ") # Input FlipAndSwitch 25
        n["t_zbrush_in"].setValue("25")
    elif k.name() == "t_in" and k.value() == "Octane":
        input("in_ch_YZX", "in_mul_XYZ") # Input FlipAndSwitch 25
        n["t_zbrush_in"].setValue("25")
    elif k.name() == "t_in" and k.value() == "Redshift":
        input("in_ch_YZX", "in_mul__XY_Z") # Input FlipAndSwitch 30
        n["t_zbrush_in"].setValue("30")
    elif k.name() == "t_in" and k.value() == "V-Ray (Absolute)":
        input("in_ch_YZX", "in_mul_XYZ") # Input FlipAndSwitch 25
        n["t_zbrush_in"].setValue("25")
    elif k.name() == "t_out" and k.value() == "Mudbox Absolute Tangent":
        output("out_mul_XYZ", "out_ch_ZXY") # Output FlipAndSwitch 25
        n["t_zbrush_out"].setValue("25")
    elif k.name() == "t_out" and k.value() == "Houdini/Arnold":
        output("out_mul_XYZ", "out_ch_ZYX") # Output FlipAndSwitch 41
        n["t_zbrush_out"].setValue("41")
    elif k.name() == "t_out" and k.value() == "Houdini/Karma":
        output("out_mul_XYZ", "out_ch_ZYX") # Output FlipAndSwitch 41
        n["t_zbrush_out"].setValue("41")
    elif k.name() == "t_out" and k.value() == "Houdini/Mantra":
        output("out_mul_XYZ", "out_ch_ZYX") # Output FlipAndSwitch 41
        n["t_zbrush_out"].setValue("41")
    elif k.name() == "t_out" and k.value() == "Houdini/Renderman":
        output("out_mul_XYZ", "out_ch_ZYX") # Output FlipAndSwitch 41
        n["t_zbrush_out"].setValue("41")
    elif k.name() == "t_out" and k.value() == "Maya/Arnold":
        output("out_mul_XYZ", "out_ch_ZXY") # Output FlipAndSwitch 25
        n["t_zbrush_out"].setValue("25")
    elif k.name() == "t_out" and k.value() == "Maya/Renderman":
        output("out_mul_X_Y_Z", "out_ch_ZYX") # Output FlipAndSwitch 44
        n["t_zbrush_out"].setValue("44")
    elif k.name() == "t_out" and k.value() == "Clarisse":
        output("out_mul_XYZ", "out_ch_ZYX") # Output FlipAndSwitch 41
        n["t_zbrush_out"].setValue("41")
    elif k.name() == "t_out" and k.value() == "Cycles":
        output("out_mul_XYZ", "out_ch_ZXY") # Output FlipAndSwitch 25
        n["t_zbrush_out"].setValue("25")
    elif k.name() == "t_out" and k.value() == "Octane":
        output("out_mul_XYZ", "out_ch_ZXY") # Output FlipAndSwitch 25
        n["t_zbrush_out"].setValue("25")
    elif k.name() == "t_out" and k.value() == "Redshift":
        output("out_mul__XY_Z", "out_ch_ZXY") # Output FlipAndSwitch 30
        n["t_zbrush_out"].setValue("30")
    elif k.name() == "t_out" and k.value() == "V-Ray (Absolute)":
        output("out_mul_XYZ", "out_ch_ZXY") # Output FlipAndSwitch 25
        n["t_zbrush_out"].setValue("25")
    else:
        pass

# Zbrush All Numbers
def zbrush():
    if k.name() == "z_in" and k.value() == 1:
        input("in_ch_XYZ", "in_mul_XYZ") # Input FlipAndSwitch 1
    elif k.name() == "z_in" and k.value() == 2:
        input("in_ch_XYZ", "in_mul_XY_Z") # Input FlipAndSwitch 2
    elif k.name() == "z_in" and k.value() == 3:
        input("in_ch_XYZ", "in_mul_X_YZ") # Input FlipAndSwitch 3
    elif k.name() == "z_in" and k.value() == 4:
        input("in_ch_XYZ", "in_mul_X_Y_Z") # Input FlipAndSwitch 4
    elif k.name() == "z_in" and k.value() == 5:
        input("in_ch_XYZ", "in_mul__XYZ") # Input FlipAndSwitch 5
    elif k.name() == "z_in" and k.value() == 6:
        input("in_ch_XYZ", "in_mul__XY_Z") # Input FlipAndSwitch 6
    elif k.name() == "z_in" and k.value() == 7:
        input("in_ch_XYZ", "in_mul__X_YZ") # Input FlipAndSwitch 7
    elif k.name() == "z_in" and k.value() == 8:
        input("in_ch_XYZ", "in_mul__X_Y_Z") # Input FlipAndSwitch 8
    elif k.name() == "z_in" and k.value() == 9:
        input("in_ch_YXZ", "in_mul_XYZ") # Input FlipAndSwitch 9
    elif k.name() == "z_in" and k.value() == 10:
        input("in_ch_YXZ", "in_mul_XY_Z") # Input FlipAndSwitch 10
    elif k.name() == "z_in" and k.value() == 11:
        input("in_ch_YXZ", "in_mul_X_YZ") # Input FlipAndSwitch 11
    elif k.name() == "z_in" and k.value() == 12:
        input("in_ch_YXZ", "in_mul_X_Y_Z") # Input FlipAndSwitch 12
    elif k.name() == "z_in" and k.value() == 13:
        input("in_ch_YXZ", "in_mul__XYZ") # Input FlipAndSwitch 13
    elif k.name() == "z_in" and k.value() == 14:
        input("in_ch_YXZ", "in_mul__XY_Z") # Input FlipAndSwitch 14
    elif k.name() == "z_in" and k.value() == 15:
        input("in_ch_YXZ", "in_mul__X_YZ") # Input FlipAndSwitch 15
    elif k.name() == "z_in" and k.value() == 16:
        input("in_ch_YXZ", "in_mul__X_Y_Z") # Input FlipAndSwitch 16
    elif k.name() == "z_in" and k.value() == 17:
        input("in_ch_XZY", "in_mul_XYZ") # Input FlipAndSwitch 17
    elif k.name() == "z_in" and k.value() == 18:
        input("in_ch_XZY", "in_mul_XY_Z") # Input FlipAndSwitch 18
    elif k.name() == "z_in" and k.value() == 19:
        input("in_ch_XZY", "in_mul_X_YZ") # Input FlipAndSwitch 19
    elif k.name() == "z_in" and k.value() == 20:
        input("in_ch_XZY", "in_mul_X_Y_Z") # Input FlipAndSwitch 20
    elif k.name() == "z_in" and k.value() == 21:
        input("in_ch_XZY", "in_mul__XYZ") # Input FlipAndSwitch 21
    elif k.name() == "z_in" and k.value() == 22:
        input("in_ch_XZY", "in_mul__XY_Z") # Input FlipAndSwitch 22
    elif k.name() == "z_in" and k.value() == 23:
        input("in_ch_XZY", "in_mul__X_YZ") # Input FlipAndSwitch 23
    elif k.name() == "z_in" and k.value() == 24:
        input("in_ch_XZY", "in_mul__X_Y_Z") # Input FlipAndSwitch 24
    elif k.name() == "z_in" and k.value() == 25:
        input("in_ch_YZX", "in_mul_XYZ") # Input FlipAndSwitch 25
    elif k.name() == "z_in" and k.value() == 26:
        input("in_ch_YZX", "in_mul_XY_Z") # Input FlipAndSwitch 26
    elif k.name() == "z_in" and k.value() == 27:
        input("in_ch_YZX", "in_mul_X_YZ") # Input FlipAndSwitch 27
    elif k.name() == "z_in" and k.value() == 28:
        input("in_ch_YZX", "in_mul_X_Y_Z") # Input FlipAndSwitch 28
    elif k.name() == "z_in" and k.value() == 29:
        input("in_ch_YZX", "in_mul__XYZ") # Input FlipAndSwitch 29
    elif k.name() == "z_in" and k.value() == 30:
        input("in_ch_YZX", "in_mul__XY_Z") # Input FlipAndSwitch 30
    elif k.name() == "z_in" and k.value() == 31:
        input("in_ch_YZX", "in_mul__X_YZ") # Input FlipAndSwitch 31
    elif k.name() == "z_in" and k.value() == 32:
        input("in_ch_YZX", "in_mul__X_Y_Z") # Input FlipAndSwitch 32
    elif k.name() == "z_in" and k.value() == 33:
        input("in_ch_ZXY", "in_mul_XYZ") # Input FlipAndSwitch 33
    elif k.name() == "z_in" and k.value() == 34:
        input("in_ch_ZXY", "in_mul_XY_Z") # Input FlipAndSwitch 34
    elif k.name() == "z_in" and k.value() == 35:
        input("in_ch_ZXY", "in_mul_X_YZ") # Input FlipAndSwitch 35
    elif k.name() == "z_in" and k.value() == 36:
        input("in_ch_ZXY", "in_mul_X_Y_Z") # Input FlipAndSwitch 36
    elif k.name() == "z_in" and k.value() == 37:
        input("in_ch_ZXY", "in_mul__XYZ") # Input FlipAndSwitch 37
    elif k.name() == "z_in" and k.value() == 38:
        input("in_ch_ZXY", "in_mul__XY_Z") # Input FlipAndSwitch 38
    elif k.name() == "z_in" and k.value() == 39:
        input("in_ch_ZXY", "in_mul__X_YZ") # Input FlipAndSwitch 39
    elif k.name() == "z_in" and k.value() == 40:
        input("in_ch_ZXY", "in_mul__X_Y_Z") # Input FlipAndSwitch 40
    elif k.name() == "z_in" and k.value() == 41:
        input("in_ch_ZYX", "in_mul_XYZ") # Input FlipAndSwitch 41
    elif k.name() == "z_in" and k.value() == 42:
        input("in_ch_ZYX", "in_mul_XY_Z") # Input FlipAndSwitch 42
    elif k.name() == "z_in" and k.value() == 43:
        input("in_ch_ZYX", "in_mul_X_YZ") # Input FlipAndSwitch 43
    elif k.name() == "z_in" and k.value() == 44:
        input("in_ch_ZYX", "in_mul_X_Y_Z") # Input FlipAndSwitch 44
    elif k.name() == "z_in" and k.value() == 45:
        input("in_ch_ZYX", "in_mul__XYZ") # Input FlipAndSwitch 45
    elif k.name() == "z_in" and k.value() == 46:
        input("in_ch_ZYX", "in_mul__XY_Z") # Input FlipAndSwitch 46
    elif k.name() == "z_in" and k.value() == 47:
        input("in_ch_ZYX", "in_mul__X_YZ") # Input FlipAndSwitch 47
    elif k.name() == "z_in" and k.value() == 48:
        input("in_ch_ZYX", "in_mul__X_Y_Z") # Input FlipAndSwitch 48
    elif k.name() == "z_out" and k.value() == 1:
        output("out_mul_XYZ", "out_ch_XYZ") # Output FlipAndSwitch 1
    elif k.name() == "z_out" and k.value() == 2:
        output("out_mul_XY_Z", "out_ch_XYZ") # Output FlipAndSwitch 2
    elif k.name() == "z_out" and k.value() == 3:
        output("out_mul_X_YZ", "out_ch_XYZ") # Output FlipAndSwitch 3
    elif k.name() == "z_out" and k.value() == 4:
        output("out_mul_X_Y_Z", "out_ch_XYZ") # Output FlipAndSwitch 4
    elif k.name() == "z_out" and k.value() == 5:
        output("out_mul__XYZ", "out_ch_XYZ") # Output FlipAndSwitch 5
    elif k.name() == "z_out" and k.value() == 6:
        output("out_mul__XY_Z", "out_ch_XYZ") # Output FlipAndSwitch 6
    elif k.name() == "z_out" and k.value() == 7:
        output("out_mul__X_YZ", "out_ch_XYZ") # Output FlipAndSwitch 7
    elif k.name() == "z_out" and k.value() == 8:
        output("out_mul__X_Y_Z", "out_ch_XYZ") # Output FlipAndSwitch 8
    elif k.name() == "z_out" and k.value() == 9:
        output("out_mul_XYZ", "out_ch_YXZ") # Output FlipAndSwitch 9
    elif k.name() == "z_out" and k.value() == 10:
        output("out_mul_XY_Z", "out_ch_YXZ") # Output FlipAndSwitch 10
    elif k.name() == "z_out" and k.value() == 11:
        output("out_mul_X_YZ", "out_ch_YXZ") # Output FlipAndSwitch 11
    elif k.name() == "z_out" and k.value() == 12:
        output("out_mul_X_Y_Z", "out_ch_YXZ") # Output FlipAndSwitch 12
    elif k.name() == "z_out" and k.value() == 13:
        output("out_mul__XYZ", "out_ch_YXZ") # Output FlipAndSwitch 13
    elif k.name() == "z_out" and k.value() == 14:
        output("out_mul__XY_Z", "out_ch_YXZ") # Output FlipAndSwitch 14
    elif k.name() == "z_out" and k.value() == 15:
        output("out_mul__X_YZ", "out_ch_YXZ") # Output FlipAndSwitch 15
    elif k.name() == "z_out" and k.value() == 16:
        output("out_mul__X_Y_Z", "out_ch_YXZ") # Output FlipAndSwitch 16
    elif k.name() == "z_out" and k.value() == 17:
        output("out_mul_XYZ", "out_ch_XZY") # Output FlipAndSwitch 17
    elif k.name() == "z_out" and k.value() == 18:
        output("out_mul_XY_Z", "out_ch_XZY") # Output FlipAndSwitch 18
    elif k.name() == "z_out" and k.value() == 19:
        output("out_mul_X_YZ", "out_ch_XZY") # Output FlipAndSwitch 19
    elif k.name() == "z_out" and k.value() == 20:
        output("out_mul_X_Y_Z", "out_ch_XZY") # Output FlipAndSwitch 20
    elif k.name() == "z_out" and k.value() == 21:
        output("out_mul__XYZ", "out_ch_XZY") # Output FlipAndSwitch 21
    elif k.name() == "z_out" and k.value() == 22:
        output("out_mul__XY_Z", "out_ch_XZY") # Output FlipAndSwitch 22
    elif k.name() == "z_out" and k.value() == 23:
        output("out_mul__X_YZ", "out_ch_XZY") # Output FlipAndSwitch 23
    elif k.name() == "z_out" and k.value() == 24:
        output("out_mul__X_Y_Z", "out_ch_XZY") # Output FlipAndSwitch 24
    elif k.name() == "z_out" and k.value() == 25:
        output("out_mul_XYZ", "out_ch_ZXY") # Output FlipAndSwitch 25
    elif k.name() == "z_out" and k.value() == 26:
        output("out_mul_XY_Z", "out_ch_ZXY") # Output FlipAndSwitch 26
    elif k.name() == "z_out" and k.value() == 27:
        output("out_mul_X_YZ", "out_ch_ZXY") # Output FlipAndSwitch 27
    elif k.name() == "z_out" and k.value() == 28:
        output("out_mul_X_Y_Z", "out_ch_ZXY") # Output FlipAndSwitch 28
    elif k.name() == "z_out" and k.value() == 29:
        output("out_mul__XYZ", "out_ch_ZXY") # Output FlipAndSwitch 29
    elif k.name() == "z_out" and k.value() == 30:
        output("out_mul__XY_Z", "out_ch_ZXY") # Output FlipAndSwitch 30
    elif k.name() == "z_out" and k.value() == 31:
        output("out_mul__X_YZ", "out_ch_ZXY") # Output FlipAndSwitch 31
    elif k.name() == "z_out" and k.value() == 32:
        output("out_mul__X_Y_Z", "out_ch_ZXY") # Output FlipAndSwitch 32
    elif k.name() == "z_out" and k.value() == 33:
        output("out_mul_XYZ", "out_ch_YZX") # Output FlipAndSwitch 33
    elif k.name() == "z_out" and k.value() == 34:
        output("out_mul_XY_Z", "out_ch_YZX") # Output FlipAndSwitch 34
    elif k.name() == "z_out" and k.value() == 35:
        output("out_mul_X_YZ", "out_ch_YZX") # Output FlipAndSwitch 35
    elif k.name() == "z_out" and k.value() == 36:
        output("out_mul_X_Y_Z", "out_ch_YZX") # Output FlipAndSwitch 36
    elif k.name() == "z_out" and k.value() == 37:
        output("out_mul__XYZ", "out_ch_YZX") # Output FlipAndSwitch 37
    elif k.name() == "z_out" and k.value() == 38:
        output("out_mul__XY_Z", "out_ch_YZX") # Output FlipAndSwitch 38
    elif k.name() == "z_out" and k.value() == 39:
        output("out_mul__X_YZ", "out_ch_YZX") # Output FlipAndSwitch 39
    elif k.name() == "z_out" and k.value() == 40:
        output("out_mul__X_Y_Z", "out_ch_YZX") # Output FlipAndSwitch 40
    elif k.name() == "z_out" and k.value() == 41:
        output("out_mul_XYZ", "out_ch_ZYX") # Output FlipAndSwitch 41
    elif k.name() == "z_out" and k.value() == 42:
        output("out_mul_XY_Z", "out_ch_ZYX") # Output FlipAndSwitch 42
    elif k.name() == "z_out" and k.value() == 43:
        output("out_mul_X_YZ", "out_ch_ZYX") # Output FlipAndSwitch 43
    elif k.name() == "z_out" and k.value() == 44:
        output("out_mul_X_Y_Z", "out_ch_ZYX") # Output FlipAndSwitch 44
    elif k.name() == "z_out" and k.value() == 45:
        output("out_mul__XYZ", "out_ch_ZYX") # Output FlipAndSwitch 45
    elif k.name() == "z_out" and k.value() == 46:
        output("out_mul__XY_Z", "out_ch_ZYX") # Output FlipAndSwitch 46
    elif k.name() == "z_out" and k.value() == 47:
        output("out_mul__X_YZ", "out_ch_ZYX") # Output FlipAndSwitch 47
    elif k.name() == "z_out" and k.value() == 48:
        output("out_mul__X_Y_Z", "out_ch_ZYX") # Output FlipAndSwitch 48
    else:
        pass

# World Warning Function
def w_convert():
    if k.name() == "w_in" or k.name() == "w_out":
        if n["w_zbrush_in"].value() == n["w_zbrush_out"].value():
            n["w_convert"].setVisible(True)
            n["t_convert"].setVisible(False)
        elif n["w_zbrush_in"].value() != n["w_zbrush_out"].value():
            n["w_convert"].setVisible(False)
        else:
            pass
    else:
        pass

# Tangent Warning Function
def t_convert():
    if k.name() == "t_in" or k.name() == "t_out":
        if n["t_zbrush_in"].value() == n["t_zbrush_out"].value():
            n["t_convert"].setVisible(True)
            n["w_convert"].setVisible(False)
        elif n["t_zbrush_in"].value() != n["t_zbrush_out"].value():
            n["t_convert"].setVisible(False)
        else:
            pass
    else:
        pass

# Main Function
def main():
    world()
    tangent()
    zbrush()
    w_convert()
    t_convert()
    if n["world_object"].value() == False and n["tangent"].value() == False and n["zbrush"].value() == False:
        w_vis(False)
        t_vis(False)
        z_vis(False)
        n["w_convert"].setVisible(False)
        n["t_convert"].setVisible(False)
        n["line"].setVisible(False)
        clear()
        nuke.toNode("Output").setInput(0, nuke.toNode("Input"))
    elif k.name() == "world_object":
        n["tangent"].setValue(False)
        n["zbrush"].setValue(False)
        w_vis(True)
        t_vis(False)
        z_vis(False)
        n["t_convert"].setVisible(False)
        n["line"].setVisible(True)
        input("in_ch_ZYX", "in_mul__X_YZ") # Input FlipAndSwitch 47
        output("out_mul__X_YZ", "out_ch_ZYX") # Output FlipAndSwitch 47
    elif k.name() == "tangent":
        n["world_object"].setValue(False)
        n["zbrush"].setValue(False)
        t_vis(True)
        w_vis(False)
        z_vis(False)
        n["w_convert"].setVisible(False)
        n["line"].setVisible(True)
        input("in_ch_YZX", "in_mul_XYZ") # Input FlipAndSwitch 25
        output("out_mul_XYZ", "out_ch_ZXY") # Output FlipAndSwitch 25
    elif k.name() == "zbrush":
        n["world_object"].setValue(False)
        n["tangent"].setValue(False)
        z_vis(True)
        w_vis(False)
        t_vis(False)
        n["w_convert"].setVisible(False)
        n["t_convert"].setVisible(False)
        n["line"].setVisible(True)
        input("in_ch_XYZ", "in_mul_XYZ") # Input FlipAndSwitch 1
        output("out_mul_XYZ", "out_ch_XYZ") # Output FlipAndSwitch 1
    else:
        pass

main()

''')
