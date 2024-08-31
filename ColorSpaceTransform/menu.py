import nuke

def add_to_menu():
    menubar = nuke.menu("Nuke")
    global custom_menu
    custom_menu = menubar.addMenu("&ColorSpace Transform")
    add_input_transform_commands_to_menu()


def add_input_transform_commands_to_menu():
    from ColorSpaceTransform import apply_input_transform_to_all, apply_input_transform_to_selected
    custom_menu.addCommand('All ReadNode', apply_input_transform_to_all)
    custom_menu.addCommand('Selected ReadNode', apply_input_transform_to_selected)

if __name__ == "__main__":
    add_to_menu()
