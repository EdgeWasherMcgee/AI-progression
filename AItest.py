import AIperiment

def test1():
	node_0_1 = AIperiment.top_node()
	node_0_2 = AIperiment.top_node()
	node_0_1.ch_val(0.5)
	node_0_2.ch_val(3)
	
	node_1_1 = AIperiment.node(2)
	node_1_1.add_parent(node_0_1, 2)
	node_1_1.add_parent(node_0_2, 4)

	node_1_2 = AIperiment.node(1)
	node_1_2.add_parent(node_0_1, 8)
	node_1_2.add_parent(node_0_2, 3.141592)

	node_1_3 = AIperiment.node(0.1313)
	node_1_3.add_parent(node_0_1, 4.3)
	node_1_3.add_parent(node_0_2, 7)

	node_2_1 = AIperiment.node(0.2)
	node_2_1.add_parent(node_1_1, 5)
	node_2_1.add_parent(node_1_2, 2)
	node_2_1.add_parent(node_1_3, 0.412)
	return node_2_1.value()