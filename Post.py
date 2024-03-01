

class Post:
    def __init__(self, user):
        self.likes = []  # List of users who liked
        self.comments = []  # List of users + there comment
        self.uploader = user   # The user which uploaded the post

    def like(self, user):
        if user.is_online() and user not in self.likes:
            self.likes.append(user)
            if user is not self.uploader:   # Don't get notified from the uploader himself
                self.uploader.notify(f"{user.name} liked your post")
                print(f"notification to {self.uploader.name}: {user.name} liked your post")

        else:
            print("You are offline")

    def comment(self, user, comment):
        if user.is_online() and user not in self.comments:
            self.comments.append((user, comment))
            if user is not self.uploader:  # Don't get notified from the uploader himself
                self.uploader.notify(f"{user.name} commented on your post")
                print(f"notification to {self.uploader.name}: {user.name} commented on your post: {comment}")

        else:
            print("You are offline")
