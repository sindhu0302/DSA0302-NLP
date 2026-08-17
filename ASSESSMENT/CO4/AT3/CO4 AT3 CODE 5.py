# Transition-Based vs Graph-Based Parsing

print("Transition-Based Parsing:")
print("- Builds dependency tree step by step")
print("- Uses local decisions")
print("- Very fast")
print("- Suitable for large datasets")

print("\nGraph-Based Parsing:")
print("- Creates possible dependency relationships")
print("- Finds the best complete tree")
print("- Usually more computationally expensive")
print("- Can provide globally better decisions")

# Simple performance comparison
transition_time = 3
graph_time = 8

print("\nExample Processing Time:")
print("Transition-Based:", transition_time, "ms")
print("Graph-Based:", graph_time, "ms")

if transition_time < graph_time:
    print("\nTransition-based parsing is faster.")

print("\nConclusion:")
print("Transition-based parsing is more suitable for large-scale applications")
print("because it is fast and requires less computation.")
