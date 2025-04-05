import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)


        #ROW1

        self.ddAnno = ft.Dropdown(label="Anno",
                                    width=200,
                                    hint_text="Seleziona un anno",
                                    options=[ft.dropdown.Option("Nessun filtro")],
                                    on_change=self._controller.scegliAnno)

        self._controller.fillAnno()

        self.ddBrand = ft.Dropdown(label="Brand",
                                    width=200,
                                    hint_text="Seleziona un brand",
                                    options=[ft.dropdown.Option("Nessun filtro")],
                                    on_change=self._controller.scegliBrand)

        self._controller.fillBrand()

        self.ddRetailer = ft.Dropdown(label="Retailer",
                                    width=200,
                                    hint_text="Seleziona un retailer",
                                    options=[ft.dropdown.Option("Nessun filtro")],
                                    on_change=self._controller.scegliRetailer)

        self._controller.fillRetailer()

        """
        # button for the "hello" reply
        self.btn_hello = ft.ElevatedButton(text="Hello", on_click=self._controller.handle_hello)
        """

        #ROW2

        self._btnTopVendite = ft.ElevatedButton(text="Top Vendite", on_click=self._controller.handle_topVendite)
        self._btnAnalizzaVendite = ft.ElevatedButton(text="Analizza Vendite", on_click=self._controller.handle_AnalizzaVendite)

        row1 = ft.Row([self.ddAnno, self.ddBrand, self.ddRetailer],
                      alignment=ft.MainAxisAlignment.CENTER)
        row2 = ft.Row([self._btnTopVendite, self._btnAnalizzaVendite],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
