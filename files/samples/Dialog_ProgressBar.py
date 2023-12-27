from native import app

# Called when application is started.
def OnStart():
    # Create a layout with objects vertically centered.
    lay = app.CreateLayout("linear", "VCenter,FillXY")

    # Create a button to start demo.
    btn = app.CreateButton("Start", 0.3, 0.1)
    btn.SetOnTouch(btn_OnTouch)
    lay.AddChild(btn)

    # Add layout to app.
    app.AddLayout(lay)

# Called when user touches our button.
def btn_OnTouch():
    app.ShowProgressBar("Processing...", 0)
    setInterval(lambda: Update(10), 1000)
    setInterval(lambda: Update(30), 2000)
    setInterval(lambda: Update(40), 3000)
    setInterval(lambda: Update(60), 4000)
    setInterval(lambda: Update(100), 5000)
    setTimeout(lambda: Hide(), 6000)

# Update the progress bar.
def Update(progress):
    app.UpdateProgressBar(progress)

# Hide the progress bar.
def Hide():
    app.HideProgressBar()