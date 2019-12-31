import gtk
import gtk.glade
import webkit

class Page3Widget:

        def __init__(self):
            self.wTree = gtk.glade.XML("page3.glade")
            self.wid = self.wTree.get_widget("page3box")
            dic = {"on_searchBtn_clicked" : self.page3_searchBtn_clicked,
                    "on_addBtn_clicked" : self.page3_addBtn_clicked,
                    "on_deleteBtn_clicked" : self.page3_deleteBtn_clicked,
                    "on_page3win_destroy" : self.destroy}
            self.wTree.signal_autoconnect(dic)
          
        #    self.window.show()
        #    gtk.main()

        #page3 slot    
        def page3_searchBtn_clicked(self, widget):
            print "page3_searchBtn_clicked"

        def page3_addBtn_clicked(self, widget):
            print "page3_addBtn_clicked"

        def page3_deleteBtn_clicked(self, widget):
            print "page3_deleteBtn_clicked"

        def destroy(self, widget):
            gtk.main_quit()
        #end page3 slot

class MainWindow(gtk.Window):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_title('MainUI')
        #self.set_keep_above(True)
        self.set_resizable(False)
        self.set_default_size(900, 600)

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
        setBtn = gtk.Button("v")
        setBtn.set_size_request(32,32)
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
        titleBarBox.pack_end(closeBtn, expand = False, fill = False, padding = 0)
        titleBarBox.pack_end(miniBtn, expand = False, fill = False, padding = 0)
        titleBarBox.pack_end(setBtn, expand = False, fill = False, padding = 0)
        titleBarBox.pack_end(userLabel, expand = False, fill = False, padding = 0)
        titleBarBox.pack_end(headPixmapLabel, expand = False, fill = False, padding = 0)

        toolBarBox.pack_start(homeBtn, expand = False, fill = False, padding = 0)
        toolBarBox.pack_start(stateBtn, expand = False, fill = False, padding = 0)
        toolBarBox.pack_start(softmanagerBtn, expand = False, fill = False, padding = 0)
        toolBarBox.pack_start(auditBtn, expand = False, fill = False, padding = 0)
        toolBarBox.pack_start(sysinfoBtn, expand = False, fill = False, padding = 0)

        homeBtn.connect('clicked', self.homeBtnClicked)
        stateBtn.connect('clicked',self.stateBtnClicked)
        softmanagerBtn.connect('clicked', self.softmanagerBtnClicked)
        auditBtn.connect('clicked', self.auditBtnClicked)
        sysinfoBtn.connect('clicked', self.sysinfoBtnClicked)

        '''
        #book3
        self.page3gladefile = "page3.glade"
        self.page3tree = gtk.glade.XML(self.page3gladefile)
        self.wid = self.page3tree.get_widget("page3win")
        dic = {"on_searchBtn_clicked" : self.page3_searchBtn_clicked,
                "on_addBtn_clicked" : self.page3_addBtn_clicked,
                "on_deleteBtn_clicked" : self.page3_deleteBtn_clicked,                
                }
        self.page3tree.signal_autoconnect(dic)
        '''
        

        barBox = gtk.VBox()
        barBox.pack_start(titleBarBox)
        barBox.pack_start(toolBarBox)
        barAlign = gtk.Alignment(0, 0, 1, 0)
        barAlign.add(barBox)

        self.box1 = gtk.HBox()
        self.box2 = gtk.HBox()
        self.box3 = gtk.VBox()

        self.notebook = gtk.Notebook()
        self.notebook.set_show_tabs(False)
        self.notebook.set_size_request(900,600 - 32 - 64)

        #book1
        wview1 = webkit.WebView()
        wview1.open('/home/ymc/test/pygtktest/html/rose_chart.html')
        self.box1.add(wview1)
        self.notebook.append_page(self.box1)

        #book2
        self.wview2 = webkit.WebView()
        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        sw.add_with_viewport(self.wview2)
        self.box2.add(sw)
        self.notebook.append_page(self.box2)
        
        '''
        #book3
        self.page3gladefile = "page3.glade"
        self.page3tree = gtk.glade.XML(self.page3gladefile)
        self.wid = self.page3tree.get_widget("page3win")
        dic = {"on_searchBtn_clicked" : self.page3_searchBtn_clicked,
                "on_addBtn_clicked" : self.page3_addBtn_clicked,
                "on_deleteBtn_clicked" : self.page3_deleteBtn_clicked,                
                }
        self.page3tree.signal_autoconnect(dic)
        self.wid.set_size_request(900, 30)
        self.box3.add(self.wid)
        self.notebook.append_page(self.box3)
        '''
        page3Widget = Page3Widget()
        wid = page3Widget.wid
        page3Align = gtk.Alignment(0, 0, 1, 0)
        page3Align.add(wid)
        self.box3.add(page3Align)
        self.notebook.append_page(self.box3)

        page4Label = gtk.Label('This is Page 4')
        page5Label = gtk.Label('This is Page 5')
        self.notebook.append_page(page4Label)
        self.notebook.append_page(page5Label)

        mainBox.add(barAlign)
        mainBox.add(self.notebook)
       
        self.connect("destroy",gtk.main_quit)
        self.add(mainBox)
        self.show_all()

    def homeBtnClicked(self, homeBtn):
        self.notebook.set_current_page(0)

    def stateBtnClicked(self, stateBtn):
        self.wview2.load_uri('https://www.baidu.com')
        self.notebook.set_current_page(1)

    def softmanagerBtnClicked(self, softmanagerBtn):
        self.notebook.set_current_page(2)

    def auditBtnClicked(self, auditBtn):
        self.notebook.set_current_page(3)

    def sysinfoBtnClicked(self, sysinfoBtn):
        self.notebook.set_current_page(4)
    

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
