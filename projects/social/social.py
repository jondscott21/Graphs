import random

from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(i + 1)
        
        total = avg_friendships * num_users
        max_friends = avg_friendships * 2
        # Create friendships
        while total > 0:
            user1 = random.randint(1, num_users)
            user2 = random.randint(1, num_users)
            if user2 not in self.friendships[user1]:
                if len(self.friendships[user1]) < max_friends and len(self.friendships[user2]) < max_friends:
                    self.add_friendship(user1, user2)
                    total -= 2
            

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        queue = Queue()
        queue.enqueue([user_id])
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        while queue.size() > 0:
            path = queue.dequeue()
            cur_user = path[-1]
            if not cur_user in visited:
                visited[cur_user] = path
                for friend in self.friendships[cur_user]:
                    new_path = list(path)
                    new_path.append(friend)
                    queue.enqueue(new_path)


        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    for i in sg.users:
        print(i)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
