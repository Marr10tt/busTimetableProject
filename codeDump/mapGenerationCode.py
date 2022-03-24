import tkinter
import tkinter.ttk
from tkintermapview import TkinterMapView

#empty template variables
windowWidth = 0
windowHeight = 0
Location = ""

#configures settings for map height, width, and displayed location
def mapSettings(width, height, location):
    global windowWidth
    global windowHeight
    global Location
    windowWidth = width
    windowHeight = height
    Location = location

#generates the actual map selecting source, location, and places the map
def generate(pageName):

    map_widget = TkinterMapView(pageName, width=windowWidth, height=windowHeight, corner_radius=0)
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google normal
    map_widget.set_address(Location, marker=True)
    map_widget.place(relx=0.2, rely=0.53, anchor=tkinter.CENTER)