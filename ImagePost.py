from Post import Post
import matplotlib.pyplot as plt
from PIL import Image


class ImagePost(Post):
    def __init__(self, user, photo):
        super().__init__(user)  # Should be implemented here?
        self.photo = photo    # Holds the text of the post

    def display(self):
        print("\n"+self.photo)
        #image = Image.open(self.photo)
        #plt.imshow(image)
        #plt.axis('off')  # Turn off axis
        #plt.show()

    def __str__(self):
        return f"{self.uploader.name} posted a picture\n"
