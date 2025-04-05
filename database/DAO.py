from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass


    def get_anno(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor()
            cursor.execute("SELECT DISTINCT YEAR(Date) FROM go_daily_sales")
            for row in cursor:
                result.append(row[0])
            cursor.close()
            cnx.close()
            print(result)
            return result
        else:
            print("Non è stato possibile connettersi")
            return None


    def get_brand(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor()
            cursor.execute("SELECT DISTINCT Product_brand FROM go_products")
            for row in cursor:
                result.append(row[0])
            cursor.close()
            cnx.close()
            print(result)
            return result
        else:
            print("Non è stato possibile connettersi")
            return None

    def get_retailer(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM go_retailers")
            for row in cursor:
                result.append(Retailer(int(row[0]), row[1], row[2], row[3]))
            cursor.close()
            cnx.close()
            print(result)
            return result
        else:
            print("Non è stato possibile connettersi")
            return None

    def getRicavi(self, anno, brand, retailer):

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = f"""select gds.Quantity * gds.Unit_sale_price as ricavo
                    from go_daily_sales gds, go_retailers gr , go_products gp 
                    where gds.Retailer_code = gr.Retailer_code 
                    and gds.Product_number = gp.Product_number 
                    and YEAR(gds.Date)= COALESCE(%s, YEAR(gds.Date))
                    and gp.Product_brand = COALESCE(%s, gp.Product_brand) 
                    and gr.Retailer_name = COALESCE(%s, gr.Retailer_name)"""
        cursor.execute(query, (anno, brand, retailer))
        # rs = cursor.fetchall()
        copia = []

        for i in cursor:
            copia.append(float(i[0]))

        copia = sorted(copia, reverse=True)

        #print(copia)

        cnx.close()
        return copia


    def getVendite(self, anno, brand, retailer):

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = f"""select gds.Quantity * gds.Unit_sale_price as ricavo, gds.Retailer_code, gp.Product_number
                    from go_daily_sales gds, go_retailers gr , go_products gp 
                    where gds.Retailer_code = gr.Retailer_code 
                    and gds.Product_number = gp.Product_number 
                    and YEAR(gds.Date)= COALESCE(%s, YEAR(gds.Date))
                    and gp.Product_brand = COALESCE(%s, gp.Product_brand) 
                    and gr.Retailer_name = COALESCE(%s, gr.Retailer_name)"""
        cursor.execute(query, (anno, brand, retailer))
        # rs = cursor.fetchall()
        copia = []

        for i in cursor:
            copia.append(i)


        print(copia)

        cnx.close()
        return copia


    def getStatistiche(self, anno, brand, retailer):

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()


        query = f"""select sum(gds.Quantity * gds.Unit_sale_price) as ricavi, 
	                count(*) as num_vendite,
	                count(DISTINCT gds.Retailer_code) as num_retailer,
                    count(DISTINCT gds.Product_number) as num_prodotti
                    from go_daily_sales gds, go_retailers gr , go_products gp 
                    where gds.Retailer_code  = gr.Retailer_code  and gds.Product_number = gp.Product_number 
                    and YEAR(gds.Date)= COALESCE(%s, YEAR(gds.Date))
                    and gp.Product_brand = COALESCE(%s, gp.Product_brand) 
                    and gr.Retailer_name = COALESCE(%s, gr.Retailer_name) """


        cursor.execute(query, (anno, brand, retailer))
        #rs = cursor.fetchall()
        res = []

        for i in cursor:
            res.append(i)



        cnx.close()
        return res



if __name__ == '__main__':
    es = DAO()
    es.get_anno()
    es.getRicavi(2015, "Edge", "Consumer Club")
    es.getVendite(2015, "Edge", "Consumer Club")
    es.getStatistiche(2015, "Edge", "Consumer Club")