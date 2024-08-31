#  ColorSpaceTransform.py
#  Version: 1.0
#  Author: Erjon Sadiku

#--------------------------------

import nuke
import nukescripts

class InputTransformPanel(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, "ColorSpace Transform")
        self.transforms = self.get_input_transforms()
        self.transform_knob = nuke.Enumeration_Knob('ColorSpace ', 'Input Transform', self.transforms)
        self.addKnob(self.transform_knob)

        self.addKnob(nuke.Text_Knob('', '', ''))
        self.name_label = nuke.Text_Knob('', 'ColorSpace Transform ', 'by Erjon Sadiku')
        self.addKnob(self.name_label)        
        self.addKnob(nuke.Text_Knob('', '', ''))

    def get_input_transforms(self):      
        dummy_node = nuke.createNode("Read", inpanel=False)
        transforms = nuke.getColorspaceList(dummy_node['colorspace'])
        nuke.delete(dummy_node)
        return transforms

    def get_selected_transform(self):     
        if self.showModalDialog():
            return self.transform_knob.value()
        return None

def apply_input_transform_to_nodes(nodes):
    panel = InputTransformPanel()
    selected_transform = panel.get_selected_transform()
    if selected_transform:
        for node in nodes:
            if node.Class() == 'Read' and node.knob('colorspace'):
                node['colorspace'].setValue(selected_transform)

def apply_input_transform_to_selected():    
    nodes = nuke.selectedNodes()
    apply_input_transform_to_nodes(nodes)

def apply_input_transform_to_all():   
    nodes = nuke.allNodes('Read')
    apply_input_transform_to_nodes(nodes)

