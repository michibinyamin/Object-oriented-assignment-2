from Post import Post


class TextPost(Post):
    def __init__(self, user, text):
        super().__init__(user)  # Should be implemented here?
        self.text = text    # Holds the text of the post

    def __str__(self):
        return f'{self.uploader.name} published a post:\n"{self.text}"\n'
