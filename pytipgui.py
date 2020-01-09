#coding=utf-8
import gtk
import gtk.glade
import webkit
import logging
import logging.handlers


class Page3Widget:

    def __init__(self):
        self.wTree = gtk.glade.XML("page3.glade")
        self.wid = self.wTree.get_widget("page3box")
        dic = {"on_searchBtn_clicked" : self.page3_searchBtn_clicked,
                "on_addBtn_clicked" : self.page3_addBtn_clicked,
                "on_deleteBtn_clicked" : self.page3_deleteBtn_clicked,
                "on_page3win_destroy" : self.destroy}
        self.wTree.signal_autoconnect(dic)

    def page3_searchBtn_clicked(self, widget):
        print "page3_searchBtn_clicked"

    def page3_addBtn_clicked(self, widget):
        print "page3_addBtn_clicked"

    def page3_deleteBtn_clicked(self, widget):
        print "page3_deleteBtn_clicked"

    def destroy(self, widget):
        gtk.main_quit()

class TitleBarWidget:
    def __init__(self):
        self.titleBarBox = gtk.HBox()

        titleLabel = gtk.Label()
        titleLabel.set_size_request(90,32)
        titleLabel.set_markup("<span foreground='white'>安全配置管理</span>")
        userLabel = gtk.Label()
        userLabel.set_size_request(80,32)
        userLabel.set_markup("<span foreground='white'>系统管理员</span>")
        self.setBtn = gtk.Button()
        self.setBtn.set_size_request(32,32)
        self.minBtn = gtk.Button()
        self.minBtn.set_size_request(32,32)
        self.closeBtn = gtk.Button()
        self.closeBtn.set_size_request(32,32)

        #set button transparency
        self.setBtn.set_relief(gtk.RELIEF_NONE)
        self.minBtn.set_relief(gtk.RELIEF_NONE)
        self.closeBtn.set_relief(gtk.RELIEF_NONE)

        #set tittlebar image
        titlepixbuf = gtk.gdk.pixbuf_new_from_file("resource/titlebar/logo.png")
        titleImage = gtk.Image()
        titleImage.set_from_pixbuf(titlepixbuf)
        titleImageBox = gtk.VBox()
        titleImageBox.pack_start(titleImage)

        headpixbuf = gtk.gdk.pixbuf_new_from_file("resource/titlebar/ID_USER_TITLEBAR.gif")
        headImage = gtk.Image()
        headImage.set_from_pixbuf(headpixbuf)
        headImageBox = gtk.VBox()
        headImageBox.pack_start(headImage)

        setpixbuf = gtk.gdk.pixbuf_new_from_file("resource/titlebar/ID_SETTING_TITLEBAR.gif")
        setImage = gtk.Image()
        setImage.set_from_pixbuf(setpixbuf)
        self.setBtn.add(setImage)

        minpixbuf = gtk.gdk.pixbuf_new_from_file("resource/titlebar/ID_MIN_TITLEBAR.gif")
        minImage = gtk.Image()
        minImage.set_from_pixbuf(minpixbuf)
        self.minBtn.add(minImage)

        closepixbuf = gtk.gdk.pixbuf_new_from_file("resource/titlebar/ID_CLOSED_TITLEBAR.gif")
        closeImage = gtk.Image()
        closeImage.set_from_pixbuf(closepixbuf)
        self.closeBtn.add(closeImage)

        self.titleBarBox.pack_start(gtk.Alignment(), False, False, 5)
        self.titleBarBox.pack_start(titleImageBox, expand = False, fill = False, padding = 0)
        self.titleBarBox.pack_start(titleLabel, expand = False, fill = False, padding = 0)
        self.titleBarBox.pack_end(self.closeBtn, expand = False, fill = False, padding = 0)
        self.titleBarBox.pack_end(self.minBtn, expand = False, fill = False, padding = 0)
        self.titleBarBox.pack_end(self.setBtn, expand = False, fill = False, padding = 0)
        self.titleBarBox.pack_end(userLabel, expand = False, fill = False, padding = 0)
        self.titleBarBox.pack_end(headImageBox, expand = False, fill = False, padding = 0)

class ToolBarWidget:
    def __init__(self):
        self.toolBarBox = gtk.HBox()

        self.homeBtn = gtk.Button()
        self.homeBtn.set_size_request(84,84)
        self.stateBtn = gtk.Button()
        self.stateBtn.set_size_request(84,84)
        self.softmanagerBtn = gtk.Button()
        self.softmanagerBtn.set_size_request(84,84)
        self.auditBtn = gtk.Button()
        self.auditBtn.set_size_request(84,84)
        self.sysinfoBtn = gtk.Button()
        self.sysinfoBtn.set_size_request(84,84)
        #set button transparency
        self.homeBtn.set_relief(gtk.RELIEF_NONE)
        self.stateBtn.set_relief(gtk.RELIEF_NONE)
        self.softmanagerBtn.set_relief(gtk.RELIEF_NONE)
        self.auditBtn.set_relief(gtk.RELIEF_NONE)
        self.sysinfoBtn.set_relief(gtk.RELIEF_NONE)
        #set toolbtn image
        homepixbuf = gtk.gdk.pixbuf_new_from_file("resource/toolbar/ID_HOME_TOOLBAR.png")
        homeImage = gtk.Image()
        #homeImage.set_from_file("resource/toolbar/ID_HOME_TOOLBAR.png")
        homeImage.set_from_pixbuf(homepixbuf)
        self.homeBtn.add(homeImage)

        statepixbuf = gtk.gdk.pixbuf_new_from_file("resource/toolbar/ID_STATE_VIEW_TOOLNAR.png")
        stateImage = gtk.Image()
        stateImage.set_from_pixbuf(statepixbuf)
        self.stateBtn.add(stateImage)

        softmanagerpixbuf = gtk.gdk.pixbuf_new_from_file("resource/toolbar/ID_SOFT_MANAGER_TOOLBAR.png")
        softmanagerImage = gtk.Image()
        softmanagerImage.set_from_pixbuf(softmanagerpixbuf)
        self.softmanagerBtn.add(softmanagerImage)

        auditpixbuf = gtk.gdk.pixbuf_new_from_file("resource/toolbar/ID_AUDIT_INFO.png")
        auditImage = gtk.Image()
        auditImage.set_from_pixbuf(auditpixbuf)
        self.auditBtn.add(auditImage)

        sysinfopixbuf = gtk.gdk.pixbuf_new_from_file("resource/toolbar/ID_BTN_SYSINFO.png")
        sysinfoImage = gtk.Image()
        sysinfoImage.set_from_pixbuf(sysinfopixbuf)
        self.sysinfoBtn.add(sysinfoImage)

        self.toolBarBox.pack_start(gtk.Alignment(), False, False, 20)
        self.toolBarBox.pack_start(self.homeBtn, expand = False, fill = False, padding = 0)
        self.toolBarBox.pack_start(self.stateBtn, expand = False, fill = False, padding = 0)
        self.toolBarBox.pack_start(self.softmanagerBtn, expand = False, fill = False, padding = 0)
        self.toolBarBox.pack_start(self.auditBtn, expand = False, fill = False, padding = 0)
        #toolBarBox.pack_start(sysinfoBtn, expand = False, fill = False, padding = 0)

class NotebookWidget:
    def __init__(self):
        self.notebook = gtk.Notebook()
        self.notebook.set_show_tabs(False)
        self.notebook.set_size_request(900,600 - 32 - 84)

        box1 = gtk.HBox()
        box2 = gtk.HBox()
        box3 = gtk.VBox()

        #book1
        wview1 = webkit.WebView()
        wview1.open('/home/ymc/test/pygtkgui/html/rose_chart.html')
        box1.add(wview1)
        self.notebook.append_page(box1)

        #book2
        self.wview2 = webkit.WebView()
        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        sw.add_with_viewport(self.wview2)
        box2.add(sw)
        self.notebook.append_page(box2)

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
        box3.add(page3Align)
        self.notebook.append_page(box3)

        page4Label = gtk.Label('This is Page 4')
        page5Label = gtk.Label('This is Page 5')
        self.notebook.append_page(page4Label)
        self.notebook.append_page(page5Label)

class MainWindow(gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_log()
        self.set_window_moveable()
        self.create_trayicon()

        mainBox = gtk.VBox();

        titleBarWid = TitleBarWidget()
        toolBarWid = ToolBarWidget()

        titleEb = gtk.EventBox()
        titleEb.add(titleBarWid.titleBarBox)
        titleEb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("#3684d7"))

        toolEb = gtk.EventBox()
        toolEb.add(toolBarWid.toolBarBox)
        toolEb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color("#3684d7"))

        titleBarWid.setBtn.connect('clicked', self.setBtnClicked)
        titleBarWid.minBtn.connect('clicked',self.minBtnClicked)
        titleBarWid.closeBtn.connect('clicked', self.closeBtnClicked)

        toolBarWid.homeBtn.connect('clicked', self.homeBtnClicked)
        toolBarWid.stateBtn.connect('clicked',self.stateBtnClicked)
        toolBarWid.softmanagerBtn.connect('clicked', self.softmanagerBtnClicked)
        toolBarWid.auditBtn.connect('clicked', self.auditBtnClicked)
        toolBarWid.sysinfoBtn.connect('clicked', self.sysinfoBtnClicked)

        barBox = gtk.VBox()
        barBox.pack_start(titleEb)
        barBox.pack_start(toolEb)
        barAlign = gtk.Alignment(0, 0, 1, 0)
        barAlign.add(barBox)

        self.notebookWid = NotebookWidget()

        mainBox.add(barAlign)
        mainBox.add(self.notebookWid.notebook)
       
        self.connect("destroy",gtk.main_quit)
        self.add(mainBox)
        self.show_all()

    #titlebar slots
    def setBtnClicked(self, setBtn):
        self.create_menu()

    def minBtnClicked(self, minBtn):
        self.hide()

    def closeBtnClicked(self, closeBtn):
        gtk.main_quit()

    
    def set_window_moveable(self):
        #self.set_keep_above(True)
        self.set_icon_from_file("resource/titlebar/tiptray.ico");
        self.set_modal(True)
        self.set_decorated(False)
        #self.set_title('MainUI')
        self.set_resizable(False)
        self.set_default_size(900, 600)

        self.set_events(gtk.gdk.BUTTON_RELEASE_MASK | gtk.gdk.BUTTON_PRESS_MASK |
                        gtk.gdk.POINTER_MOTION_MASK | gtk.gdk.POINTER_MOTION_HINT_MASK)
        self.connect('button-release-event', self.on_release) # 鼠标释放
        self.connect('button-press-event', self.on_press) # 鼠标按下
        self.connect('motion-notify-event', self.on_move) #鼠标移动
 
        self.is_press = False
        # 鼠标按下坐标
        self.start_x = 0
        self.start_y = 0
        #窗口坐标
        self.coordinate_x = 0
        self.coordinate_y = 0

    def on_press(self, widget, event):
        # 获取窗口起始坐标
        self.coordinate_x, self.coordinate_y = self.get_position()
        # 鼠标按下时坐标
        self.start_x = event.x
        self.start_y = event.y
        self.is_press = True
 
    def on_release(self, widget, event):
        self.is_press = False
 
    def on_move(self, widget, event):
        if self.is_press:
            # 计算鼠标移动的距离（相对按下时的坐标）
            x = event.x - self.start_x
            y = event.y - self.start_y
            # 更新窗口起始坐标
            self.coordinate_x += x
            self.coordinate_y += y
            # 移动窗口
            self.move(int(self.coordinate_x), int(self.coordinate_y))




    #toolbar slots
    def homeBtnClicked(self, homeBtn):
        self.notebookWid.notebook.set_current_page(0)
        self.mylog.debug("home btn clicked")

    def stateBtnClicked(self, stateBtn):
        self.notebookWid.wview2.load_uri('https://developer.gnome.org/pygtk/stable/index.html')
        self.notebookWid.notebook.set_current_page(1)
        self.mylog.info("state btn clicked")

    def softmanagerBtnClicked(self, softmanagerBtn):
        self.notebookWid.notebook.set_current_page(2)
        self.mylog.warning("softmanager btn clicked")

    def auditBtnClicked(self, auditBtn):
        self.notebookWid.notebook.set_current_page(3)
        self.mylog.error("audit btn clicked")

    def sysinfoBtnClicked(self, sysinfoBtn):
        self.notebookWid.notebook.set_current_page(4)
        self.mylog.critical("sysinfo btn clicked")

    #window topright setting menu
    def create_menu(self):
        menu = gtk.Menu()
        menu.set_size_request(136,223)

        registItem = gtk.ImageMenuItem("     软件注册")
        registItem.set_size_request(136,35)
        modeItem = gtk.ImageMenuItem("     模式设置")
        modeItem.set_size_request(136,35)
        upgradeItem = gtk.ImageMenuItem("     版本升级")
        upgradeItem.set_size_request(136,35)
        manualItem = gtk.ImageMenuItem("     操作手册")
        manualItem.set_size_request(136,35)
        aboutItem = gtk.ImageMenuItem("     关于我们")
        aboutItem.set_size_request(136,35)

        #add image
        registPixbuf = gtk.gdk.pixbuf_new_from_file("resource/titlebar/ID_SETTING_REGISTER.png")
        registImage = gtk.Image()
        registImage.set_from_pixbuf(registPixbuf)
        registItem.set_image(registImage)
        registItem.set_always_show_image(True)
        
        modePixbuf = gtk.gdk.pixbuf_new_from_file("resource/titlebar/ID_toolbar_peizhimianban.png")
        modeImage = gtk.Image()
        modeImage.set_from_pixbuf(modePixbuf)
        modeItem.set_image(modeImage)
        modeItem.set_always_show_image(True)

        upgradePixbuf = gtk.gdk.pixbuf_new_from_file("resource/titlebar/ID_SETTING_UPGRADE.png")
        upgradeImage = gtk.Image()
        upgradeImage.set_from_pixbuf(upgradePixbuf)
        upgradeItem.set_image(upgradeImage)
        upgradeItem.set_always_show_image(True)

        manualPixbuf = gtk.gdk.pixbuf_new_from_file("resource/titlebar/ID_SETTING_MANUAL.png")
        manualImage = gtk.Image()
        manualImage.set_from_pixbuf(manualPixbuf)
        manualItem.set_image(manualImage)
        manualItem.set_always_show_image(True)

        aboutPixbuf = gtk.gdk.pixbuf_new_from_file("resource/titlebar/ID_SETTING_ABOUT.png")
        aboutImage = gtk.Image()
        aboutImage.set_from_pixbuf(aboutPixbuf)
        aboutItem.set_image(aboutImage)
        aboutItem.set_always_show_image(True)

        sep1 = gtk.SeparatorMenuItem()
        sep2 = gtk.SeparatorMenuItem()
        sep3 = gtk.SeparatorMenuItem()
        sep4 = gtk.SeparatorMenuItem()

        menu.append(registItem)
        menu.append(sep1)
        menu.append(modeItem)
        menu.append(sep2)
        menu.append(upgradeItem)
        menu.append(sep3)
        menu.append(manualItem)
        menu.append(sep4)
        menu.append(aboutItem)

        menu.show_all()
        menu.popup(None, None, None, 3, 0)

    #create statusicon
    def create_trayicon(self):
        self.trayicon = gtk.status_icon_new_from_file("resource/titlebar/tiptray.ico")
        self.trayicon.set_tooltip("Httcgui")
        self.trayicon.connect("activate", self.togglevisibility)
        self.trayicon.connect("popup-menu", self.popupmenu)
    #create statusicon menu
    def popupmenu(self, icon, button, time):
        menu = gtk.Menu()

        shlabel = "Hide" if self.get_visible() else "Show"
        showhide = gtk.MenuItem(shlabel)

        quit = gtk.MenuItem("Quit")

        showhide.connect("activate", self.togglevisibility)
        quit.connect("activate", self.main_quit)

        menu.append(showhide)
        menu.append(quit)

        menu.show_all()
        menu.popup(None, None, gtk.status_icon_position_menu, button, time, self.trayicon)

    def togglevisibility(self, event):
        if self.get_visible():
            self.hide()
            self.trayicon.set_blinking(True)
        else:
            self.show()
            self.trayicon.set_blinking(False)

    def main_quit(self, event):
        gtk.main_quit()

    def init_log(self):
        ''' NOTSET(0)、DEBUG(10)、INFO(20)、WARNING(30)、ERROR(40)、CRITICAL(50) '''
        #logging.basicConfig()
        self.mylog = logging.getLogger('log_gui')
        self.mylog.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s %(pathname)s[line: %(lineno)d] %(levelname)s: %(message)s")
        handler = logging.handlers.RotatingFileHandler('logs/log_gui.log', maxBytes = 100*1024*1024, backupCount = 3, encoding = 'utf-8')
        handler.setFormatter(formatter)
        self.mylog.addHandler(handler)



if __name__ == "__main__":
    MainWindow()
    gtk.main()

