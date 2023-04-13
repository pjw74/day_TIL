import win32com.client as win32
import keyboard

excel = win32.gencache.EnsureDispatch("Excel.Application")

while True:
    if keyboard.is_pressed("F9"):
        if excel.Visible != 1:
            wb = excel.Workbooks.Open(r"C:\Users\김혜진\Desktop\1")
            if wb == None:
                excel.Quit()
                break

            excel.Visible = 1
            excel.WindowState = win32.constants.xlMaximized  # this works for me

    if keyboard.is_pressed("F9"):
        wb = excel.Workbooks.Open(r"C:\Users\김혜진\Desktop\1")
        if wb == None:
            excel.Quit()
            break
        excel.Visible = 0
        excel.WindowState = win32.constants.xlMinimized

    if keyboard.is_pressed("esc"):
        wb.Close(SaveChanges=True)
        excel.Quit()
        break
