g_sum = None
ans = None

def dfs(order, warehouses, cost, i, l, c_sum):
	if isOrderSatisfied(order):
		global g_sum, ans
		if c_sum < g_sum:
			g_sum = c_sum
			ans = l
		return
	if i < len(warehouses):
		# discard
		orderA = order.copy()
		dfs(orderA, warehouses, cost, i+1, l.copy(), c_sum)

		# keep
		orderB = decreaseOrder(order.copy(), warehouses[i])
		new_l = l.copy()
		new_l[i] = 1
		dfs(orderB, warehouses, cost, i+1, new_l, c_sum + cost[i])

def decreaseOrder(order, warehouse):
	for key, val in warehouse.items():
		if key in order:
			order[key] -= val
	return order

def isOrderSatisfied(order):
	for num in order.values():
		if num > 0:
			return False
	return True

if __name__ == '__main__':
	order = { 'apple': 5, 'banana': 3 }
	warehouses = [
		{ 'apple': 1, 'banana': 2 },
		{ 'apple': 3, 'banana': 2 },
		{ 'apple': 2, 'banana': 1 }
	]
	cost = [ 1, 2, 4 ]
	g_sum = sum(cost)
	dfs(order, warehouses, cost, 0, [0] * len(warehouses), 0)
	if ans != None:
		print("The answer should be(0 - don't select, 1 - select):")
		print(ans)
	else:
		print("No solution")
