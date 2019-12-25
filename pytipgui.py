import gtk
import webkit
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainWindow(gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
 #       window = gtk.Window()
        self.set_title('MainUI')
        self.set_keep_above(True)
        self.set_default_size(600, 480)

#       titleBarFixed = gtk.Fixed();
#       toolBarFixed = gtk.Fixed();

        mainBox = gtk.VBox();
        titleBarBox = gtk.HBox()
        toolBarBox = gtk.HBox()

        #tittlebar
        titlePixmapLabel = gtk.Label("Logo")
        titlePixmapLabel.set_size_request(32,32)
        titleLabel = gtk.Label("safemanager")
        titleLabel.set_size_request(100,32)
        headPixmapLabel = gtk.Label("Head")
        headPixmapLabel.set_size_request(32,32)
        userLabel = gtk.Label("sysuser")
        userLabel.set_size_request(100,32)
        miniBtn = gtk.Button("-")
        miniBtn.set_size_request(32,32)
        closeBtn = gtk.Button("X")
        closeBtn.set_size_request(32,32)

        #toolbar
        homeBtn = gtk.Button("home")
        homeBtn.set_size_request(64,64)
        stateBtn = gtk.Button("state")
        stateBtn.set_size_request(64,64)
        softmanagerBtn = gtk.Button("softmanager")
        softmanagerBtn.set_size_request(64,64)
        auditBtn = gtk.Button("audit")
        auditBtn.set_size_request(64,64)
        sysinfoBtn = gtk.Button("sysinfo")
        sysinfoBtn.set_size_request(64,64)
       
        titleBarBox.pack_start(titlePixmapLabel, expand = False, fill = False, padding = 0)
        titleBarBox.pack_start(titleLabel, expand = False, fill = False, padding = 0)
        titleBarBox.pack_start(headPixmapLabel, expand = False, fill = False, padding = 0)
        titleBarBox.pack_end(closeBtn, expand = False, fill = False, padding = 0)
        titleBarBox.pack_end(miniBtn, expand = False, fill = False, padding = 0)
        titleBarBox.pack_end(userLabel, expand = False, fill = False, padding = 0)

#        titleBarAlign = gtk.Alignment(0, 0, 1, 0)
 #       titleBarAlign.add(titleBarBox)

        toolBarBox.add(homeBtn)
        toolBarBox.add(stateBtn)
        toolBarBox.add(softmanagerBtn)
        toolBarBox.add(auditBtn)
        toolBarBox.add(sysinfoBtn)

#       toolBarAlign = gtk.Alignment(0, 0, 1, 0)
#       toolBarAlign.add(toolBarBox)

        barVBox = gtk.VBox()
#        barVBox.add(titleBarBox)
#        barVBox.add(toolBarBox)

        barAlign = gtk.Alignment(0, 0, 1, 0)
#        barAlign.add(barVBox)
      #  homeFixed = gtk.Fixed()
      #  homeFixed.set_size_request(600, 300);
        wview = webkit.WebView()
        #wview.load_uri('https://www.baidu.com')
        wview.open('/home/ymc/test/pygtktest/html/rose_chart.html')

#        mainBox.add(barAlign)
#        mainBox.pack_start(toolBarBox)
#        mainBox.pack_end(wview)

        mainBox.add(titleBarBox)
        mainBox.add(toolBarBox)
        mainBox.add(wview)
        
        self.add(mainBox)
        self.show_all()
if __name__ == "__main__":
    MainWindow()
    gtk.main()


'''      
        toolBarBox.pack_start(homeBtn, expand = False, fill = False, padding = 0)
        toolBarBox.pack_start(stateBtn, expand = False, fill = False, padding = 0)
        toolBarBox.pack_start(softmanagerBtn, expand = False, fill = False, padding = 0)
        toolBarBox.pack_start(auditBtn, expand = False, fill = False, padding = 0)
        toolBarBox.pack_start(sysinfoBtn, expand = False, fill = False, padding = 0)
'''

      #  homeFixed = gtk.Fixed()
      #  homeFixed.set_size_request(600, 300);
'''
        self.wview = webkit.WebView()
        #self.wview.load_uri('https://www.baidu.com')
        #self.wview.open('/home/ymc/test/pygtktest/html/baidu.html')
        self.wview.open('/home/ymc/test/pygtktest/html/rose_chart.html')

        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.add(self.wview)
        window.add(scrolled_window)
'''
#        self.connect('destroy', gtk.main_quit)
