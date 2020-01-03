#coding=utf-8
import gtk
import gtk.glade
import webkit

class SettingWidget(gtk.Window):
    def __init__(self):
        super(SettingWidget, self).__init__()
        self.set_default_size(136, 233)
        self.set_position(gtk.WIN_POS_MOUSE)
        menu = gtk.Menu()
        regist = gtk.MenuItem("软件注册")
        mode = gtk.MenuItem("模式设置")
        upgrade = gtk.MenuItem("版本升级")
        doc = gtk.MenuItem("操作手册")
        about = gtk.MenuItem("关于我们")

        menu.append(regist)
        menu.append(mode)
        menu.append(upgrade)
        menu.append(doc)
        menu.append(about)


        vbox = gtk.VBox()
        vbox.pack_start(menu, False, False, 0)
        self.add(vbox)


class Page3Widget:

    def __init__(self):
        self.wTree = gtk.glade.XML("page3.glade")
        self.wid = self.wTree.get_widget("page3box")
        dic = {"on_searchBtn_clicked" : self.page3_searchBtn_clicked,
                "on_addBtn_clicked" : self.page3_addBtn_clicked,
                "on_deleteBtn_clicked" : self.page3_deleteBtn_clicked,
                "on_page3win_destroy" : self.destroy}
        self.wTree.signal_autoconnect(dic)
          
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
    def create_menu(self):
        menu = gtk.Menu()
        menu.set_size_request(136,223)

        regist = gtk.MenuItem("     软件注册")
        regist.set_size_request(136,35)
        mode = gtk.MenuItem("     模式设置")
        mode.set_size_request(136,35)
        upgrade = gtk.MenuItem("     版本升级")
        upgrade.set_size_request(136,35)
        doc = gtk.MenuItem("     操作手册")
        doc.set_size_request(136,35)
        about = gtk.MenuItem("     关于我们")
        about.set_size_request(136,35)

        sep1 = gtk.SeparatorMenuItem()
        sep2 = gtk.SeparatorMenuItem()
        sep3 = gtk.SeparatorMenuItem()
        sep4 = gtk.SeparatorMenuItem()

        menu.append(regist)
        menu.append(sep1)
        menu.append(mode)
        menu.append(sep2)
        menu.append(upgrade)
        menu.append(sep3)
        menu.append(doc)
        menu.append(sep4)
        menu.append(about)


        regpix = gtk.gdk.pixbuf_new_from_file("/home/ymc/test/pygtkgui/resource/titlebar/logo.png")
        regImage = gtk.Image()
        regImage.set_from_pixbuf(regpix)
        #regist.set_image(regImage)

        menu.show_all()
        menu.popup(None, None, None, 3, 0)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_title('MainUI')
        #self.set_keep_above(True)
        self.set_resizable(False)
        self.set_default_size(900, 600)

        mainBox = gtk.VBox();
        titleBarBox = gtk.HBox()
        toolBarBox = gtk.HBox()

        titleEb = gtk.EventBox()
        titleEb.add(titleBarBox)
        titleEb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("#3684d7"))

        toolEb = gtk.EventBox()
        toolEb.add(toolBarBox)
        toolEb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("#3684d7"))

        #tittlebar
        titleLabel = gtk.Label()
        titleLabel.set_size_request(90,32)
        titleLabel.set_markup("<span foreground='white'>安全配置管理</span>")
        userLabel = gtk.Label()
        userLabel.set_size_request(80,32)
        userLabel.set_markup("<span foreground='white'>系统管理员</span>")
        setBtn = gtk.Button()
        setBtn.set_size_request(32,32)
        minBtn = gtk.Button()
        minBtn.set_size_request(32,32)
        closeBtn = gtk.Button()
        closeBtn.set_size_request(32,32)
        #set button background
        setBtn.set_relief(gtk.RELIEF_NONE)  #transparency
        minBtn.set_relief(gtk.RELIEF_NONE)
        closeBtn.set_relief(gtk.RELIEF_NONE)
        #set tittlebar image
        titlepixbuf = gtk.gdk.pixbuf_new_from_file("/home/ymc/test/pygtkgui/resource/titlebar/logo.png")
        titleImage = gtk.Image()
        titleImage.set_from_pixbuf(titlepixbuf)
        titleImageBox = gtk.VBox()
        titleImageBox.pack_start(titleImage)

        headpixbuf = gtk.gdk.pixbuf_new_from_file("/home/ymc/test/pygtkgui/resource/titlebar/ID_USER_TITLEBAR.gif")
        headImage = gtk.Image()
        headImage.set_from_pixbuf(headpixbuf)
        headImageBox = gtk.VBox()
        headImageBox.pack_start(headImage)

        setpixbuf = gtk.gdk.pixbuf_new_from_file("/home/ymc/test/pygtkgui/resource/titlebar/ID_SETTING_TITLEBAR.gif")
        setImage = gtk.Image()
        setImage.set_from_pixbuf(setpixbuf)
        setBtn.add(setImage)

        minpixbuf = gtk.gdk.pixbuf_new_from_file("/home/ymc/test/pygtkgui/resource/titlebar/ID_MIN_TITLEBAR.gif")
        minImage = gtk.Image()
        minImage.set_from_pixbuf(minpixbuf)
        minBtn.add(minImage)

        closepixbuf = gtk.gdk.pixbuf_new_from_file("/home/ymc/test/pygtkgui/resource/titlebar/ID_CLOSED_TITLEBAR.gif")
        closeImage = gtk.Image()
        closeImage.set_from_pixbuf(closepixbuf)
        closeBtn.add(closeImage)

        #toolbar
        homeBtn = gtk.Button()
        homeBtn.set_size_request(84,84)
        stateBtn = gtk.Button()
        stateBtn.set_size_request(84,84)
        softmanagerBtn = gtk.Button()
        softmanagerBtn.set_size_request(84,84)
        auditBtn = gtk.Button()
        auditBtn.set_size_request(84,84)
        sysinfoBtn = gtk.Button()
        sysinfoBtn.set_size_request(84,84)
        #set button background
        homeBtn.set_relief(gtk.RELIEF_NONE)  #transparency
        stateBtn.set_relief(gtk.RELIEF_NONE)
        softmanagerBtn.set_relief(gtk.RELIEF_NONE)
        auditBtn.set_relief(gtk.RELIEF_NONE)
        sysinfoBtn.set_relief(gtk.RELIEF_NONE)
        #set toolbtn image
        homepixbuf = gtk.gdk.pixbuf_new_from_file("/home/ymc/test/pygtkgui/resource/toolbar/ID_HOME_TOOLBAR.png")
        homeImage = gtk.Image()
        #homeImage.set_from_file("/home/ymc/test/pygtkgui/resource/toolbar/ID_HOME_TOOLBAR.png")
        homeImage.set_from_pixbuf(homepixbuf)
        homeBtn.add(homeImage)

        statepixbuf = gtk.gdk.pixbuf_new_from_file("/home/ymc/test/pygtkgui/resource/toolbar/ID_STATE_VIEW_TOOLNAR.png")
        stateImage = gtk.Image()
        stateImage.set_from_pixbuf(statepixbuf)
        stateBtn.add(stateImage)

        softmanagerpixbuf = gtk.gdk.pixbuf_new_from_file("/home/ymc/test/pygtkgui/resource/toolbar/ID_SOFT_MANAGER_TOOLBAR.png")
        softmanagerImage = gtk.Image()
        softmanagerImage.set_from_pixbuf(softmanagerpixbuf)
        softmanagerBtn.add(softmanagerImage)

        auditpixbuf = gtk.gdk.pixbuf_new_from_file("/home/ymc/test/pygtkgui/resource/toolbar/ID_AUDIT_INFO.png")
        auditImage = gtk.Image()
        auditImage.set_from_pixbuf(auditpixbuf)
        auditBtn.add(auditImage)

        sysinfopixbuf = gtk.gdk.pixbuf_new_from_file("/home/ymc/test/pygtkgui/resource/toolbar/ID_BTN_SYSINFO.png")
        sysinfoImage = gtk.Image()
        sysinfoImage.set_from_pixbuf(sysinfopixbuf)
        sysinfoBtn.add(sysinfoImage)
        

        titleBarBox.pack_start(gtk.Alignment(), False, False, 5)
        titleBarBox.pack_start(titleImageBox, expand = False, fill = False, padding = 0)
        titleBarBox.pack_start(titleLabel, expand = False, fill = False, padding = 0)
        titleBarBox.pack_end(closeBtn, expand = False, fill = False, padding = 0)
        titleBarBox.pack_end(minBtn, expand = False, fill = False, padding = 0)
        titleBarBox.pack_end(setBtn, expand = False, fill = False, padding = 0)
        titleBarBox.pack_end(userLabel, expand = False, fill = False, padding = 0)
        titleBarBox.pack_end(headImageBox, expand = False, fill = False, padding = 0)

        setBtn.connect('clicked', self.setBtnClicked)
        minBtn.connect('clicked',self.minBtnClicked)
        closeBtn.connect('clicked', self.closeBtnClicked)

        toolBarBox.pack_start(gtk.Alignment(), False, False, 20)
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
        #barBox.pack_start(titleBarBox)
        #barBox.pack_start(toolBarBox)
        barBox.pack_start(titleEb)
        barBox.pack_start(toolEb)
        barAlign = gtk.Alignment(0, 0, 1, 0)
        barAlign.add(barBox)

        self.box1 = gtk.HBox()
        self.box2 = gtk.HBox()
        self.box3 = gtk.VBox()

        self.notebook = gtk.Notebook()
        self.notebook.set_show_tabs(False)
        self.notebook.set_size_request(900,600 - 32 - 84)

        #book1
        wview1 = webkit.WebView()
        wview1.open('/home/ymc/test/pygtkgui/html/rose_chart.html')
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

    #titlebar slots
    def setBtnClicked(self, setBtn):
        #settingWid = SettingWidget()
        #settingWid.show_all()
        self.create_menu()

    def minBtnClicked(self, minBtn):
        self.maximize()

    def closeBtnClicked(self, closeBtn):
        gtk.main_quit()


    #toolbar slots
    def homeBtnClicked(self, homeBtn):
        self.notebook.set_current_page(0)

    def stateBtnClicked(self, stateBtn):
        self.wview2.load_uri('https://developer.gnome.org/pygtk/stable/index.html')
        self.notebook.set_current_page(1)

    def softmanagerBtnClicked(self, softmanagerBtn):
        self.notebook.set_current_page(2)

    def auditBtnClicked(self, auditBtn):
        self.notebook.set_current_page(3)

    def sysinfoBtnClicked(self, sysinfoBtn):
        self.notebook.set_current_page(4)
   


'''
    def create_menu(self):
        menu = gtk.Menu()

        register = gtk.MenuItem()
        regbuf = gtk.gdk.pixbuf_new_from_file("/home/ymc/test/pygtkgui/resource/titlebar/logo.png")
        regimage = gtk.Image()
        regimage.set_from_pixbuf(regbuf)
        item.set_image(regimage)
        menu.append(item)

        menu.show_all()
        menu_popup(None, None, 3, 0)
'''
if __name__ == "__main__":
    MainWindow()
    gtk.main()

