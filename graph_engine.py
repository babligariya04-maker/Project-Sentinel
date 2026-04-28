import networkx as nx

print("🕸️ Initializing Project Sentinel Graph Engine...")

# 1. Build the Baseline Supply Chain Graph
G = nx.Graph()

# Add Nodes (Cities/Hubs)
nodes = ["Mumbai Port", "Pune Hub", "Nashik Hub", "Surat Factory", "Ahmedabad Plant"]
G.add_nodes_from(nodes)

# Add Edges (Routes) with Baseline Transit Times (in hours)
baseline_edges = [
    ("Mumbai Port", "Pune Hub", 3),
    ("Mumbai Port", "Nashik Hub", 4),
    ("Pune Hub", "Surat Factory", 6),
    ("Nashik Hub", "Surat Factory", 5),
    ("Surat Factory", "Ahmedabad Plant", 4)
]
G.add_weighted_edges_from(baseline_edges)

def get_optimal_route(graph, source, target):
    """Calculates the fastest route using Dijkstra's shortest path algorithm."""
    try:
        path = nx.shortest_path(graph, source=source, target=target, weight='weight')
        transit_time = nx.shortest_path_length(graph, source=source, target=target, weight='weight')
        return path, transit_time
    except nx.NetworkXNoPath:
        return None, float('inf')

def trigger_contagion(graph, infected_node, delay_hours):
    """
    Simulates a disruption by dynamically increasing the weight (time) 
    of all routes connected to the infected node.
    """
    print(f"\n🚨 CONTAGION ALERT: {infected_node} has been compromised. (+{delay_hours} hrs delay)")
    
    # Create a copy of the graph so we don't permanently destroy the baseline
    dynamic_graph = graph.copy()
    
    for neighbor in dynamic_graph.neighbors(infected_node):
        # Increase the transit time heavily
        dynamic_graph[infected_node][neighbor]['weight'] += delay_hours
        
    return dynamic_graph

if __name__ == "__main__":
    # --- TEST RUN THE ENGINE ---
    print("\n--- BASELINE ROUTE (NORMAL CONDITIONS) ---")
    base_path, base_time = get_optimal_route(G, "Mumbai Port", "Ahmedabad Plant")
    print(f"Optimal Path: {' -> '.join(base_path)}")
    print(f"Estimated Transit Time: {base_time} hours")

    print("\n--- SIMULATING DISRUPTION ---")
    # Let's say our LSTM from Phase 2 predicted a 48-hour delay at Pune Hub
    infected_G = trigger_contagion(G, infected_node="Pune Hub", delay_hours=48)

    print("\n--- DYNAMIC REROUTE (SENTINEL ACTIVE) ---")
    new_path, new_time = get_optimal_route(infected_G, "Mumbai Port", "Ahmedabad Plant")
    print(f"New Optimal Path: {' -> '.join(new_path)}")
    print(f"Estimated Transit Time: {new_time} hours")
    
    # Calculate how much time the AI saved the company
    time_saved = (base_time + 48) - new_time
    print(f"⏱️ Time Saved by Rerouting: {time_saved} hours")