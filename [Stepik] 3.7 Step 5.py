text = []
with open('dataset_3380_5.txt', 'r', encoding='utf-8') as f:
    for line in f:
        text.append(line.strip().split())
classes = {str(numClass): '' for numClass in range(1,12)}
for line in text:
    classes[line[0]] = []
for line in text:
    classes[line[0]].append(int(line[2]))
for key, value in classes.items():
    print(f"{key} {sum(value) / len(value) if len(value) > 0 else '-'}")