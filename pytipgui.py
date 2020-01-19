#coding=utf-8
import gtk
import gtk.glade
import webkit
import logging
import logging.handlers
import os

import widgetclass

class MainWindow(gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_log()
        self.set_window_moveable()
        self.create_trayicon()

        mainBox = gtk.VBox();

        titleBarWid = widgetclass.TitleBarWidget()
        toolBarWid = widgetclass.ToolBarWidget()

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

        self.notebookWid = widgetclass.NotebookWidget()

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
        resource_dir = os.path.join(widgetclass.guiDir(), "resource")

        #self.set_keep_above(True)
        self.set_icon_from_file(resource_dir + "/titlebar/tiptray.ico");
        self.set_modal(True)
        self.set_decorated(False)
        #self.set_title('MainUI')
        self.set_resizable(True)
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

        resource_dir = os.path.join(widgetclass.guiDir(), "resource")
        #add image
        registPixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/titlebar/ID_SETTING_REGISTER.png")
        registImage = gtk.Image()
        registImage.set_from_pixbuf(registPixbuf)
        registItem.set_image(registImage)
        registItem.set_always_show_image(True)
        
        modePixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/titlebar/ID_toolbar_peizhimianban.png")
        modeImage = gtk.Image()
        modeImage.set_from_pixbuf(modePixbuf)
        modeItem.set_image(modeImage)
        modeItem.set_always_show_image(True)

        upgradePixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/titlebar/ID_SETTING_UPGRADE.png")
        upgradeImage = gtk.Image()
        upgradeImage.set_from_pixbuf(upgradePixbuf)
        upgradeItem.set_image(upgradeImage)
        upgradeItem.set_always_show_image(True)

        manualPixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/titlebar/ID_SETTING_MANUAL.png")
        manualImage = gtk.Image()
        manualImage.set_from_pixbuf(manualPixbuf)
        manualItem.set_image(manualImage)
        manualItem.set_always_show_image(True)

        aboutPixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/titlebar/ID_SETTING_ABOUT.png")
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
        resource_dir = os.path.join(widgetclass.guiDir(), "resource")
        self.trayicon = gtk.status_icon_new_from_file(resource_dir + "/titlebar/tiptray.ico")
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
        logs_dir = os.path.join(widgetclass.guiDir(), "logs")
        self.mylog = logging.getLogger('log_gui')
        self.mylog.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s %(pathname)s[line: %(lineno)d] %(levelname)s: %(message)s")
        handler = logging.handlers.RotatingFileHandler(logs_dir + '/log_gui.log', maxBytes = 100*1024*1024, backupCount = 3, encoding = 'utf-8')
        handler.setFormatter(formatter)
        self.mylog.addHandler(handler)

if __name__ == "__main__":
    MainWindow()
    gtk.main()

