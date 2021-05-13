pos = {str(i): (i, 3) for i in range(4)}
pos.update({str(i): (i-4, 2) for i in range(4, 8)})
pos.update({str(i): (i-8, 1) for i in range(8, 12)})
pos['4'] = (0.6, 1.3)
pos['6'] = (3, 2)
pos['7'] = (4, 2)
pos['3'] = (5, 3)
pos['11'] = (5, 1)
