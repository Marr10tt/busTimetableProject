import tkinter
import tkinter.ttk
from tkintermapview import TkinterMapView

windowWidth = 100
windowHeight = 100
Location = "Doncaster, England"

def generate():
    map_widget = TkinterMapView(width=windowWidth, height=windowHeight, corner_radius=0)
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    map_widget.set_address(Location, marker=True)
    map_widget.place(relx=0.2, rely=0.53)