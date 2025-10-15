# make_diagram.py
from graphviz import Digraph

# Buat diagram berformat PNG
diagram = Digraph(format="png")
diagram.attr(rankdir="TB", size="8")

# Node untuk client, server, database
diagram.node("client", "User's Browser\n(Client-Side: HTML, CSS, JS)\n- Display UI\n- Handle inputs\n- Send request")
diagram.node("server", "Web Server\n(Server-Side: Node.js, PHP, Python)\n- Process request\n- Business logic\n- Query DB\n- Send response")
diagram.node("db", "Database\n(MySQL, MongoDB, PostgreSQL)\n- Store data\n- Retrieve data")

# Panah alur kerja
diagram.edge("client", "server", label="HTTP Request")
diagram.edge("server", "db", label="Query")
diagram.edge("db", "server", label="Result")
diagram.edge("server", "client", label="HTTP Response")

# Render ke file PNG di folder kerja saat ini
output_filename = "client_server_diagram"
diagram.render(output_filename, format="png", cleanup=True)

print(f"Diagram selesai: {output_filename}.png")
