from gi.repository import Gtk, Gdk, Gio, GdkPixbuf, Pango, GObject

import TreeViewFrame
import QueryViewFrame
import SelectedNodesFrame

import LfsController

def pathlist(path):
  return [node for node in path.split('/') if node != ""]

class ThreePaned(Gtk.Paned):
  def __init__(self):
    Gtk.Paned.__init__(self)
    
    self.Pane2 = Gtk.Paned()
    self.pack1(self.Pane2,0,0)
    self.get_style_context().add_class("three-paned")    

  def add_left(self,child):
    self.get_child1().pack1(child,0,0)
    
  def add_center(self,child):
    self.get_child1().pack2(child,1,0)
    
  def add_right(self,child):
    self.pack2(child,0,0)

class Window(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title="Labels")
    provider = Gtk.CssProvider();
    provider.load_from_path("/home/gerard/labelfs/labels/gtk-style.css");
    
    Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider, 600);

    self.get_style_context().add_class("window")    
    
    self.set_default_size(600,400)
        
    self.three_paned = ThreePaned()
    self.add(self.three_paned)

    self.tree_view_frame = TreeViewFrame.TreeViewFrame()
    self.three_paned.add_left(self.tree_view_frame)

    self.query_view_frame = QueryViewFrame.QueryViewFrame()
    self.three_paned.add_center(self.query_view_frame)

    #self.selected_node_frame = SelectedNodeFrame.SelectedNodeFrame()
    #self.three_paned.add_right(self.selected_node_frame)
        
    self.set_focus(self.query_view_frame.icon_view)

    self.connect("delete-event", Gtk.main_quit)

    self.show_all()
