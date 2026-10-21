import json

data = {
    "id": "graph-theory",
    "name": "Graph theory",
    "mono": "GPH",
    "category": "Math",
    "qbCategory": "Science · Other Science (Math)",
    "kicker": "Dots joined by lines · Began with Euler’s Seven Bridges of Königsberg",
    "dates": "Founded by Leonhard Euler, 1736",
    "briefing": "Graph theory studies networks made of dots, called vertices or nodes, joined by lines, called edges, like cities linked by roads or friends linked online. It began in 1736, when Leonhard Euler proved that no one could walk through the city of Königsberg crossing each of its seven bridges exactly once. Its most famous result, the four color theorem, says that four colors are always enough to fill in a flat map so that no two neighboring regions match.",
    "answerHtml": "<b><u>graph</u></b> theory (accept <u>graph</u>s; prompt on <u>network</u>s or <u>network theory</u>; do not accept “graphs of functions”)",
    "accept": [
        "graph theory",
        "graphs",
        "graph",
        "theory of graphs",
        "mathematical graph",
        "mathematical graphs"
    ],
    "prompt": [
        "network theory",
        "networks",
        "network",
        "network science",
        "combinatorics",
        "discrete math",
        "discrete mathematics"
    ],
    "reject": [
        "graphs of functions",
        "graph of a function",
        "graph of function",
        "graphs of a function",
        "graphing",
        "graphing functions",
        "coordinate graph",
        "coordinate graphs",
        "coordinate plane",
        "line graph",
        "line graphs",
        "bar graph",
        "bar graphs",
        "pie graph",
        "graph paper",
        "graphing calculator",
        "topology",
        "group theory",
        "set theory",
        "game theory",
        "knot theory",
        "number theory",
        "chaos theory",
        "four color theorem",
        "four colour theorem",
        "seven bridges of konigsberg",
        "seven bridges",
        "konigsberg bridge problem",
        "konigsberg",
        "euler path",
        "eulerian path",
        "euler circuit",
        "eulerian circuit",
        "hamiltonian path",
        "hamiltonian cycle",
        "leonhard euler",
        "euler",
        "tree",
        "trees",
        "matrices",
        "chromatography"
    ],
    "tests": {
        "right": [
            "Graph theory",
            "graphs",
            "graph",
            "graf theory",
            "theory of graphs"
        ],
        "prompt": [
            "network theory",
            "networks"
        ],
        "wrong": [
            "topology",
            "group theory",
            "graph of a function",
            "four color theorem",
            "Euler",
            "set theory",
            "bar graph"
        ]
    },
    "mediaPending": True,
    "media": [],
    "wiki": "https://en.wikipedia.org/wiki/Graph_theory",
    "qb": {
        "q": "graph theory",
        "found": 0,
        "tip": "Search QBReader for this answer line (Middle School + Easy High School, power-marked) to see how real tossups clue it."
    },
    "sample": {
        "n": 0,
        "note": "no real tossups checked yet"
    },
    "tossups": [
        {
            "p": "James Joseph Sylvester introduced the name for the main objects of this field in 1878, comparing them to the diagrams chemists drew of molecules. Dénes Kőnig [“KUR-nig”] wrote the first textbook on this subject in 1936, exactly 200 years after its famous first problem was solved.",
            "r": "It studies networks of vertices joined by edges. For 10 points, name this branch of math that began with Leonhard Euler’s solution to the Seven Bridges of Königsberg problem."
        },
        {
            "p": "It is impossible to connect three houses to water, gas, and electricity on a flat sheet without any lines crossing, and the same is true for five points that are each joined to all the others. Networks that can be drawn with no crossings are called planar.",
            "r": "For 10 points, name this branch of math that studies vertices joined by edges, founded by Leonhard Euler."
        },
        {
            "p": "In 1852, Francis Guthrie made a guess while coloring a map of the counties of England, and in 1976 Kenneth Appel and Wolfgang Haken needed a computer to prove that guess. It was the first major theorem proved with a computer’s help.",
            "r": "That result, the four color theorem, belongs to this field. For 10 points, name this branch of math that studies vertices and edges."
        },
        {
            "p": "At any party of six people, either some three all know one another or some three are all strangers, a fact proved by coloring the lines between six dots and studied in Ramsey theory. In this field, the number of edges touching a vertex is called its degree.",
            "r": "For 10 points, name this branch of math, founded by Leonhard Euler, that studies networks of vertices and edges."
        },
        {
            "p": "Adding up the number of edges at every vertex of a network always gives exactly twice the number of edges, so the number of vertices that touch an odd number of edges must be even. That fact is called the handshake lemma.",
            "r": "For 10 points, name this branch of math that studies vertices joined by edges, which Leonhard Euler founded by studying seven bridges."
        },
        {
            "p": "William Rowan Hamilton’s 1857 Icosian game asked players to travel along the edges of a dodecahedron, visiting every corner exactly once and returning to the start. Finding the shortest such round trip through a list of cities is called the traveling salesman problem.",
            "r": "For 10 points, name this branch of math that studies networks of vertices and edges."
        },
        {
            "p": "A mathematician’s Erdős [“AIR-dush”] number counts the steps in the shortest chain of co-written papers linking them to Paul Erdős, who wrote about 1,500 papers. A similar game links actors to Kevin Bacon through the movies they made together.",
            "r": "Those games show “six degrees of separation” in social networks. For 10 points, name this branch of math that studies networks of vertices and edges."
        },
        {
            "p": "In Stanley Milgram’s 1967 small-world experiment, people tried to get a letter to a stranger by mailing it only to someone they knew personally, and the chains that finished took about six steps.",
            "r": "That idea is now called “six degrees of separation.” For 10 points, name this branch of math that models social networks as vertices joined by edges."
        },
        {
            "p": "In this field, a tree with 10 vertices must have exactly 9 edges, because every tree has one fewer edge than vertex. A tree is a connected network with no cycles, so there is exactly one path between any two of its vertices.",
            "r": "For 10 points, name this branch of math, founded by Leonhard Euler, that studies vertices and edges."
        },
        {
            "p": "For a connected network drawn on paper with no crossing edges, the number of vertices minus the number of edges plus the number of regions, counting the outside, always equals 2. A cube’s outline has 8 corners, 12 edges, and 6 faces, and 8 minus 12 plus 6 is 2.",
            "r": "For 10 points, name this branch of math that began with Euler’s puzzle about the seven bridges of Königsberg."
        },
        {
            "p": "Edsger Dijkstra’s [“DIKE-struhz”] algorithm finds the shortest route between two points in a network whose edges are labeled with distances, much like a GPS app planning a drive. Networks with numbers on their edges are called weighted.",
            "r": "For 10 points, name this branch of math that studies vertices joined by edges, starting with Euler’s seven bridges."
        },
        {
            "p": "The chromatic number of a network is the smallest number of colors that can be given to its vertices so that no edge joins two of the same color. Schools use this idea to schedule exams so that no student has two tests at the same time.",
            "r": "The four color theorem belongs to this field. For 10 points, name this branch of math that studies vertices and edges."
        },
        {
            "p": "Google’s original PageRank method treated the web as a huge network whose vertices are pages and whose one-way edges are links. A table of 0s and 1s called an adjacency matrix records which pairs of vertices are joined.",
            "r": "For 10 points, name this branch of math founded by Leonhard Euler’s work on the bridges of Königsberg."
        },
        {
            "p": "A figure can be drawn in one stroke, without lifting your pencil or retracing a line, only if zero or two of its corners touch an odd number of lines. If no corners touch an odd number, the drawing can end right where it started.",
            "r": "Leonhard Euler used this idea to show that no walk could cross each of Königsberg’s seven bridges exactly once. For 10 points, name this branch of math that studies vertices and edges."
        },
        {
            "p": "Networks with one-way edges are called directed, like a map of one-way streets or a food web whose arrows point from each prey to its predators. A network in which every pair of vertices is joined by an edge is called complete; the complete network on five vertices has 10 edges.",
            "r": "For 10 points, name this branch of math, begun by Leonhard Euler, that studies vertices and edges."
        }
    ],
    "clues": [
        {
            "id": "definition",
            "tier": "giveaway",
            "t": "Studies networks of dots, called vertices or nodes, joined by lines, called edges",
            "k": ["vertices", "edges", "nodes"],
            "n": 0
        },
        {
            "id": "konigsberg",
            "tier": "giveaway",
            "t": "Began in 1736, when Leonhard Euler showed that no walk could cross each of Königsberg’s seven bridges exactly once",
            "k": ["euler", "königsberg", "seven bridges", "1736"],
            "n": 0,
            "rabbit": "Leonhard Euler"
        },
        {
            "id": "four-color",
            "tier": "giveaway",
            "t": "Four color theorem: four colors are always enough to fill in any flat map so that no two neighboring regions match",
            "k": ["four color theorem", "neighboring regions"],
            "n": 0,
            "rabbit": "The number four"
        },
        {
            "id": "applications",
            "tier": "giveaway",
            "t": "Models social networks, road maps, airline routes, and the internet",
            "k": ["social networks", "airline routes", "internet"],
            "n": 0
        },
        {
            "id": "degree",
            "tier": "middle",
            "t": "A vertex’s degree is how many edges touch it; all the degrees add up to twice the number of edges (the handshake lemma)",
            "k": ["degree", "twice", "handshake lemma"],
            "n": 0
        },
        {
            "id": "euler-path",
            "tier": "middle",
            "t": "A path using every edge exactly once (an Euler path) needs zero or two odd-degree vertices; one that returns to its start (an Euler circuit) needs zero",
            "k": ["euler path", "euler circuit", "odd-degree"],
            "n": 0
        },
        {
            "id": "odd-bridges",
            "tier": "middle",
            "t": "Königsberg’s four land areas touched 5, 3, 3, and 3 bridges, all odd numbers, so the walk was impossible",
            "k": ["land areas", "all odd"],
            "n": 0
        },
        {
            "id": "pencil",
            "tier": "middle",
            "t": "Drawing a figure in one stroke, without lifting your pencil or retracing a line, is the same puzzle as finding an Euler path",
            "k": ["one stroke", "pencil"],
            "n": 0
        },
        {
            "id": "trees",
            "tier": "middle",
            "t": "A tree is a connected network with no cycles (loops); a tree with n vertices always has n − 1 edges",
            "k": ["tree", "cycles", "n − 1"],
            "n": 0
        },
        {
            "id": "six-degrees",
            "tier": "middle",
            "t": "“Six degrees of separation”: any two people may be linked by a short chain of acquaintances, as in the Kevin Bacon game",
            "k": ["six degrees", "separation", "kevin bacon"],
            "n": 0
        },
        {
            "id": "planar",
            "tier": "middle",
            "t": "Planar networks can be drawn on flat paper with no crossing edges",
            "k": ["planar", "crossing"],
            "n": 0
        },
        {
            "id": "complete",
            "tier": "middle",
            "t": "A complete network joins every pair of vertices; the one with 5 vertices has 10 edges",
            "k": ["complete", "every pair", "10 edges"],
            "n": 0
        },
        {
            "id": "sylvester",
            "tier": "power",
            "t": "James Joseph Sylvester introduced the name of its main objects in 1878, comparing them to chemists’ drawings of molecules",
            "k": ["sylvester", "1878", "molecules"],
            "n": 0
        },
        {
            "id": "konig",
            "tier": "power",
            "t": "Dénes Kőnig wrote the field’s first textbook in 1936, exactly 200 years after Euler’s bridges paper",
            "k": ["kőnig", "textbook", "1936"],
            "n": 0
        },
        {
            "id": "guthrie",
            "tier": "power",
            "t": "Francis Guthrie first guessed the four color rule in 1852 while coloring a map of England’s counties",
            "k": ["guthrie", "1852", "counties"],
            "n": 0
        },
        {
            "id": "appel-haken",
            "tier": "power",
            "t": "Kenneth Appel and Wolfgang Haken proved the four color theorem in 1976; it was the first major theorem proved with a computer’s help",
            "k": ["appel", "haken", "computer", "1976"],
            "n": 0
        },
        {
            "id": "utilities",
            "tier": "power",
            "t": "Three utilities puzzle: joining three houses to water, gas, and electricity with no crossings is impossible on a flat sheet; so is joining 5 points all to one another",
            "k": ["three utilities", "flat sheet"],
            "n": 0
        },
        {
            "id": "ramsey",
            "tier": "power",
            "t": "Ramsey theory: at any party of six people, some three all know one another or some three are all strangers",
            "k": ["ramsey", "party of six", "strangers"],
            "n": 0
        },
        {
            "id": "hamilton",
            "tier": "power",
            "t": "A Hamiltonian path visits every vertex once; Hamilton’s Icosian game (1857) used a dodecahedron, and the traveling salesman problem seeks the shortest such round trip",
            "k": ["hamiltonian", "icosian", "traveling salesman"],
            "n": 0
        },
        {
            "id": "erdos",
            "tier": "power",
            "t": "A mathematician’s Erdős number counts co-author links to Paul Erdős, who wrote about 1,500 papers",
            "k": ["erdős number", "co-author"],
            "n": 0
        },
        {
            "id": "milgram",
            "tier": "power",
            "t": "Stanley Milgram’s 1967 small-world experiment passed letters through chains of acquaintances; the chains that finished took about six steps",
            "k": ["milgram", "small-world", "1967"],
            "n": 0
        },
        {
            "id": "euler-formula",
            "tier": "power",
            "t": "Drawn with no crossings, a connected network has vertices − edges + regions = 2 (a cube’s outline: 8 − 12 + 6 = 2)",
            "k": ["regions", "8 − 12 + 6 = 2"],
            "n": 0
        },
        {
            "id": "dijkstra",
            "tier": "power",
            "t": "Edsger Dijkstra’s algorithm finds the shortest path through a weighted network (numbers on the edges), like a GPS app",
            "k": ["dijkstra", "weighted", "gps"],
            "n": 0
        },
        {
            "id": "chromatic",
            "tier": "power",
            "t": "The chromatic number is the fewest colors needed so that no edge joins two same-colored vertices; it helps schedule exams",
            "k": ["chromatic number", "fewest colors", "schedule exams"],
            "n": 0
        },
        {
            "id": "adjacency",
            "tier": "power",
            "t": "An adjacency matrix of 0s and 1s records which pairs of vertices are joined; Google’s PageRank treated the web as pages joined by links",
            "k": ["adjacency matrix", "pagerank"],
            "n": 0,
            "rabbit": "Matrices"
        },
        {
            "id": "directed",
            "tier": "power",
            "t": "Directed networks have one-way edges, like one-way streets or a food web’s arrows from prey to predator",
            "k": ["directed", "one-way", "food web"],
            "n": 0
        }
    ],
    "trap": {
        "title": "Not that kind of graph",
        "body": "In this field, a “graph” means dots (vertices) joined by lines (edges), not the graph of a function like y = 2x + 1 on a coordinate grid, so answers like “graph of a function” or “bar graph” are wrong. Group theory and set theory sound alike but are separate answer lines, and a tossup about Euler’s life wants the man, not the field.",
        "fix": "Listen for vertices, edges, nodes, networks, Königsberg’s bridges, map coloring, or trees: say “graph theory.” Saying only “network theory” earns a prompt, so be ready to add “graph theory.”",
        "line": "Real answer line: <b><u>graph</u></b> theory (accept <u>graph</u>s; prompt on <u>network</u>s or <u>network theory</u>; do not accept “graphs of functions”)"
    }
}

with open("topics/graph-theory.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote topics/graph-theory.json")
