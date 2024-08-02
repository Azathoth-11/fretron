'''
APROACH: we connect all the points of flight 1 because we will take it as a  reference.

then we go for flight 2 where we start connecting the points. but we need to make sure it doesn't collide with any lines of flight 1.
if it does. we need to make a detour. for that we need to the the coordinates of the line its in conflict with eg. in our case its having a conflict with
flight 1's (2,2) and (3,3) so we need to take the bigger one coordinate value ie.(3,3) make a +1 to its x-coordinate i.e (4,3) now we need to make sure 
that the lower value of flight 2 ie. (2,4) when joining with (4,3) doesn't collide. if it doesn't we connect it with (4,3) and the other remaining one.
Same for flight 3 but here we need to make sure it doesn't collide with flight 2 and keep on increasing the x-coordinate value till it doesn't collide

The reason for choosing shapely is it abstracted the calc. of intersection. found from a stackoverflow discussion.
https://stackoverflow.com/questions/22417842/how-do-i-find-the-intersection-of-two-line-segments

'''







import matplotlib.pyplot as plt
from shapely.geometry import LineString

def check_intersection(line1, line2):
    return LineString(line1).intersects(LineString(line2))

def find_detour_point(point, x_increment=1):
    return (point[0] + x_increment, point[1])

def optimize_flight_paths(flights):
    optimized_flights = [flights[0]]
    
    for flight in flights[1:]:
        optimized_flight = [flight[0]]
        
        for i in range(1, len(flight)):
            current_segment = [optimized_flight[-1], flight[i]]
            
            intersection = False
            for opt_flight in optimized_flights:
                for j in range(len(opt_flight) - 1):
                    if check_intersection(current_segment, opt_flight[j:j+2]):
                        intersection = True
                        detour_point = find_detour_point(opt_flight[-1])
                        
                        while any(check_intersection([detour_point, point], segment) 
                                  for segment in [opt_flight[j:j+2] for opt_flight in optimized_flights]
                                  for point in flight[i:]):
                            detour_point = find_detour_point(detour_point)
                        
                        optimized_flight.append(detour_point)
                        break
                if intersection:
                    break
            
            optimized_flight.append(flight[i])
        
        optimized_flights.append(optimized_flight)
    
    return optimized_flights

def plot_flight_paths(flights):
    colors = ['r', 'g', 'b']
    markers = ['o', 'o', 'o']
    
    plt.figure(figsize=(10, 8))
    for i, flight in enumerate(flights):
        x, y = zip(*flight)
        plt.plot(x, y, color=colors[i], marker=markers[i], linestyle='-', linewidth=2, markersize=8, label=f'Flight {i+1}')
    
    plt.legend()
    plt.xticks(range(0, 6))
    plt.yticks(range(0, 5))
    plt.show()

flights = [
    [(1, 1), (2, 2), (3, 3)],
    [(1, 1), (2, 4), (3, 2)],
    [(1, 1), (4, 2), (3, 4)]
]

optimized_flights = optimize_flight_paths(flights)
plot_flight_paths(optimized_flights)