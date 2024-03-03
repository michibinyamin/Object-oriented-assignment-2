from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password
        self.__online = True   # When is the user online (initially online)
        self.following = []  # Keep track of who user is following
        self.followers = []  # Keep track of user followers
        self.notifications = []  # Keep track of notifications(holds strings only?)
        self.number_of_posts = 0

    def set_online(self, online):  # Set online \ offline
        self.__online = online

    def is_online(self):        # Get online \ offline
        return self.__online

    def follow(self, user):  # Follow a user
        if self.is_online():    # User can only edit if online
            self.following.append(user)
            user.__add_follower(self)
            print(f"{self.name} started following {user.name}")
        else:
            print("You are offline")

    def unfollow(self, user):
        if self.is_online():  # User can only edit if online
            if user in self.following:
                self.following.remove(user)     # Remove following(stop following
                user.__remove_follower(self)    # Remove from user the follower
                print(f"{self.name} unfollowed {user.name}")    # Print
            else:
                print("You are not following this user.")
        else:
            print("You are offline")

    def publish_post(self, t, cont, *args):     # Using factory design pattern to create the chosen object(post)
        if self.is_online():  # User can only post if online
            if t == "Text":
                post = TextPost(self, cont)
            elif t == "Image":
                post = ImagePost(self, cont)
            elif t == "Sale":
                post = SalePost(self, cont, args[0], args[1])
            else:
                print("No such post type")
                return None

            self.number_of_posts = self.number_of_posts + 1
            self.__notify_followers()   # Notify all the users followers (with Observer design pattern)
            print(post)  # Print the post
            return post     # Return the Chosen post
        else:
            print("You are offline")

    # Implementing Observer design pattern to update all
    # the users followers that post has been uploaded
    def __notify_followers(self):
        for u in self.followers:
            u.notify(f"{self.name} has a new post")

    def __add_follower(self, user):
        self.followers.append(user)

    def __remove_follower(self, user):
        self.followers.remove(user)

    def notify(self, update):   # Get a notification
        self.notifications.append(update)   # Add notification to list

    def print_notifications(self):
        print(f"{self.name}'s notifications:")
        for update in self.notifications:
            print(update)

    def __str__(self):
        return f"User name: {self.name}, Number of posts: {self.number_of_posts}, Number of followers: {len(self.followers)}"   # Print user

    def get_password(self):  # Returns the user password
        return self.__password


