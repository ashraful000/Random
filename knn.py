from math import sqrt


def ed(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)


def get_neighbours(train, test_row, num_neighbours):
    distances = list()
    for train_row in train:
        dist = ed(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbours = list()
    for i in range(num_neighbours):
        neighbours.append(distances[i][0])
    return neighbours

def predict(train, test_row, num_neighbours):
    neighbours = get_neighbours(train, test_row, num_neighbours)
    output_values = [row[-1] for row in neighbours]
    prediction = max(set(output_values), key=output_values.count)
    return prediction


dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]

prediction = predict(dataset, dataset[0], 3)
print(prediction)
