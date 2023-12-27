from native import app

#Translated Python code:

#Called when application is started.
def OnStart():
    global spin
    #Create a layout with objects vertically centered.
    lay = app.CreateLayout("linear", "VCenter,FillXY")

    #Add a spinner control to select storage type.
    spin = app.AddSpinner(lay, "Internal,External,USB", 0.5)
    spin.SelectItem("Internal")

    #Create a test button.
    btnWrite = app.AddButton(lay, "Write to Storage", 0.5)
    btnWrite.SetOnTouch(btnWrite_OnTouch)
    btnWrite.SetMargins(0, 0.05, 0, 0)

    #Create a button to clear write permissions.
    btnRemove = app.AddButton(lay, "Remove Permissions", 0.5)
    btnRemove.SetOnTouch(btnRemove_OnTouch)
    btnRemove.SetMargins(0, 0.05, 0, 0)

    #Add layout to app.
    app.AddLayout(lay)

#Handle the 'write to storage' button.
def btnWrite_OnTouch():
    WriteToStorage()

#Handle the 'remove permissions' button.
def btnRemove_OnTouch():
    app.RemovePermission("*")

#Write a file to the chosen storage type.
def WriteToStorage():
    #Set internal or external storage folder.
    if spin.GetText() == "Internal":
        fldr = "/Internal/Documents/MyData"
        perm = "internal"
    elif spin.GetText() == "External":
        fldr = "/External/Documents/MyData"
        perm = "external"
    else:
        fldr = "/USB/MyData"
        perm = "usb"

    #Check if we have permission to write to folder.
    if not app.CheckPermission(fldr):
        app.Alert("Please give permission to access the " + fldr + " folder or a parent folder")
        app.GetPermission(perm, OnPermission)
        return

    #Create folder and write a file.
    app.MakeFolder(fldr)
    app.WriteFile(fldr + "/file.txt", "Hello")

    #Read back file to check it worked.
    s = app.ReadFile(fldr + "/file.txt")
    if s == "Hello":
        app.ShowPopup("written: " + s)
    else:
        app.ShowPopup("write failed!")

#Handle result of permission request.
def OnPermission(path, uri):
    if not path:
        app.ShowPopup("Permission not granted!")
    else:
        WriteToStorage()