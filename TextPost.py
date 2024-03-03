from Post import Post


# Objects created with Factory design pattern in user when chosen to create textpost object
class TextPost(Post):
    def __init__(self, user, text):
        super().__init__(user)  # Initialize user
        self.text = text    # Holds the text of the post

    def __str__(self):
        return f'{self.uploader.name} published a post:\n"{self.text}"\n'
