from database.DAO import DAO


class Model:
    def __init__(self):
        self.anno = None
        self.brand = None
        self.retailer = None

    def getAnno(self):
        self.anno = DAO().get_anno()
        return self.anno

    def getBrand(self):
        self.brand = DAO().get_brand()
        return self.brand

    def getRetailer(self):
        self.retailer = DAO().get_retailer()
        return self.retailer

    def ricavi(self, anno, brand, retailer):
        ricavi = DAO().getRicavi(anno, brand, retailer)
        return ricavi

    def get_stats_vendite(self, anno, brand, retailer):
        statistiche = DAO().getStatistiche(anno, brand, retailer)
        return statistiche
