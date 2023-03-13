from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.config import Config
from kivy.core.window import Window

Config.set("graphics", "resizable", "1")
Config.set("graphics", "width", "1200")
Config.set("graphics", "height", "900")


Window.clearcolor = (.61, .87, .95, 1)


class Garden(MDApp):
    def __init__(self, model, controller):
        super().__init__()
        self.controller = controller
        self.controller.setView(self)
        self.model = model
        self.money = 99

    def exit(self):
        self.stop()

    def build(self):
        root = Builder.load_file('lib.kv')
        return root

    def clear_label(self):
        x = self.root.ids.display_data_screen.ids.gl_2
        x.clear_widgets()

    def update_data(self):
        self.root.ids.main_screen.ids.weather.text = "Погода: " + str(self.model.get_weather())
        self.root.ids.main_screen.ids.tree_kol.text = "Кол-во деревьев: " + str(self.model.tree_kol())
        self.root.ids.main_screen.ids.money.text = "Деньги: " + str(self.model.money())
        self.root.ids.main_screen.ids.garden_bed_kol.text = "Кол-во грядок: " + str(self.model.garden_bed_kol())
        self.root.ids.main_screen.ids.day.title = "День: " + str(self.model.day())

    def show_data(self):
        print("sh data")
        info_tree, info_cult = self.model.get_data_about_garden()
        print(info_tree)
        help = [self.root.ids.garden_screen.ids.tree_1, self.root.ids.garden_screen.ids.tree_2, self.root.ids.garden_screen.ids.tree_3, self.root.ids.garden_screen.ids.tree_4, self.root.ids.garden_screen.ids.tree_5]
        help_ill = [self.root.ids.garden_screen.ids.tree_ill_1, self.root.ids.garden_screen.ids.tree_ill_2, self.root.ids.garden_screen.ids.tree_ill_3, self.root.ids.garden_screen.ids.tree_ill_4, self.root.ids.garden_screen.ids.tree_ill_5]
        help_bug = [self.root.ids.garden_screen.ids.tree_bug_1, self.root.ids.garden_screen.ids.tree_bug_2, self.root.ids.garden_screen.ids.tree_bug_3, self.root.ids.garden_screen.ids.tree_bug_4, self.root.ids.garden_screen.ids.tree_bug_5]
        help_har = [self.root.ids.garden_screen.ids.tree_har_1, self.root.ids.garden_screen.ids.tree_har_2, self.root.ids.garden_screen.ids.tree_har_3, self.root.ids.garden_screen.ids.tree_har_4, self.root.ids.garden_screen.ids.tree_har_5]
        count = 0
        for tree in info_tree:
            count = count + 1
            if tree.get('Type') == 'pear':
                if tree.get('Adult'):
                    help[count - 1].source = 'image/peer.png'
                else:
                    help[count - 1].source = 'image/peer_little.png'
            else:
                if tree.get('Adult'):
                    help[count - 1].source = 'image/apple.png'
                else:
                    help[count - 1].source = 'image/apple_little.png'
            if tree.get('Ill'):
                help_ill[count - 1].source = 'image/ill.png'
            else:
                help_ill[count - 1].source = 'image/lol.png'
            if tree.get('Pest'):
                help_bug[count - 1].source = 'image/bug.png'
            else:
                help_bug[count - 1].source = 'image/lol.png'
            if tree.get('Harvest'):
                help_har[count - 1].source = 'image/har.png'
            else:
                help_har[count - 1].source = 'image/lol.png'

        h_c_weed = [self.root.ids.garden_screen.ids.cell_1_weed, self.root.ids.garden_screen.ids.cell_2_weed, self.root.ids.garden_screen.ids.cell_3_weed, self.root.ids.garden_screen.ids.cell_4_weed,  self.root.ids.garden_screen.ids.cell_5_weed, self.root.ids.garden_screen.ids.cell_6_weed]
        h_c = [self.root.ids.garden_screen.ids.cell_1, self.root.ids.garden_screen.ids.cell_2, self.root.ids.garden_screen.ids.cell_3, self.root.ids.garden_screen.ids.cell_4, self.root.ids.garden_screen.ids.cell_5, self.root.ids.garden_screen.ids.cell_6]
        h_c_bug = [self.root.ids.garden_screen.ids.cell_1_bug, self.root.ids.garden_screen.ids.cell_2_bug, self.root.ids.garden_screen.ids.cell_3_bug, self.root.ids.garden_screen.ids.cell_4_bug, self.root.ids.garden_screen.ids.cell_5_bug, self.root.ids.garden_screen.ids.cell_6_bug]
        h_c_har = [self.root.ids.garden_screen.ids.cell_1_har, self.root.ids.garden_screen.ids.cell_2_har, self.root.ids.garden_screen.ids.cell_3_har, self.root.ids.garden_screen.ids.cell_4_har, self.root.ids.garden_screen.ids.cell_5_har, self.root.ids.garden_screen.ids.cell_6_har]
        h_c_ill = [self.root.ids.garden_screen.ids.cell_1_ill, self.root.ids.garden_screen.ids.cell_2_ill, self.root.ids.garden_screen.ids.cell_3_ill, self.root.ids.garden_screen.ids.cell_4_ill, self.root.ids.garden_screen.ids.cell_5_ill, self.root.ids.garden_screen.ids.cell_6_ill]
        h_c_w = [self.root.ids.garden_screen.ids.cell_1_w, self.root.ids.garden_screen.ids.cell_2_w, self.root.ids.garden_screen.ids.cell_3_w, self.root.ids.garden_screen.ids.cell_4_w, self.root.ids.garden_screen.ids.cell_5_w, self.root.ids.garden_screen.ids.cell_6_w]
        h_c_water = [self.root.ids.garden_screen.ids.cell_1_water, self.root.ids.garden_screen.ids.cell_2_water, self.root.ids.garden_screen.ids.cell_3_water, self.root.ids.garden_screen.ids.cell_4_water, self.root.ids.garden_screen.ids.cell_5_water, self.root.ids.garden_screen.ids.cell_6_water]
        h_c_f = [self.root.ids.garden_screen.ids.cell_1_f, self.root.ids.garden_screen.ids.cell_2_f, self.root.ids.garden_screen.ids.cell_3_f, self.root.ids.garden_screen.ids.cell_4_f, self.root.ids.garden_screen.ids.cell_5_f, self.root.ids.garden_screen.ids.cell_6_f]
        h_c_fer = [self.root.ids.garden_screen.ids.cell_1_fer, self.root.ids.garden_screen.ids.cell_2_fer, self.root.ids.garden_screen.ids.cell_3_fer, self.root.ids.garden_screen.ids.cell_4_fer, self.root.ids.garden_screen.ids.cell_5_fer, self.root.ids.garden_screen.ids.cell_6_fer]

        count = 0
        for cell in info_cult:
            count = count + 1
            if cell.get('Weed'):
                h_c_weed[count - 1].source = 'image/weed.png'
            else:
                h_c_weed[count - 1].source = 'image/lol.png'
            if not cell.get('Plant'):
                h_c[count - 1].source = 'image/soil.png'
            else:
                h_c_w[count - 1].source = 'image/water.png'
                h_c_water[count - 1].text = str(cell.get('Water'))
                h_c_f[count - 1].source = 'image/fer.png'
                h_c_fer[count - 1].text = str(cell.get('Fertiliser'))
                if cell.get('Ill'):
                    h_c_ill[count - 1].source = 'image/ill.png'
                else:
                    h_c_ill[count - 1].source = 'image/lol.png'
                if cell.get('Pest'):
                    h_c_bug[count - 1].source = 'image/bug.png'
                else:
                    h_c_bug[count - 1].source = 'image/lol.png'
                if cell.get('Harvest'):
                    h_c_har[count - 1].source = 'image/har.png'
                else:
                    h_c_har[count - 1].source = 'image/lol.png'
                if cell.get('Type') == 'potato':
                    h_c[count - 1].source = 'image/potato.png'
                elif cell.get('Type') == 'tomato':
                    h_c[count - 1].source = 'image/tomato.png'
                else:
                    h_c[count - 1].source = 'image/pepper.png'


class MainScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class GardenScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass
