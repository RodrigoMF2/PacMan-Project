# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    stack = util.Stack()
    visited = set()
    start = problem.getStartState()
    stack.push((start, []))
    while not stack.isEmpty():
        state, action1 = stack.pop()
        if problem.isGoalState(state):
            return action1
        visited.add(state)
        child = problem.getSuccessors(state)
        for successor, action, _ in child:
            if successor not in visited:
                new = action1 + [action]
                stack.push((successor, new))

    return []


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    # inicializa a fila para a busca em pronfudidade
    queue = util.Queue()

    # Criar um conjunto para rastear os nós vizinhos
    visited = set()

    # Comece com o estado inicial do problema
    start_stade = problem.getStartState()

    # empurre o estado inicial para a fila com uma lista vazia de açoes
    queue.push((start_stade, []))

    # enquanto a fila nao estiver vazia
    while not queue.isEmpty():
        state, actions = queue.pop() #

        # verifique se o estado atual é o objetivo
        if problem.isGoalState(state):
            return actions

        # obtenha os sucessores do estado atual
        if state not in visited:
            successors = problem.getSuccessors(state)
            for successor, action, _ in successors:
                    new_actions = actions + [action]
                    queue.push((successor, new_actions))

        # marque o estado atual como visitado
        visited.add(state)
    # se nao encontrarmo uma soluçao, retornaremos uma lista vazia
    return []



    # util.raiseNotDefined()

# function BREADTH - FIRST - SEARCH(problem)returns a solution node or failure
def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    # inicializa uma fila para a busca em pronfudidade
    queue = util.PriorityQueue()

    # Criar um conjunto para rastear os nós vizinhos
    visited = set()

    # Comece com o estado inicial do problema
    start_stade = problem.getStartState()

    # empurre o estado inicial para a fila com uma lista vazia de açoes
    queue.push((start_stade, [], 0),0)

    while not queue.isEmpty():
        state, actions,my_value = queue.pop()

        # verifique se o estado atual é o objetivo
        if problem.isGoalState(state):
            return actions

        # obtenha os sucessores do estado atual
        if state not in visited:
            successors = problem.getSuccessors(state)
            for successor, action, value in successors:
                new_actions = actions + [action]
                queue.push((successor, new_actions,my_value + value), my_value + value)

        # marque o estado atual como visitado
        visited.add(state)
    # se nao encontrarmo uma soluçao, retornaremos uma lista vazia

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    # Inicializa a fila de prioridade para a busca A*
    pqueue = util.PriorityQueue()

    # Cria um conjunto para rastrear os nós visitados
    visited = set()

    # Comece com o estado inicial do problema
    start_state = problem.getStartState()

    # Empurre o estado inicial para a fila com uma lista vazia de ações e um custo acumulado inicial de 0
    pqueue.push((start_state, [], 0), 0)

    while not pqueue.isEmpty():
        state, actions, acomulated_cost = pqueue.pop()

        # Verifique se o estado atual é o objetivo
        if problem.isGoalState(state):
            return actions

        # Obtenha os sucessores do estado atual
        if state not in visited:
            successors = problem.getSuccessors(state)
            for successor, action, step_cost in successors:
                new_actions = actions + [action]
                # Calcula o custo total (custo acumulado até agora + custo do passo + estimativa heurística)
                total_cost = acomulated_cost + step_cost + heuristic(successor, problem)
                new_cost = acomulated_cost + step_cost
                pqueue.push((successor, new_actions, new_cost), total_cost)
        # Marque o estado atual como visitado
        visited.add(state)
    # Se não encontrarmos uma solução, retornaremos uma lista vazia
    return []


util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
