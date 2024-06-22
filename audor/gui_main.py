import wx
import subprocess

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 200))
        
        panel = wx.Panel(self)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.file_picker = wx.FilePickerCtrl(panel, message="Select a file")
        self.vbox.Add(self.file_picker, flag=wx.EXPAND|wx.ALL, border=10)
        
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.small_button = wx.Button(panel, label='Small')
        self.medium_button = wx.Button(panel, label='Medium')
        self.large_button = wx.Button(panel, label='Large')
        
        self.hbox.Add(self.small_button, flag=wx.RIGHT, border=10)
        self.hbox.Add(self.medium_button, flag=wx.RIGHT, border=10)
        self.hbox.Add(self.large_button, flag=wx.RIGHT, border=10)
        
        self.vbox.Add(self.hbox, flag=wx.ALIGN_CENTER|wx.ALL, border=10)
        
        panel.SetSizer(self.vbox)
        
        self.small_button.Hide()
        self.medium_button.Hide()
        self.large_button.Hide()
        
        self.small_button.Bind(wx.EVT_BUTTON, self.on_size_selected)
        self.medium_button.Bind(wx.EVT_BUTTON, self.on_size_selected)
        self.large_button.Bind(wx.EVT_BUTTON, self.on_size_selected)
        
        self.file_picker.Bind(wx.EVT_FILEPICKER_CHANGED, self.on_file_selected)
        
        self.selected_file_path = None

    def on_file_selected(self, event):
        self.selected_file_path = self.file_picker.GetPath()
        if self.selected_file_path:
            self.small_button.Show()
            self.medium_button.Show()
            self.large_button.Show()
            self.vbox.Layout()
    
    def on_size_selected(self, event):
        file_path = self.selected_file_path
        model_size = event.GetEventObject().GetLabel().upper()
        
        if file_path:
            subprocess.run(['python', 'audor/detect.py', file_path, model_size])
        

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title='Audor')
        frame.Show()
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()