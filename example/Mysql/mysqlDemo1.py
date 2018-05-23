# -*- coding: UTF-8 -*-
import MySQLdb
db = MySQLdb.connect("192.168.1.188","root","123456","escondida", charset='utf8')
cursor = db.cursor()

# sql1="UPDATE project_car_log SET statue=0 where id=1"
# sql2="UPDATE project_car_log SET statue=1 where id=2"
# sql3="UPDATE project_car_log SET statue=2 where id=3"
# sql4="UPDATE project_car_log SET statue=2 where id=4"
# sql5="UPDATE project_car_log SET statue=3 where id=5"
# sql6="UPDATE project_car_log SET statue=4 where id=6"

# cursor.execute(sql1)
# cursor.execute(sql2)
# cursor.execute(sql3)
# cursor.execute(sql4)
# cursor.execute(sql5)
# cursor.execute(sql6)


sql6="UPDATE project_work_plan_detail SET car_id=888888 where car_id=33"
sql7="UPDATE project_work_plan_detail SET digging_machine_id=888888 where digging_machine_id=33"
cursor.execute(sql6)
cursor.execute(sql7)

db.commit()
db.close()

