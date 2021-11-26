import turtle
def tree(branch,t):
    if branch>5:
        t.forward(branch)
        t.right(20)
        tree(branch-15,t)
        t.left(40)
        tree(branch-15,t)
        t.right(20)
        t.backward(branch)
def main():
    t=turtle.Turtle()
    turtle.screensize(400,300)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    tree(100,t)
main()
