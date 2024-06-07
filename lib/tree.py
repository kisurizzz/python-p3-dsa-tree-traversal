class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]

    while nodes_to_visit:
      current = nodes_to_visit.pop()
      if current['id'] == id:
        return current

      nodes_to_visit = current['children'] + nodes_to_visit
    return None
    
  
  def breadth_first_traversal(node):
    result = []
    nodes_to_visit = [node]

    while len(nodes_to_visit) > 0:
      # 1. Remove the first node from the `nodes_to_visit` list
      node = nodes_to_visit.pop(0)
      # 2. Add its value to the result list 
      result.append(node['value'])
      # 3. Add its children (if any) to the END of the `nodes_to_visit` list
      nodes_to_visit = nodes_to_visit + node['children']

    return result
  
  

  def depth_first_traversal(node):
    result = []
    nodes_to_visit = [node]

    while len(nodes_to_visit) > 0:
      # 1. Remove the first node from the `nodes_to_visit` list
      node = nodes_to_visit.pop(0)
      # 2. Add its value to the result list
      result.append(node['value'])
      # 3. Add its children (if any) to the BEGINNING of the `nodes_to_visit` list
      nodes_to_visit = node['children'] + nodes_to_visit

    return result