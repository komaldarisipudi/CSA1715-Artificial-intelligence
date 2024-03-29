:- dynamic visited/1.

% best_first_search(+Start, +Goal, +Edges, +Heuristic, -Path, -Cost)
best_first_search(Start, Goal, Edges, Heuristic, Path, Cost) :-
    heuristic(Start, Goal, H),
    best_first_search_helper([(H, Start)], Goal, Edges, Heuristic, [Start], Path, Cost).

best_first_search_helper([(Cost, Node)|_], Goal, _, _, Path, [Node|Path], Cost) :-
    Node == Goal, !.

best_first_search_helper([(Cost, Node)|RestQueue], Goal, Edges, Heuristic, Visited, Path, TotalCost) :-
    findall((NewCost, Neighbor), (member((Node, Neighbor, EdgeCost), Edges),
                                 \+ member(Neighbor, Visited),
                                 heuristic(Neighbor, Goal, H),
                                 NewCost is Cost + EdgeCost + H),
            NeighborCostList),
    append(NeighborCostList, RestQueue, NewQueue),
    sort(NewQueue, SortedQueue),
    best_first_search_helper(SortedQueue, Goal, Edges, Heuristic, [Node|Visited], Path, TotalCost).

% Example Heuristic function
% heuristic(+Node, +Goal, -H)
% Define your own heuristic function based on your problem domain
heuristic(_, _, 0).

% Example graph edges
% graph_edge(Node1, Node2, Cost)
% Define your own graph edges based on your problem domain
graph_edge(a, b, 1).
graph_edge(a, c, 2).
graph_edge(b, d, 3).
graph_edge(c, e, 2).
graph_edge(d, e, 1).
graph_edge(e, f, 3).

% Example query:
% ?- best_first_search(a, f, [(a,b,1),(a,c,2),(b,d,3),(c,e,2),(d,e,1),(e,f,3)], heuristic, Path, Cost).
