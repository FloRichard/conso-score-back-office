from .db_access import get_db


def get_seller_partners_db(seller_id):
    try :
        cursor = get_db().cursor()
        cursor.execute("SELECT * FROM maker \
                        JOIN partnership ON partnership.maker_id = maker.maker_id\
                        JOIN seller ON seller.seller_id = partnership.seller_id\
                        WHERE seller.seller_id=%s",(seller_id,))
        partners = []
        for element in cursor.fetchall():
            partners.append({"maker_id":element[0], "name":element[1], "location":element[2]})
        return partners
    except Exception as e:
        print(e)
        return "an error occured while getting the partners"


