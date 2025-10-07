import var

def run_task():
    if var.timer1:
        var.a += .01
        print(var.a)

def reset_task():
    var.a = 0

def stop_task(id):
    if id == 0:
        var.timer1 = False
    if id == 1:
        var.t1 = var.a
    if id == 2:
        var.t2 = var.a