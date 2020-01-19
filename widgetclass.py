#!/usr/bin/env python
# -*- coding: utf-8
import gtk
import webkit
import os
import sys
import pkg_resources

def guiDir():
    return os.path.dirname(sys.argv[0])

class CustomListWiget():
    def __init__(self, col, data, length=350, height=250):
        #self.set_size_request(length, height)
        #self.set_position(gtk.WIN_POS_CENTER)
        #self.connect("destroy", gtk.main_quit)
        #self.set_title(title)
        self.col = col
        self.data = data

        self.vbox = gtk.VBox()
        sw = gtk.ScrolledWindow()
        sw.set_size_request(960, 600 - 32 - 84 - 47)
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.vbox.pack_start(sw, True, True, 0)

        args = []
        for i in range(len(col)):
            args.append(str)

        self.store = gtk.ListStore(*args)
        for res in data:
            self.store.append(res)
        treeView = gtk.TreeView(self.store)
        treeView.set_size_request(960, 600 - 32 - 84 - 47)
        treeView.modify_bg(gtk.STATE_SELECTED, gtk.gdk.Color('#555555'))

        sw.add(treeView)
        self.create_columns(treeView)

    def create_columns(self, treeView):
        for i in range(len(self.col)):
            rendererText = gtk.CellRendererText()
            column = gtk.TreeViewColumn(self.col[i], rendererText, text=i)
            column.set_sort_column_id(i)
            column.set_resizable(True)
            #column.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
            column.set_min_width(20)
            column.set_fixed_width(80)
            column.set_expand(True)
            treeView.append_column(column)

    def refresh_view(self, newdata):
        print 'refreshing...'
        self.store.clear()
        for res in newdata:
            self.store.append(res)
        return True

class Page3Widget:
    def __init__(self):
        gladefile = os.path.join(guiDir(), "page3.glade")
        print(gladefile)
        self.glade = gtk.glade.XML(gladefile)
        self.wid = self.glade.get_widget("page3box")
        self.glade.signal_autoconnect({"on_searchBtn_clicked" : self.page3_searchBtn_clicked,
                "on_addBtn_clicked" : self.page3_addBtn_clicked,
                "on_deleteBtn_clicked" : self.page3_deleteBtn_clicked,
                "on_page3win_destroy" : self.destroy})

    def page3_searchBtn_clicked(self, widget):
        print "page3_searchBtn_clicked"

    def page3_addBtn_clicked(self, widget):
        print "page3_addBtn_clicked"

    def page3_deleteBtn_clicked(self, widget):
        print "page3_deleteBtn_clicked"

    def destroy(self, widget):
        gtk.main_quit()

class Page4Widget:
    def __init__(self):
        self.vbox = gtk.VBox()
        label_hbox = gtk.HBox()
        label = gtk.Label();
        label.set_size_request(960, 47)
        label.set_markup("<span foreground = '#9aebff'>审计信息</span>")
        label_hbox.pack_start(label, False, False, 10)

        coltitle = ['审计时间', '用户名','操作','操作结果']
        row_data = [['2020.01.10 15:19:56', 'root', '测试数据a', '成功'],
                    ['2020.01.11 15:19:56', 'secadm', '测试数据e', '成功'],
                    ['2020.01.23 15:19:56', 'auditadm', '测试数据z', '失败'],
                    ['2020.01.16 15:19:56', 'secadm', '测试数据f', '失败'],
                    ['2020.01.24 15:19:56', 'secadm', '测试数据e', '失败'],
                    ['2020.01.12 15:19:56', 'root', '测试数据g', '成功'],
                    ['2020.01.22 15:19:56', 'root', '测试数据h', '成功'],
                    ['2020.01.20 15:19:56', 'auditadm', '测试数据g', '失败'],
                    ['2020.01.16 15:19:56', 'secadm', '测试数据g', '成功'],
                    ['2020.01.13 15:19:56', 'auditadm', '测试数据r', '失败'],
                    ['2020.01.16 15:19:56', 'auditadm', '测试数据e', '成功'],
                    #['2020.01.19 15:19:56', 'root', '测试数据e', '成功'],
                    #['2020.01.18 15:19:56', 'root', '测试数据t', '成功'],
                    #['2020.01.14 15:19:56', 'secadm', '测试数据m', '失败'],
                    #['2020.01.21 15:19:56', 'root', '测试数据n', '失败'],
                    #['2020.01.15 15:19:56', 'root', '测试数据b', '成功'],
                    #['2020.01.17 15:19:56', 'secadm', '测试数据n', '成功'],
                   ]
        list_widget = CustomListWiget(coltitle, row_data)
        self.vbox.pack_start(label_hbox, False, False, 0)
        self.vbox.pack_start(list_widget.vbox, True, True, 0)

class TitleBarWidget:
    def __init__(self):
        resource_dir = os.path.join(guiDir(), "resource")

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
        titlepixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/titlebar/logo.png")
        titleImage = gtk.Image()
        titleImage.set_from_pixbuf(titlepixbuf)
        titleImageBox = gtk.VBox()
        titleImageBox.pack_start(titleImage)

        headpixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/titlebar/ID_USER_TITLEBAR.gif")
        headImage = gtk.Image()
        headImage.set_from_pixbuf(headpixbuf)
        headImageBox = gtk.VBox()
        headImageBox.pack_start(headImage)

        setpixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/titlebar/ID_SETTING_TITLEBAR.gif")
        setImage = gtk.Image()
        setImage.set_from_pixbuf(setpixbuf)
        self.setBtn.add(setImage)

        minpixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/titlebar/ID_MIN_TITLEBAR.gif")
        minImage = gtk.Image()
        minImage.set_from_pixbuf(minpixbuf)
        self.minBtn.add(minImage)

        closepixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/titlebar/ID_CLOSED_TITLEBAR.gif")
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
        resource_dir = os.path.join(guiDir(), "resource")

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
        homepixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/toolbar/ID_HOME_TOOLBAR.png")
        homeImage = gtk.Image()
        #homeImage.set_from_file("resource/toolbar/ID_HOME_TOOLBAR.png")
        homeImage.set_from_pixbuf(homepixbuf)
        self.homeBtn.add(homeImage)

        statepixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/toolbar/ID_STATE_VIEW_TOOLNAR.png")
        stateImage = gtk.Image()
        stateImage.set_from_pixbuf(statepixbuf)
        self.stateBtn.add(stateImage)

        softmanagerpixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/toolbar/ID_SOFT_MANAGER_TOOLBAR.png")
        softmanagerImage = gtk.Image()
        softmanagerImage.set_from_pixbuf(softmanagerpixbuf)
        self.softmanagerBtn.add(softmanagerImage)

        auditpixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/toolbar/ID_AUDIT_INFO.png")
        auditImage = gtk.Image()
        auditImage.set_from_pixbuf(auditpixbuf)
        self.auditBtn.add(auditImage)

        sysinfopixbuf = gtk.gdk.pixbuf_new_from_file(resource_dir + "/toolbar/ID_BTN_SYSINFO.png")
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
        box4 = gtk.VBox()

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

        page4Widget = Page4Widget()
#        page3Align = gtk.Alignment(0, 0, 1, 0)
#        page3Align.add(wid)
        box4.add(page4Widget.vbox)
        self.notebook.append_page(box4)

        page5Label = gtk.Label('This is Page 5')
        self.notebook.append_page(page5Label)



