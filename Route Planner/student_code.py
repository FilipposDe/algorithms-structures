import math
import heapq


def get_inters_distance(coord_1, coord_2):
    return math.sqrt(pow(coord_1[0] - coord_2[0], 2) + pow(coord_1[1] - coord_2[1], 2))


def shortest_path(M, start, goal):
    
    explored = dict()
    curr_inter = start

    # paths items are tuples: ( total path distance including last est. distance to target,
    #                           est. distance to target,
    #                           array with intersections visited in the path )
    start_est_distance = get_inters_distance(M.intersections[start], M.intersections[goal])
    paths = [(0, start_est_distance,[start])]

    # frontier_to_goal has each last inter of a path as keys
    # and their total distances as values
    frontier_to_goal = dict()
    frontier_to_goal[start] = start_est_distance
        
    while True:
        
        # Choose shortest (min) path from paths
        min_path_total_distance, est_distance, min_path = heapq.heappop(paths)
        
        # Subtract previous est_distance (to goal) from path distance 
        # beacause it is included in total distance
        min_path_distance = min_path_total_distance - est_distance

        # Exit if no paths are left to explore
        if min_path is None:
            return None

        # Get the last intersection in min path
        curr_inter = min_path[-1]

        # Exit if smallest path distance leads to goal
        if curr_inter == goal:
            return min_path

        # This intersection is now explored
        explored[curr_inter] = True       
        
        
        
        # Update paths

        curr_inter_roads = M.roads[curr_inter]

        for connected_inter in curr_inter_roads:

            # Continue if road leads to intersection previously
            # explored
            if explored.get(connected_inter) is not None:
                continue
                
            # Create new path tuple
            
            new_path = min_path + [connected_inter]

            distance_to_inter = get_inters_distance(
                M.intersections[curr_inter], M.intersections[connected_inter])
            distance_to_goal = get_inters_distance(
                M.intersections[goal], M.intersections[connected_inter])

            # Total path distance is dependent both on distance to connected
            # intersection, and straight line distance to goal
            new_distance = min_path_distance + distance_to_inter + distance_to_goal
            
            # If the new inter (connected_inter) is the last inter of another
            # path, and it already has a total distance to target smaller
            # than this path, there is no point in adding this path to paths
            if frontier_to_goal.get(connected_inter) is not None:
                if new_distance > frontier_to_goal[connected_inter]:
                    continue
                    
            frontier_to_goal[connected_inter] = new_distance
            
            # Estimated distance to goal is included because it was added to new_distance,
            # it will be subtracted once this path is popped
            new_tuple = (new_distance, distance_to_goal, new_path)
            heapq.heappush(paths, new_tuple)
    
    print("shortest path called")
    return
