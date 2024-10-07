import heapq

class Network:
    def __init__(self):
        self.connections = {}

    def add_connection(self, start_node, end_node, weight):
        if start_node not in self.connections:
            self.connections[start_node] = []
        self.connections[start_node].append((end_node, weight))

    def dijkstra_algorithm(self, start):
        shortest_distances = {start: (None, 0)}
        priority_queue = [(0, start)]
        heapq.heapify(priority_queue)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > shortest_distances[current_node][1]:
                continue

            for neighbor, weight in self.connections.get(current_node, []):
                distance = current_distance + weight
                if neighbor not in shortest_distances or distance < shortest_distances[neighbor][1]:
                    shortest_distances[neighbor] = (current_node, distance)
                    heapq.heappush(priority_queue, (distance, neighbor))

        return shortest_distances

# Example usage
network = Network()
network.add_connection('A', 'B', 1)
network.add_connection('B', 'C', 2)
network.add_connection('A', 'C', 4)
network.add_connection('C', 'D', 1)

shortest_distances = network.dijkstra_algorithm('A')
print(shortest_distances)