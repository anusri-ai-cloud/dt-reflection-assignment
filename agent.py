import json

with open("reflection-tree.json") as f:
    tree = {node["id"]: node for node in json.load(f)}

current = "START"
answers = {}

while True:
    node = tree[current]

    print("\n" + node["text"])

    if node["type"] == "question":
        for i, option in enumerate(node["options"]):
            print(f"{i+1}. {option}")

        choice = int(input("Choose option: ")) - 1
        selected = node["options"][choice]
        answers[current] = selected

        # Move to decision node
        next_node = node["next"]
        decision = tree[next_node]

        current = decision["rules"][selected]

    elif node["type"] == "decision":
        # Skip (handled above)
        pass

    elif node["type"] in ["reflection", "bridge", "summary"]:
        input("\nPress Enter to continue...")
        current = node["next"]

    elif node["type"] == "start":
        current = node["next"]

    elif node["type"] == "end":
        print("\nSession complete.")
        break
