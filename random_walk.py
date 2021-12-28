from random import choice

class RandomWalk():
    """Generates Random Walks"""
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        #All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]


    def get_step(self):
        #Decide which direction to go and how far to go in that direction.
        direction = choice([1, -1])
        distance = choice([0,1,2,3,4])
        step = direction * distance
        
        return step

              
    def fill_walk(self):
            while len(self.x_values) < self.num_points:
                """Calculate all the points in a walk"""
                #Keep taking steps until the walk reaches the desired length
                x_step = self.get_step()
                y_step = self.get_step()

                if x_step == 0 and y_step == 0:
                    continue

                next_x = self.x_values[-1] + x_step
                next_y = self.y_values[-1] + y_step

                self.x_values.append(next_x)
                self.y_values.append(next_y)
    


    # def fill_walk(self):
    #     """Calculate all the points in a walk"""
    #     #Keep taking steps until the walk reaches the desired length
    #     while len(self.x_values) < self.num_points:
    #         #Decide which direction to go and how far to go in that direction.
    #         x_direction = choice([1, -1])
    #         x_distance = choice([0,1,2,3,4])
    #         x_step = x_direction * x_distance

    #         y_direction = choice([1, -1])
    #         y_distance = choice([0,1,2,3,4])
    #         y_step = y_direction * y_distance

    #         #Reject null moves
    #         if x_step == 0 and y_step == 0:
    #             continue

    #         next_x = self.x_values[-1] + x_step
    #         next_y = self.y_values[-1] + y_step

    #         self.x_values.append(next_x)
    #         self.y_values.append(next_y)
    
