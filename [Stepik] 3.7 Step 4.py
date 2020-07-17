stepCount = int(input())
directions = []
coord = {'x' : 0, 'y' : 0}
for i in range(stepCount):
    direction = input().split()
    directions.append({direction[0]: int(direction[1])})
for direction in directions:
    if list(direction.keys())[0] == 'восток':
        coord['x'] += direction.get('восток')
    elif list(direction.keys())[0] == 'запад':
        coord['x'] -= direction.get('запад')
    elif list(direction.keys())[0] == 'север':
        coord['y'] += direction.get('север')
    elif list(direction.keys())[0] == 'юг':
        coord['y'] -= direction.get('юг')
[print(i,end=' ') for i in list(coord.values())]