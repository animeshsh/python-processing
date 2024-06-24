import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from PIL import Image

class BatchCropApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Batch Crop Images")

        self.label1 = Label(root, text="Crop Area (x, y, width, height):")
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.entry = Entry(root)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        self.select_button = Button(root, text="Select Folder", command=self.select_folder)
        self.select_button.grid(row=1, column=0, padx=10, pady=10)

        self.crop_button = Button(root, text="Crop Images", command=self.crop_images)
        self.crop_button.grid(row=1, column=1, padx=10, pady=10)

        self.folder_path = ""

    def select_folder(self):
        self.folder_path = filedialog.askdirectory(title="Select Folder Containing Images")
        if self.folder_path:
            messagebox.showinfo("Selected Folder", f"Selected folder: {self.folder_path}")
        else:
            messagebox.showwarning("No Selection", "No folder selected.")

    def crop_images(self):
        if not self.folder_path:
            messagebox.showwarning("No Folder", "Please select a folder first.")
            return

        try:
            crop_values = list(map(int, self.entry.get().split(',')))
            if len(crop_values) != 4:
                raise ValueError("Please enter four values for the crop area.")

            x, y, width, height = crop_values
            output_dir = filedialog.askdirectory(title="Select Output Directory")
            if not output_dir:
                return

            for filename in os.listdir(self.folder_path):
                if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                    img_path = os.path.join(self.folder_path, filename)
                    img = Image.open(img_path)
                    cropped_img = img.crop((x, y, x + width, y + height))
                    cropped_img.save(os.path.join(output_dir, filename))

            messagebox.showinfo("Success", "Images cropped successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = Tk()
    app = BatchCropApp(root)
    root.mainloop()

