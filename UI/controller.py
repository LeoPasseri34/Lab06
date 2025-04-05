import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None
        self._brand = None
        self._retailer = None

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def scegliAnno(self, e):
        if self._view.ddAnno.value == "Nessun filtro":
            return self._anno
        else:
             self._anno = self._view.ddAnno.value



    def fillAnno(self):
        for i in self._model.getAnno():
            self._view.ddAnno.options.append(ft.dropdown.Option(i))
        self._view.update_page()

    def scegliBrand(self, e):
        if self._view.ddAnno.value == "Nessun filtro":
            return self._brand
        else:
             self._brand = self._view.ddBrand.value

    def fillBrand(self):
        for i in self._model.getBrand():
            self._view.ddBrand.options.append(ft.dropdown.Option(i))
        self._view.update_page()

    def scegliRetailer(self, e):
        if self._view.ddRetailer.value == "Nessun filtro":
            self._retailer = None
        else:
             self._retailer = self._view.ddRetailer.value

    def fillRetailer(self):
        for i in self._model.getRetailer():
            self._view.ddRetailer.options.append(ft.dropdown.Option(i))
        self._view.update_page()

    def handle_topVendite(self, e):
        ricavi = self._model.ricavi(self._anno, self._brand, self._retailer)
        if len(ricavi) > 4:
            lunghezza = 5

        else:
            lunghezza = len(ricavi)

        for i in range(0, lunghezza):
            self._view.txt_result.controls.append(ft.Text(ricavi[i]))
        self._view.update_page()

    def handle_AnalizzaVendite(self, e):
        stats_vendite = self._model.get_stats_vendite(self._anno, self._brand, self._retailer)
        s = stats_vendite[0]
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Statistiche vendite:"))
        self._view.txt_result.controls.append(ft.Text(f"Giro d'affari: {float(s[0])}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero vendite: {s[1]}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero retailer coinvolti: {s[2]}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero prodotti coinvolti: {s[3]}"))
        self._view.update_page()

