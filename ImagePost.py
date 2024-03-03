from Post import Post
import matplotlib.pyplot as plt
from PIL import Image


# Objects created with Factory design pattern in user when chosen to create imagepost object
class ImagePost(Post):
    def __init__(self, user, photo):
        super().__init__(user)  # Should be implemented here?
        self.photo = photo    # Holds the text of the post

    #def display(self):
        #print("\n"+self.photo)
        #image = Image.open(self.photo)
        #plt.imshow(image)
        #plt.axis('off')  # Turn off axis
        #plt.show()
    def display(self):
        print("Shows picture")
        try:
            # Display image
            img_matplotlib = plt.imread(self.photo)
            plt.imshow(img_matplotlib)
            plt.axis('off')
            plt.show()

            # Displaying image using Pillow
            img_pillow = Image.open(self.photo)
            img_pillow.show()
            return "Displayed an image."

        except FileNotFoundError:
            return "Failed to display image."

    def __str__(self):
        return f"{self.uploader.name} posted a picture\n"
