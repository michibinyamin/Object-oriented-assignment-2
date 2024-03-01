from Post import Post


class ImagePost(Post):
    def __init__(self, user, photo):
        super().__init__(user)  # Should be implemented here?
        self.photo = photo    # Holds the text of the post

    def display(self):
        print("\n"+self.photo)

    def __str__(self):
        return f"{self.uploader.name} posted a picture\n"
