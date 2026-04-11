import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]]

copied_classes = copy.deepcopy(classes)

classes[0][1][0] = 99   

print("Original:", classes)
print("Copied:", copied_classes)
