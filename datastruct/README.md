#LRU

    To solve this problem I used LinkedList and built-in dict structure.

    LinkedList is good in deleating and inserting we can do it in O(1).

    And Dict good in searching.
    In case of huge amount of data and heigh capacity and collisions we can use HashTable.

    get, set: time: O(1)
    space: O(n)

#FileRecursion

    time: O(log(n))- because recursion, worst case O(n)

    For space complecity - same. In woth case we sill save names of all dirs in memory
    space: O(log(n)) - worst case O(n)

#HuffmanCoding

    We should iterate through all characters thats why time complecity is O(n)
    When we build priority queue time complexity is O(n \* log(n))
    Time complecity of getting codes O(n)

    encoding time: O(n \* log(n))

    With decoding we shou;d iterate through all bytes
    decoding time: o(n)

    space: O(n)

#ActiveDirectory

    In worst case we will iterate throuth all nodes, and build result arrays (leaf nodes) times

    Example:
        g1
      /  |  \
    g2   g3  g4
    /\    |\  \

g5 g6 g7 g8 g9

    incase if we dont have user we should iterate through each group

    result: [[g1, g2, g5], [g1, g2, g6], [g1, g3, g7], [g1, g3, g8],[g1, g4, g9]]

    time: O(n)
    space: O(n)

    PS. Previous reviewer point that here is O(n) time and space complecity
    I'm not sure

#Blockchain

    Time to create and Add block is constant
    It will take as much space as many nodes we have

    time: O(1)
    space: O(n)

#UnionAndIntersection

    in worst cases we shoul iterate throuh both input lists
    and then create result one

    time: O(n)
    space: O(n)
