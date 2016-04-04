from turtle import *
color('blue', 'red')
begin_fill()
while True:
    forward(2)
    right(1)
    if abs(pos()) < 1:
        break
end_fill()
done()
