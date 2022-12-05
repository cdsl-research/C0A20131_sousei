from surveillance import ping2
from apl import apl_print
from web import web_print
import select_mode
select = select_mode.get_select() 
print(select)
if select == "death":
    a = ping2.print_ping()
    print(a)
if select == "apl":
    b = apl_print.print_apl()
    print(b)
if select == "web":
    c = web_print.web_print()
    print(c)
else:
    print("失敗")


