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

def searchAlgorithm(problemState,stack,searchType,heuristic = None):
    visitedState = dict()
    state = problemState.getStartState()       
    node = {}
    node["parent"] = None
    node["action"] = None
    node["state"] = state
    if searchType == 'ucs' or searchType == 'astar':
        #introduction of cost as a part of ucs & a*
        node["cost"] = 0
    #check to push the date into the stack
    if searchType == 'ucs':
        stack.push(node, node["cost"])
    elif searchType == 'astar':
        node["evaluate"] = heuristic(state, problemState)
        # here 0 is node["cost"]
        stack.push(node, 0 + node["evaluate"])
    else:
        stack.push(node)
    while not stack.isEmpty():
        node = stack.pop()
        state = node["state"]
        if searchType == 'ucs' or searchType == 'astar':
            cost = node["cost"]
        if searchType == 'astar':
            eval = node["evaluate"]
        if state in visitedState:
          continue
        visitedState[state] = True

        if problemState.isGoalState(state) == True:
          break   
        for child in problemState.getSuccessors(state):
            if (child[0]) not in visitedState:
                neighbourNode = {}
                neighbourNode["parent"] = node
                neighbourNode["action"] = child[1]
                neighbourNode["state"] = child[0]
                if searchType == 'ucs':
                    neighbourNode["cost"] = child[2] + cost
                    stack.push(neighbourNode, neighbourNode["cost"])
                elif searchType == 'astar':
                    # f(x) = h(x) + g(x) as per the heuristic a* formula
                    neighbourNode["cost"] = child[2] + cost
                    neighbourNode["evaluate"] = heuristic(neighbourNode["state"], problemState)
                    stack.push(neighbourNode, neighbourNode["cost"] + neighbourNode["evaluate"])
                else:
                    stack.push(neighbourNode)
    actions = []
    while node["action"] != None:
        actions.insert(0, node["action"])
        node = node["parent"]

    return actions

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    dataStack = util.Stack()
    return searchAlgorithm(problem,dataStack,'dfs')

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    dataQueue = util.Queue()
    return searchAlgorithm(problem,dataQueue,'bfs')

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    dataPriorityQueue = util.PriorityQueue()
    return searchAlgorithm(problem,dataPriorityQueue,'ucs')

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    dataAQueue = util.PriorityQueue()
    return searchAlgorithm(problem,dataAQueue,'astar',heuristic)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
