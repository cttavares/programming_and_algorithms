
def sierpinsky (x1, y1, x2, y2, x3, y3):

    x1_l = (x1 + x2)/2
    y1_l = (y1 + y2)/2

    x2_l = (x1 + x3)/2
    y2_l = (y1 + y3)/2

    x3_l = (x2+x3)/2
    y3_l = (y2+y3)/2

    if (x2-x1 < 0.5):
        return 

    desenha_triangulo (x1_l, y1_l, x3_l, y3_l, x2_l, y2_l)
    
    sierpinsky (x1_l, y1_l, x2_l, y2_l, x3_l, y3_l)
    sierpinsky (x1, y1, x1_l, y1_l, x2_l, y2_l)
    sierpinsky (x2_l, y2_l, x3_l, y3_l, x3, y3)

