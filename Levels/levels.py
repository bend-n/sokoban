# Level data stolen from: https://www.mathsisfun.com/games/sokoban.html
# (https://www.mathsisfun.com/games/a/sokoban/js/maps.js)
maps=[[[0,0,1,1,1,1,1,0],[1,1,1,2,2,2,1,0],[1,3,6,4,2,2,1,0],[1,1,1,2,4,3,1,0],[1,3,1,1,4,2,1,0],[1,2,1,2,3,2,1,1],[1,4,2,5,4,4,3,1],[1,2,2,2,3,2,2,1],[1,1,1,1,1,1,1,1]],[[2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,1,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,1,4,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,1,1,1,2,2,4,1,1,1,2,2,2,2,2,2,2,2,2,2,2],[2,2,1,2,2,4,2,2,4,2,1,2,2,2,2,2,2,2,2,2,2,2],[1,1,1,2,1,2,1,1,1,2,1,2,2,2,2,2,1,1,1,1,1,1],[1,2,2,2,1,2,1,1,1,2,1,1,1,1,1,1,1,2,2,3,3,1],[1,2,4,2,2,4,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,1],[1,1,1,1,1,2,1,1,1,1,2,1,6,1,1,1,1,2,2,3,3,1],[2,2,2,2,1,2,2,2,2,2,2,1,1,1,2,2,1,1,1,1,1,1],[2,2,2,2,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]],[[1,1,1,1,1,1,1,1,1,1,1,1,2,2],[1,3,3,2,2,1,2,2,2,2,2,1,1,1],[1,3,3,2,2,1,2,4,2,2,4,2,2,1],[1,3,3,2,2,1,4,1,1,1,1,2,2,1],[1,3,3,2,2,2,2,6,2,1,1,2,2,1],[1,3,3,2,2,1,2,1,2,2,4,2,1,1],[1,1,1,1,1,1,2,1,1,4,2,4,2,1],[2,2,1,2,4,2,2,4,2,4,2,4,2,1],[2,2,1,2,2,2,2,1,2,2,2,2,2,1],[2,2,1,1,1,1,1,1,1,1,1,1,1,1]],[[2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,2],[2,2,2,2,2,2,2,2,1,2,2,2,2,2,6,1,2],[2,2,2,2,2,2,2,2,1,2,4,1,4,2,1,1,2],[2,2,2,2,2,2,2,2,1,2,4,2,2,4,1,2,2],[2,2,2,2,2,2,2,2,1,1,4,2,4,2,1,2,2],[1,1,1,1,1,1,1,1,1,2,4,2,1,2,1,1,1],[1,3,3,3,3,2,2,1,1,2,4,2,2,4,2,2,1],[1,1,3,3,3,2,2,2,2,4,2,2,4,2,2,2,1],[1,3,3,3,3,2,2,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2]],[[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,3,3,3,3,1],[2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,3,3,1],[2,2,2,1,2,2,2,2,1,2,2,4,2,4,2,2,2,3,3,3,3,1],[2,2,2,1,2,4,4,4,1,4,2,2,4,2,1,2,2,3,3,3,3,1],[2,2,2,1,2,2,4,2,2,2,2,2,4,2,1,2,2,3,3,3,3,1],[2,2,2,1,2,4,4,2,1,4,2,4,2,4,1,1,1,1,1,1,1,1],[1,1,1,1,2,2,4,2,1,2,2,2,2,2,1,2,2,2,2,2,2,2],[1,2,2,2,1,2,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2],[1,2,2,2,2,4,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2],[1,2,4,4,1,4,4,2,6,1,2,2,2,2,2,2,2,2,2,2,2,2],[1,2,2,2,1,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2],[1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2]],[[2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2],[2,2,2,2,2,2,2,2,1,2,2,2,1,1,1,1,1],[2,2,2,2,2,2,2,2,1,2,1,4,1,1,2,2,1],[2,2,2,2,2,2,2,2,1,2,2,2,2,2,4,2,1],[1,1,1,1,1,1,1,1,1,2,1,1,1,2,2,2,1],[1,3,3,3,3,2,2,1,1,2,4,2,2,4,1,1,1],[1,3,3,3,3,2,2,2,2,4,2,4,4,2,1,1,2],[1,3,3,3,3,2,2,1,1,4,2,2,4,2,6,1,2],[1,1,1,1,1,1,1,1,1,2,2,4,2,2,1,1,2],[2,2,2,2,2,2,2,2,1,2,4,2,4,2,2,1,2],[2,2,2,2,2,2,2,2,1,1,1,2,1,1,2,1,2],[2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,1,2],[2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,2]],[[1,1,1,1,1,1,2,2,1,1,1,2],[1,3,3,2,2,1,2,1,1,6,1,1],[1,3,3,2,2,1,1,1,2,2,2,1],[1,3,3,2,2,2,2,2,4,4,2,1],[1,3,3,2,2,1,2,1,2,4,2,1],[1,3,3,1,1,1,2,1,2,4,2,1],[1,1,1,1,2,4,2,1,4,2,2,1],[2,2,2,1,2,2,4,1,2,4,2,1],[2,2,2,1,2,4,2,2,4,2,2,1],[2,2,2,1,2,2,1,1,2,2,2,1],[2,2,2,1,1,1,1,1,1,1,1,1]],[[2,2,2,2,2,2,2,1,1,1,1,1,2],[2,1,1,1,1,1,1,1,2,2,2,1,1],[1,1,2,1,2,6,1,1,2,4,4,2,1],[1,2,2,2,2,4,2,2,2,2,2,2,1],[1,2,2,4,2,2,1,1,1,2,2,2,1],[1,1,1,2,1,1,1,1,1,4,1,1,1],[1,2,4,2,2,1,1,1,2,3,3,1,2],[1,2,4,2,4,2,4,2,3,3,3,1,2],[1,2,2,2,2,1,1,1,3,3,3,1,2],[1,2,4,4,2,1,2,1,3,3,3,1,2],[1,2,2,1,1,1,2,1,1,1,1,1,2],[1,1,1,1,2,2,2,2,2,2,2,2,2]],[[2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2],[2,2,1,2,2,1,1,1,1,1,1,1,1,1,1,1],[2,2,1,2,2,2,2,4,2,2,2,4,2,4,2,1],[2,2,1,2,4,1,2,4,2,1,2,2,4,2,2,1],[2,2,1,2,2,4,2,4,2,2,1,2,2,2,2,1],[1,1,1,2,4,1,2,1,2,2,1,1,1,1,2,1],[1,6,1,4,2,4,2,4,2,2,1,1,2,2,2,1],[1,2,2,2,2,4,2,1,4,1,2,2,2,1,2,1],[1,1,2,2,4,2,2,2,2,4,2,4,2,4,2,1],[2,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1],[2,2,1,1,1,2,2,1,1,1,2,2,2,2,2,2],[2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,2],[2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,2],[2,2,1,3,3,3,3,3,3,1,2,2,2,2,2,2],[2,2,1,3,3,3,3,3,3,1,2,2,2,2,2,2],[2,2,1,3,3,3,3,3,3,1,2,2,2,2,2,2],[2,2,1,1,1,1,1,1,1,1,2,2,2,2,2,2]],[[2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2,2,1,2,2,3,3,3,1],[2,2,2,2,2,2,1,1,1,1,1,2,2,3,3,3,1],[2,2,2,2,2,2,1,2,2,2,2,2,2,3,3,3,1],[2,2,2,2,2,2,1,2,2,1,1,2,2,3,3,3,1],[2,2,2,2,2,2,1,1,2,1,1,2,2,3,3,3,1],[2,2,2,2,2,1,1,1,2,1,1,1,1,1,1,1,1],[2,2,2,2,2,1,2,4,4,4,2,1,1,2,2,2,2],[2,1,1,1,1,1,2,2,4,2,4,2,1,1,1,1,1],[1,1,2,2,2,1,4,2,4,2,2,2,1,2,2,2,1],[1,6,2,4,2,2,4,2,2,2,2,4,2,2,4,2,1],[1,1,1,1,1,1,2,4,4,2,4,2,1,1,1,1,1],[2,2,2,2,2,1,2,4,2,2,2,2,1,2,2,2,2],[2,2,2,2,2,1,1,1,1,2,1,1,1,2,2,2,2],[2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,2],[2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,2],[2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,2],[2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2]],[[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2],[2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,1,2,2,2],[2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,1,2,2,2],[2,2,2,2,2,2,2,2,2,1,2,2,1,1,1,1,2,1,1,1,2],[2,1,1,1,2,2,1,1,1,1,1,2,1,1,1,2,2,2,2,1,2],[1,1,6,1,1,1,1,2,2,2,4,4,4,2,1,2,2,2,2,1,2],[1,2,4,4,2,2,2,4,4,2,4,2,2,2,1,3,3,3,3,1,1],[1,2,2,4,4,4,1,2,2,2,2,4,2,2,1,3,3,3,3,3,1],[1,2,4,2,2,2,1,2,4,4,2,4,4,2,1,3,3,3,3,3,1],[1,1,1,2,2,2,1,2,2,4,2,2,2,2,1,3,3,3,3,3,1],[2,2,1,2,2,2,1,2,4,2,4,2,4,2,1,3,3,3,3,3,1],[2,2,1,2,1,1,1,1,1,1,1,2,1,1,1,3,3,3,3,3,1],[2,2,1,2,2,2,1,2,2,4,2,4,2,2,1,3,3,3,3,3,1],[2,2,1,1,1,2,1,2,4,4,2,4,2,4,1,1,1,1,1,1,1],[2,2,2,2,1,2,1,2,2,4,2,2,2,2,2,2,1,2,2,2,2],[2,2,2,2,1,2,1,2,4,4,4,2,4,4,4,2,1,2,2,2,2],[2,2,2,2,1,2,1,2,2,2,2,2,2,2,1,2,1,2,2,2,2],[2,2,2,2,1,2,1,1,1,1,1,1,1,1,1,2,1,2,2,2,2],[2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2],[2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2]],[[2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2],[2,2,2,2,2,1,1,1,1,2,1,2,2,1,2,2,2,2,2],[2,2,2,1,1,1,2,2,1,1,1,4,2,1,2,2,2,2,2],[2,2,1,1,2,2,2,6,2,2,4,2,2,1,2,2,2,2,2],[2,1,1,2,2,4,2,4,4,1,1,2,1,1,2,2,2,2,2],[2,1,2,2,1,4,1,1,2,2,2,2,2,1,2,2,2,2,2],[2,1,2,1,2,4,2,4,4,2,1,2,1,1,1,2,2,2,2],[2,1,2,2,2,4,2,1,2,2,1,2,4,2,1,1,1,1,1],[1,1,1,1,2,2,2,2,1,2,2,4,4,2,1,2,2,2,1],[1,1,1,1,2,1,1,2,4,2,2,2,2,2,2,2,2,2,1],[1,3,2,2,2,2,1,1,1,2,2,1,1,1,1,1,1,1,1],[1,3,3,2,3,3,1,2,1,1,1,1,2,2,2,2,2,2,2],[1,3,3,3,1,3,1,2,2,2,2,2,2,2,2,2,2,2,2],[1,3,3,3,3,3,1,2,2,2,2,2,2,2,2,2,2,2,2],[1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2]],[[2,2,1,1,1,1,1,1,1,1,1,2,2],[2,2,1,5,3,5,1,5,3,5,1,2,2],[2,2,1,3,5,3,5,3,5,3,1,2,2],[2,2,1,5,3,5,3,5,3,5,1,2,2],[2,2,1,3,5,3,5,3,5,3,1,2,2],[2,2,1,5,3,5,3,5,3,5,1,2,2],[2,2,1,1,1,2,2,2,1,1,1,2,2],[2,2,2,2,1,2,2,2,1,2,2,2,2],[1,1,1,1,1,1,2,1,1,1,1,1,1],[1,2,2,2,2,2,2,2,2,2,2,2,1],[1,2,4,2,4,2,4,2,4,2,4,2,1],[1,1,2,4,2,4,2,4,2,4,2,1,1],[2,1,4,2,4,2,4,2,4,2,4,1,2],[2,1,2,2,2,4,6,4,2,2,2,1,2],[2,1,2,2,1,1,1,1,1,2,2,1,2],[2,1,1,1,1,2,2,2,1,1,1,1,2]],[[2,2,2,2,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2],[2,2,1,1,1,2,2,2,1,1,2,2,1,1,1,1,1,2,2,2],[1,1,1,2,2,2,2,2,2,1,2,2,1,2,2,2,1,1,1,1],[1,2,2,4,4,2,1,4,2,1,2,2,1,2,2,3,3,3,2,1],[1,2,1,2,2,4,1,6,4,1,1,2,1,2,1,3,1,3,2,1],[1,2,2,1,1,2,1,4,2,2,1,2,2,2,2,3,3,3,2,1],[1,2,4,1,2,2,2,2,4,2,1,2,1,2,1,3,1,3,2,1],[1,2,2,2,2,1,1,2,2,1,1,4,2,4,2,3,3,3,2,1],[1,2,4,2,1,1,2,2,2,1,2,2,1,4,1,3,1,3,2,1],[1,1,2,4,4,2,2,4,2,2,2,4,2,2,4,3,3,3,2,1],[2,1,4,2,2,1,1,1,1,1,1,2,2,2,2,1,1,2,2,1],[2,1,2,2,2,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1],[2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2]],[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2],[1,2,1,2,1,1,1,1,1,1,2,2,2,2,2,1,2],[1,2,1,2,2,4,2,4,2,4,2,4,1,2,2,1,2],[1,2,1,2,2,2,4,6,4,2,2,2,1,1,2,1,1],[1,2,1,2,1,4,2,4,2,4,1,1,1,3,3,3,1],[1,2,1,2,2,2,4,2,4,2,2,1,1,3,3,3,1],[1,2,1,1,1,4,4,4,2,4,2,1,1,3,3,3,1],[1,2,2,2,2,2,1,2,1,1,2,1,1,3,3,3,1],[1,1,1,1,1,2,2,2,1,1,2,1,1,3,3,3,1],[2,2,2,2,1,1,1,1,1,2,2,2,2,2,1,1,1],[2,2,2,2,2,2,2,2,1,2,2,2,2,2,1,2,2],[2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,2,2]],[[2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2,2],[2,2,2,2,1,1,1,1,2,2,1,2,2,2,2,2,2],[2,2,2,1,1,2,2,1,2,2,1,2,2,2,2,2,2],[2,2,2,1,2,2,4,2,4,2,1,2,2,2,2,2,2],[2,1,1,1,2,1,4,2,2,2,1,1,1,1,2,2,2],[2,1,2,2,4,2,2,1,1,4,2,2,2,1,2,2,2],[2,1,2,2,1,2,6,2,4,2,1,2,4,1,2,2,2],[2,1,2,2,1,2,2,2,2,2,2,4,2,1,1,1,1],[2,1,1,2,1,1,1,1,4,1,1,2,2,2,2,2,1],[2,1,2,4,1,3,3,3,3,3,1,2,1,2,2,2,1],[2,1,2,2,4,3,3,3,5,3,2,4,1,2,1,1,1],[1,1,2,2,1,3,3,3,3,3,1,2,2,2,1,2,2],[1,2,2,2,1,1,1,2,1,1,1,1,1,1,1,2,2],[1,2,4,4,2,2,1,2,2,1,2,2,2,2,2,2,2],[1,2,2,1,2,2,2,2,2,1,2,2,2,2,2,2,2],[1,1,1,1,1,1,2,2,2,1,2,2,2,2,2,2,2],[2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2]],[[1,1,1,1,1,2,2,2,2,2,2,2,2,2],[1,2,2,2,1,1,2,2,2,2,2,2,2,2],[1,2,2,2,2,1,2,2,1,1,1,1,2,2],[1,2,4,2,2,1,1,1,1,2,2,1,2,2],[1,2,2,4,4,2,4,2,2,2,4,1,2,2],[1,1,1,6,2,1,4,2,2,2,2,1,1,2],[2,1,2,2,1,1,2,2,4,2,4,2,1,1],[2,1,2,4,2,2,1,1,2,1,1,2,3,1],[2,1,2,2,1,4,1,1,4,2,2,1,3,1],[2,1,1,1,2,2,2,4,3,3,1,1,3,1],[2,2,1,2,2,2,2,1,3,5,3,3,3,1],[2,2,1,2,4,4,2,1,3,3,3,3,3,1],[2,2,1,2,2,1,1,1,1,1,1,1,1,1],[2,2,1,2,2,1,2,2,2,2,2,2,2,2],[2,2,1,1,1,1,2,2,2,2,2,2,2,2]],[[2,2,2,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2],[2,1,1,1,1,1,1,1,2,2,2,2,2,1,2,2,2,2],[2,1,2,2,2,2,2,1,2,4,6,4,2,1,2,2,2,2],[2,1,4,4,2,1,2,2,2,1,1,1,1,1,1,1,1,1],[2,1,2,1,1,1,3,3,3,3,3,3,1,1,2,2,2,1],[2,1,2,2,2,4,3,3,3,3,3,3,1,1,2,1,2,1],[2,1,2,1,1,1,3,3,3,3,3,3,2,2,2,2,2,1],[1,1,2,2,2,1,1,1,1,2,1,1,1,2,1,4,1,1],[1,2,2,1,4,2,2,2,1,2,2,4,2,2,1,2,1,2],[1,2,2,4,2,4,4,4,2,2,1,2,4,1,1,2,1,2],[1,2,2,2,4,2,4,2,1,1,1,4,4,2,1,2,1,2],[1,1,1,1,1,2,2,2,2,2,4,2,2,2,1,2,1,2],[2,2,2,2,1,1,1,2,1,1,1,2,2,2,1,2,1,2],[2,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,1,2],[2,2,2,2,2,2,1,1,1,1,1,1,1,1,2,2,1,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2]],[[2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2],[2,2,2,2,2,2,1,2,2,3,2,2,1,1,2,2,2,1,2,2,2,2],[2,2,2,2,2,2,1,2,1,3,2,2,2,2,2,6,2,1,2,2,2,2],[2,1,1,1,1,1,1,2,1,1,3,3,3,1,2,1,1,1,1,2,2,2],[1,1,2,2,1,1,3,3,3,1,1,1,1,2,2,2,2,2,1,1,1,1],[1,2,4,2,1,1,3,3,3,2,2,2,2,4,2,1,2,2,4,2,2,1],[1,2,2,2,2,2,3,3,2,1,1,2,1,2,1,1,2,1,1,2,2,1],[1,1,1,1,4,1,1,1,4,1,2,4,2,2,1,2,2,2,1,2,1,1],[2,1,1,1,2,2,1,2,2,2,2,1,1,4,2,4,4,2,1,2,1,2],[2,1,2,2,2,4,4,2,1,2,1,2,4,2,1,2,4,1,1,2,1,2],[2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2],[2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2]],[[2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,1,2,2,2,6,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,1,1,1,1,1,2,4,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,1,2,2,2,1,1,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,1,2,4,1,1,2,2,1,1,2,2,2,2,1,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,1,2,2,2,1,2,2,1,1,1,1,1,2,1,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,1,2,1,4,4,2,4,2,2,2,2,1,2,1,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,1,2,2,4,2,4,2,1,1,1,2,1,2,1,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,1,2,1,2,2,2,4,2,2,1,2,1,2,1,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,1,2,1,2,2,1,4,1,2,2,2,1,2,1,2,2,2,2,2,2,2,2],[2,2,2,2,2,1,1,2,1,1,1,1,2,2,2,1,2,1,2,1,2,2,2,2,2,2,2,2],[2,2,2,2,2,1,2,2,4,2,2,1,1,1,1,1,2,1,2,1,2,1,1,1,1,2,2,2],[2,2,2,2,1,1,2,2,2,2,4,2,2,2,2,2,4,2,2,1,1,1,2,2,1,1,1,1],[1,1,1,1,1,2,2,1,1,1,2,4,2,4,1,2,4,2,1,2,2,2,3,3,3,3,3,1],[1,2,2,2,2,2,1,1,2,2,2,2,2,2,1,2,2,1,1,2,2,1,3,3,3,3,3,1],[1,2,4,4,4,4,2,2,2,2,1,1,1,1,1,1,4,1,1,2,2,2,1,3,1,1,3,1],[1,1,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,3,3,3,3,1],[2,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,3,3,3,3,1],[2,2,1,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,1,1],[2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2]],[[2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],[2,2,2,2,2,2,2,1,3,3,3,3,3,3,3,3,3,3,1,2],[2,2,2,2,2,1,1,1,3,1,3,1,3,1,3,1,3,3,1,2],[2,2,2,2,2,1,2,2,2,3,3,3,3,3,3,3,3,3,1,2],[2,2,2,2,2,1,6,2,4,2,4,2,4,2,5,3,5,3,1,2],[2,2,2,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2],[2,1,1,1,1,2,2,2,1,2,2,2,2,1,1,2,2,1,2,2],[1,1,2,2,2,2,4,2,1,2,2,2,2,1,2,4,2,1,1,2],[1,2,2,1,4,1,2,1,1,1,2,1,1,1,4,2,2,2,1,1],[1,2,4,2,2,4,2,4,2,2,2,1,2,4,2,4,2,4,2,1],[1,2,2,1,2,4,2,1,1,2,2,2,2,2,2,2,1,4,2,1],[1,2,2,2,4,1,1,1,1,4,1,1,1,1,4,1,1,2,2,1],[1,1,1,1,2,2,1,1,2,2,2,1,2,2,2,2,1,2,2,1],[2,2,2,1,4,2,1,1,2,2,2,1,2,1,2,4,4,2,2,1],[2,2,2,1,2,2,2,1,2,4,2,1,2,2,4,2,2,2,2,1],[2,2,2,1,1,1,2,1,2,4,4,2,1,2,2,4,2,1,1,1],[2,2,2,2,2,1,2,1,2,2,2,2,1,2,4,2,1,1,2,2],[2,2,2,2,2,1,2,1,1,1,1,1,1,1,1,2,1,2,2,2],[2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,1,2,2,2],[2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2]],[[2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2],[2,2,2,1,3,3,2,2,1,2,2,2,1,2,2,2],[2,2,2,1,3,3,2,2,2,2,2,2,1,2,2,2],[2,2,2,1,3,3,2,2,1,2,2,1,1,1,1,2],[2,2,1,1,1,1,1,1,1,2,2,1,2,2,1,1],[2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,1],[2,2,1,2,2,1,2,2,1,1,2,2,1,2,2,1],[1,1,1,1,2,1,1,2,2,1,1,1,1,2,1,1],[1,2,2,4,2,2,1,1,1,1,1,2,1,2,2,1],[1,2,1,2,4,2,2,4,2,2,1,2,4,2,2,1],[1,2,6,4,2,2,4,2,2,2,1,2,2,2,1,1],[1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,2],[2,2,2,1,2,2,2,2,1,2,2,2,2,2,2,2],[2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2]],[[2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2,2],[2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,2,2],[2,1,2,2,2,2,1,2,2,1,2,2,4,2,2,1,2,2,2,1,1,2],[2,1,2,4,2,4,2,4,2,2,4,2,1,2,4,2,4,2,2,2,1,2],[2,1,1,4,2,4,2,2,2,1,2,6,1,2,4,2,2,2,4,2,1,2],[1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2],[1,2,2,4,2,4,1,2,2,1,3,3,3,3,3,3,1,2,4,1,2,2],[1,2,1,2,2,2,1,2,2,1,3,3,3,3,3,3,1,1,2,1,2,2],[1,2,2,1,1,2,1,1,2,1,2,3,3,3,3,3,1,2,2,1,2,2],[1,2,1,2,2,2,2,2,2,4,3,3,3,3,3,3,2,4,2,1,2,2],[1,2,1,2,4,2,1,1,2,1,3,3,3,3,3,3,1,2,2,1,2,2],[1,2,2,4,2,4,1,2,2,1,3,3,3,3,3,3,1,2,4,1,2,2],[1,2,4,2,2,2,1,2,2,1,1,4,1,1,1,1,1,2,2,1,2,2],[1,2,4,2,4,2,1,1,1,1,2,4,2,4,2,2,4,2,4,1,2,2],[1,1,2,1,2,2,2,2,2,4,2,4,2,4,2,4,2,2,2,1,1,1],[2,1,2,2,1,1,1,1,1,1,2,4,2,2,2,2,4,2,2,2,2,1],[2,1,2,2,2,2,2,2,2,2,2,1,2,1,1,1,1,1,1,1,2,1],[2,1,1,1,1,1,1,1,2,1,4,2,2,2,2,2,2,2,2,2,2,1],[2,2,2,2,2,2,2,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]],[[2,2,2,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,1,2,2,1,2,2,1,1,1,1,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,1,2,4,1,4,2,1,2,2,1,1,2,2,2,2,2,2,2],[1,1,1,1,1,1,1,1,2,2,1,2,2,1,2,2,2,1,1,1,1,1,1,1,1],[1,3,3,3,3,2,2,1,2,4,1,4,2,1,2,2,4,1,2,2,1,2,2,2,1],[1,3,3,3,3,1,2,1,2,2,2,2,2,1,4,2,2,1,2,2,2,2,2,2,1],[1,3,3,1,3,2,2,2,2,4,1,2,2,1,2,4,2,2,2,2,1,4,2,2,1],[1,3,3,3,2,6,1,1,2,2,1,4,2,1,4,2,2,1,2,2,1,2,2,2,1],[1,3,3,3,3,2,1,1,2,4,1,2,2,2,2,2,4,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,2,2,1,4,4,1,4,2,2,1,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,1,2,4,1,2,2,1,2,2,4,1,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,1,2,2,1,2,2,1,2,2,2,1,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,1,1,1,1,2,2,1,1,1,1,1,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2]],[[2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2],[2,2,2,1,3,3,3,3,3,3,3,3,1,1,1,1,2,2,2,2,2],[2,2,2,1,3,1,3,1,3,3,3,3,1,2,2,1,2,2,2,2,2],[2,2,2,1,3,3,3,3,3,3,3,3,4,4,2,1,2,2,2,2,2],[2,2,2,1,2,2,2,2,2,3,1,1,1,2,2,1,1,1,1,2,2],[2,1,1,1,1,1,1,1,1,1,2,2,4,2,1,2,2,2,1,2,2],[2,1,2,2,2,2,2,4,2,2,2,4,2,4,2,2,4,2,1,2,2],[2,1,2,2,1,2,2,2,2,1,2,2,4,2,4,1,2,2,1,2,2],[2,1,1,2,1,1,1,1,1,2,2,2,1,2,2,1,2,2,1,2,2],[2,1,2,4,2,2,2,2,2,1,2,2,2,1,1,1,1,2,1,2,2],[1,1,2,2,4,1,2,2,2,1,2,1,1,2,2,1,2,2,1,2,2],[1,2,2,2,2,1,1,4,1,1,1,2,2,2,2,1,2,2,1,1,2],[1,2,4,2,2,2,2,4,2,1,2,2,1,2,2,1,2,2,2,1,2],[1,1,1,1,1,2,2,2,2,1,2,1,1,2,1,2,1,1,2,1,1],[2,2,2,2,1,4,1,2,1,2,2,4,2,2,4,2,4,2,2,2,1],[2,2,2,2,1,6,1,2,2,4,1,4,4,4,2,2,1,2,2,2,1],[2,2,2,2,1,1,1,2,2,4,2,2,2,2,2,2,1,1,1,1,1],[2,2,2,2,2,2,1,1,2,2,1,2,2,1,2,2,1,2,2,2,2],[2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2]],[[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,1,1,1,1,1],[2,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2,2,2,1,2,2,2,1],[2,2,2,2,1,2,2,2,2,2,2,4,2,4,2,1,1,2,1,2,1,2,1],[2,2,2,2,1,2,2,1,1,1,1,2,4,2,2,1,2,2,2,2,2,3,1],[2,2,2,2,1,2,2,2,2,2,2,4,2,1,2,1,2,1,1,3,1,3,1],[2,2,2,2,1,1,4,1,1,1,1,4,2,4,2,4,2,1,1,3,1,3,1],[2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,1,1,1,1,3,1,1,1],[2,2,2,2,1,2,4,2,2,2,1,1,1,1,1,1,2,2,1,3,1,3,1],[1,1,1,1,1,1,4,4,4,1,1,2,2,2,2,2,2,6,1,3,1,3,1],[1,2,2,2,2,2,2,1,2,2,2,2,1,4,1,4,1,1,1,3,2,3,1],[1,2,1,1,1,1,2,1,4,4,4,4,4,2,2,2,2,1,2,3,3,3,1],[1,2,1,2,2,2,2,4,2,2,2,2,2,1,2,2,2,1,2,3,3,3,1],[1,2,1,2,2,2,1,1,2,1,1,2,2,2,2,2,1,1,1,3,3,3,1],[1,2,1,1,1,1,1,1,4,1,1,1,1,1,1,2,2,1,1,1,1,1,1],[1,2,2,2,2,2,2,2,2,1,2,2,2,2,1,2,2,1,2,2,2,2,2],[1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,1,2,2,2,2,2]],[[1,1,1,1,1,1,1,1,1,2,2,2,2,2,2],[1,2,2,2,2,2,2,2,1,2,2,2,2,2,2],[1,2,2,2,2,2,2,2,1,1,1,1,2,2,2],[1,1,2,1,1,1,1,2,1,2,2,1,2,2,2],[1,1,2,1,6,1,1,2,2,2,2,1,2,2,2],[1,2,4,4,4,2,4,2,2,4,4,1,2,2,2],[1,2,2,1,2,1,1,2,4,2,2,1,2,2,2],[1,2,2,1,2,1,1,2,2,4,2,1,1,1,1],[1,1,1,1,2,2,4,4,4,2,4,1,2,2,1],[2,1,2,2,2,1,1,2,2,2,3,3,3,3,1],[2,1,2,1,2,2,2,1,2,1,3,3,2,3,1],[2,1,2,2,2,1,2,1,2,1,1,3,3,3,1],[2,1,1,1,1,1,2,4,2,2,1,3,3,3,1],[2,2,2,2,2,1,1,2,2,2,1,1,1,1,1],[2,2,2,2,2,2,1,1,1,1,1,2,2,2,2]],[[2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2],[2,1,3,3,3,2,2,2,1,2,2,2,2,1,2,2,2,1,1,1,2,2,2],[1,1,3,3,3,3,3,2,2,4,1,1,2,1,2,1,2,4,2,1,2,2,2],[1,3,3,3,3,3,3,1,2,2,4,2,2,1,2,2,4,2,2,1,2,2,2],[1,3,3,3,3,3,3,1,2,2,1,2,2,1,2,1,2,1,2,1,1,2,2],[1,1,1,1,1,1,1,1,1,2,4,2,2,4,2,1,2,1,2,2,1,1,1],[2,2,1,2,2,2,2,2,1,4,1,1,4,2,1,1,2,1,1,2,2,2,1],[2,1,1,2,2,2,4,2,2,2,2,1,2,4,2,2,4,2,2,2,1,2,1],[2,1,2,2,1,1,2,1,1,1,2,1,2,2,1,1,1,1,1,4,1,2,1],[2,1,2,4,2,4,4,2,2,2,2,2,4,2,2,2,4,2,2,2,2,2,1],[2,1,2,4,2,2,2,2,4,1,1,4,2,1,1,1,1,1,1,1,1,2,1],[2,1,1,1,1,1,1,1,2,2,6,2,1,1,2,2,2,2,2,2,1,1,1],[2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]],[[2,2,2,2,2,1,1,1,1,1,1,1,2,2,2],[2,2,2,2,2,1,6,2,1,2,2,1,2,2,2],[2,2,2,2,2,1,2,4,2,2,2,1,2,2,2],[2,2,2,2,1,1,1,2,1,1,2,1,2,2,2],[2,1,1,1,1,2,4,2,2,1,2,1,1,2,2],[2,1,2,2,2,2,2,2,2,1,2,2,1,1,2],[2,1,2,4,2,4,1,1,1,1,2,4,2,1,2],[2,1,2,4,4,2,1,2,2,1,2,2,4,1,2],[2,1,4,2,2,4,2,2,2,1,4,2,2,1,2],[1,1,2,2,4,4,1,2,2,2,4,4,2,1,1],[1,2,4,4,2,2,1,2,2,1,2,2,4,2,1],[1,2,2,2,2,2,1,1,1,1,2,4,2,2,1],[1,2,2,1,4,1,1,3,3,1,1,2,2,2,1],[1,1,1,2,3,1,3,3,3,3,1,1,1,1,1],[2,2,1,2,3,3,3,3,3,3,3,1,1,2,2],[2,2,1,3,3,3,3,2,2,2,3,3,1,2,2],[2,2,1,1,1,1,1,1,1,1,1,1,1,2,2]],[[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2],[2,2,2,2,2,2,2,1,1,1,1,1,1,2,1,1,1,2,2,2,1,1,1,1],[2,2,2,1,1,1,1,1,2,2,2,2,1,1,1,2,4,2,4,2,2,4,2,1],[1,1,1,1,2,2,1,1,2,1,4,2,4,2,2,2,2,4,2,1,2,2,2,1],[1,3,3,3,3,2,2,2,4,4,2,4,2,4,2,2,4,2,2,2,1,4,1,1],[1,3,3,2,1,2,1,1,2,1,2,2,2,1,1,1,4,1,1,2,1,2,2,1],[1,3,3,3,3,2,2,2,2,1,2,1,1,1,2,2,2,2,1,2,2,2,2,1],[1,3,3,3,3,2,2,2,2,1,2,1,1,2,2,4,2,2,1,1,1,4,2,1],[1,3,3,1,1,1,1,1,1,2,2,4,2,2,1,2,2,1,1,1,1,2,1,1],[1,1,1,1,2,2,2,2,1,2,2,2,1,1,1,2,2,2,2,6,2,2,1,2],[2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]],[[2,1,1,1,1,1,2,2,2,2,2,2,2,2],[2,1,2,2,2,1,1,1,1,1,1,1,2,2],[2,1,2,4,2,1,1,1,2,2,2,1,2,2],[2,1,2,4,2,2,2,2,4,4,2,1,2,2],[2,1,1,2,1,1,1,1,2,2,2,1,2,2],[1,1,1,2,1,2,2,1,2,1,1,1,2,2],[1,2,2,2,1,2,2,1,6,1,1,2,2,2],[1,2,4,4,2,2,2,2,4,2,1,2,2,2],[1,2,2,2,1,2,1,2,4,2,1,1,1,1],[1,1,1,1,1,2,1,2,2,2,1,2,2,1],[2,1,2,2,2,4,1,1,1,1,2,2,2,1],[2,1,2,2,4,2,2,2,2,2,4,2,2,1],[2,1,1,2,2,2,1,1,1,1,1,2,1,1],[2,1,1,1,1,1,1,1,1,1,1,2,2,1],[1,1,3,3,3,3,1,2,4,2,2,4,2,1],[1,3,3,3,3,3,1,2,4,4,1,2,2,1],[1,3,3,2,3,3,1,2,4,2,2,4,2,1],[1,3,3,3,3,3,4,2,2,2,1,2,2,1],[1,1,2,2,1,1,1,1,1,1,1,1,1,1],[2,1,1,1,1,2,2,2,2,2,2,2,2,2]],[[2,1,1,1,1,1,1,1,2,2,2,2,2,2,2],[2,1,2,2,1,2,2,1,1,1,1,1,2,2,2],[1,1,2,2,1,2,2,1,3,3,3,1,1,1,2],[1,2,2,4,1,2,2,1,3,3,3,2,2,1,2],[1,2,4,2,1,4,4,2,3,3,3,2,2,1,2],[1,2,2,4,1,2,2,1,3,3,3,2,3,1,2],[1,2,2,2,1,2,4,1,1,1,1,1,1,1,1],[1,1,4,2,2,2,2,2,2,2,4,2,4,2,1],[1,1,2,2,1,2,2,4,4,2,1,2,2,2,1],[2,1,1,1,1,1,1,2,2,1,1,4,4,6,1],[2,2,2,2,2,2,1,2,2,2,2,2,2,1,1],[2,2,2,2,2,2,1,1,1,1,1,1,1,1,2]],[[2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,1,2,2,1,1,1,1,1,1,1,1,1,2,2,2,2],[2,1,1,2,2,1,1,2,6,1,2,2,2,1,2,2,2,2],[2,1,2,2,4,1,2,4,2,4,2,2,2,1,1,1,1,2],[2,1,4,2,2,4,2,2,1,2,4,2,4,1,2,2,1,1],[1,1,2,2,4,1,1,2,1,4,2,4,2,2,2,2,2,1],[1,2,2,1,2,2,1,2,1,2,2,2,4,4,4,2,2,1],[1,2,4,2,2,2,2,4,2,2,4,1,1,2,1,1,1,1],[1,2,4,2,4,2,1,4,1,2,2,1,2,2,1,2,2,2],[1,1,2,2,1,1,1,2,2,1,1,1,4,2,1,2,2,2],[2,1,2,2,1,3,3,3,3,2,2,2,2,2,1,2,2,2],[2,1,1,1,1,3,3,3,3,3,3,1,1,1,1,2,2,2],[2,2,2,1,3,3,3,3,1,1,1,1,2,2,2,2,2,2],[2,2,2,1,3,3,3,1,1,2,2,2,2,2,2,2,2,2],[2,2,2,1,3,3,3,1,2,2,2,2,2,2,2,2,2,2],[2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]],[[2,2,2,2,2,2,1,1,1,1,2,2,2],[2,2,1,1,1,1,1,2,2,1,2,2,2],[2,1,1,2,2,2,2,2,4,1,2,2,2],[1,1,2,4,2,2,1,1,2,1,1,1,2],[1,6,4,2,4,2,1,2,4,2,2,1,2],[1,1,1,1,2,1,1,2,2,2,4,1,2],[2,1,3,3,3,3,1,4,2,4,2,1,2],[2,1,3,3,3,3,1,2,2,2,4,1,2],[2,1,3,3,3,3,2,2,4,4,2,1,1],[2,1,3,3,3,2,1,2,4,2,2,2,1],[2,1,1,1,1,1,1,4,2,4,2,2,1],[2,2,2,2,2,2,1,2,2,2,1,1,1],[2,2,2,2,2,2,1,4,2,1,1,1,2],[2,2,2,2,2,2,1,2,2,1,2,2,2],[2,2,2,2,2,2,1,1,1,1,2,2,2]],[[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,2,2,2,2,2,1,1,2,2,1],[1,1,2,2,2,4,2,2,2,4,2,1],[1,1,1,1,2,1,1,2,4,4,2,1],[1,2,2,2,4,2,1,2,2,2,2,1],[1,2,4,4,4,2,1,2,1,1,1,1],[1,2,2,2,1,2,1,2,4,2,1,1],[1,2,2,1,2,2,1,2,2,4,2,1],[1,2,4,1,2,4,1,2,2,2,2,1],[1,2,2,2,3,3,1,2,1,1,1,1],[1,1,1,1,3,3,2,4,2,1,6,1],[1,3,3,3,3,3,1,2,4,1,2,1],[1,1,3,3,3,3,1,2,2,4,2,1],[1,1,1,3,3,1,1,2,2,2,2,1],[1,1,1,1,1,1,1,1,1,1,1,1]],[[1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1],[1,2,2,2,1,2,2,2,2,1,6,1,1,1,1,3,3,3,3,1],[1,2,2,2,4,4,1,2,2,2,2,2,2,2,3,3,3,3,3,1],[1,2,2,2,1,2,1,1,1,2,2,2,1,1,2,3,3,3,3,1],[1,1,2,1,1,2,1,1,1,2,2,1,2,2,2,3,3,3,3,1],[2,1,2,4,2,4,2,2,2,2,2,1,2,1,1,2,1,1,1,1],[2,1,2,2,4,2,4,1,1,2,2,1,2,2,2,2,2,2,2,1],[1,1,1,1,2,1,2,2,1,1,1,1,2,1,1,2,1,1,2,1],[1,2,2,1,2,1,4,2,2,2,1,1,2,1,1,2,2,2,2,1],[1,2,4,2,2,4,2,2,1,2,1,1,2,1,1,1,1,1,1,1],[1,2,1,2,4,2,4,2,2,2,2,1,2,1,2,2,2,2,2,2],[1,2,2,4,2,1,1,2,1,1,2,1,2,1,2,2,2,2,2,2],[1,2,4,4,2,2,2,2,2,4,4,2,2,1,2,2,2,2,2,2],[1,1,2,1,1,2,1,1,1,2,4,2,2,1,2,2,2,2,2,2],[2,1,2,2,2,2,1,2,1,2,2,2,2,1,2,2,2,2,2,2],[2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,2,2,2,2,2]],[[2,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2],[2,2,2,1,1,1,2,2,1,1,2,2,2,2,2,2,2,2],[1,1,1,1,2,2,4,2,2,1,2,2,2,2,2,2,2,2],[1,2,2,2,4,2,4,2,2,1,1,1,1,2,2,2,2,2],[1,2,4,2,2,2,1,2,4,2,2,2,1,2,1,1,1,1],[1,2,2,1,2,2,1,2,2,2,4,2,1,2,1,3,3,1],[1,1,4,1,4,2,1,1,1,1,4,1,1,1,1,3,3,1],[2,1,2,2,2,1,1,1,1,1,2,1,1,2,3,3,3,1],[2,1,4,1,2,1,1,6,1,1,2,1,1,2,2,3,3,1],[2,1,2,1,2,2,2,2,4,2,2,2,2,2,3,3,3,1],[2,1,2,2,2,1,1,1,1,2,1,1,1,2,2,3,3,1],[2,1,1,1,2,1,1,2,1,2,2,1,1,2,3,3,3,1],[2,2,1,1,4,2,1,1,1,1,4,2,1,1,1,3,3,1],[2,2,1,2,2,2,1,1,2,2,2,2,1,2,1,3,3,1],[2,1,1,2,4,4,1,1,2,2,4,2,1,2,1,1,1,1],[2,1,2,2,2,2,2,4,4,4,4,2,1,2,2,2,2,2],[2,1,2,4,2,1,1,1,2,2,2,2,1,2,2,2,2,2],[2,1,2,2,2,1,2,1,1,1,1,1,1,2,2,2,2,2],[2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2]],[[1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2],[1,3,3,3,3,3,3,2,2,2,1,1,1,1,1,1,1,1,1,2,2],[1,3,3,3,3,3,3,2,2,2,1,2,2,1,1,2,2,2,1,2,2],[1,3,3,1,1,1,2,4,2,2,2,2,4,2,2,2,2,2,1,2,2],[1,3,3,3,2,4,2,4,2,1,2,2,1,1,1,2,2,2,1,2,2],[1,3,3,3,1,4,1,1,1,1,1,2,2,2,2,1,2,2,1,2,2],[1,1,1,2,2,2,2,1,2,2,2,1,4,2,2,1,2,4,1,1,1],[2,2,1,2,2,4,4,2,4,2,4,2,2,4,1,1,2,2,4,2,1],[2,2,1,2,2,4,2,2,2,1,4,1,2,2,1,1,2,2,2,2,1],[2,2,1,1,1,2,1,1,2,1,2,2,4,2,1,1,1,1,1,1,1],[2,2,2,1,2,2,4,2,4,2,1,1,2,1,1,2,2,2,2,2,2],[2,2,2,1,2,2,2,2,4,2,2,4,2,2,1,2,2,2,2,2,2],[2,2,2,1,1,2,2,2,1,2,1,2,2,2,1,2,2,2,2,2,2],[2,2,2,2,1,1,1,1,1,6,1,1,1,1,1,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2,2,2,2,2]],[[2,1,1,1,1,1,1,1,1,1,2,2,2,2],[2,1,3,3,3,3,2,2,2,1,1,2,2,2],[2,1,3,1,3,1,2,2,4,2,1,1,2,2],[1,1,3,3,3,3,1,2,1,2,6,1,1,2],[1,2,3,3,3,3,1,2,2,1,2,2,1,1],[1,2,2,2,2,2,1,4,2,1,1,4,2,1],[1,1,2,1,1,1,2,2,4,2,2,2,2,1],[2,1,4,2,2,4,2,4,2,4,1,2,2,1],[2,1,2,1,2,2,4,2,4,2,1,1,2,1],[2,1,2,2,1,1,1,2,2,1,1,2,2,1],[2,1,2,2,2,2,1,1,2,1,1,2,1,1],[2,1,2,2,4,2,1,2,2,4,2,2,1,2],[2,1,1,1,4,2,4,2,2,2,1,1,1,2],[2,2,2,1,2,2,1,1,1,1,1,2,2,2],[2,2,2,1,1,1,1,2,2,2,2,2,2,2]],[[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,3,1,1,1,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,1,3,3,3,3,1,2,2,2,2],[2,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,1,2,2,2,2],[1,1,2,2,2,1,1,2,2,2,2,2,1,1,3,3,3,3,1,1,1,1,1],[1,2,2,4,4,1,1,2,2,4,2,6,1,1,3,3,3,3,2,2,2,2,1],[1,2,2,2,2,2,2,4,4,2,4,1,2,2,3,3,3,3,1,2,2,2,1],[1,2,2,4,2,1,1,2,4,4,2,1,2,1,3,3,3,3,1,2,2,1,1],[1,2,2,4,2,1,1,2,4,2,2,1,2,1,1,2,1,1,1,2,2,1,2],[1,1,2,1,1,1,1,1,2,1,1,1,2,2,2,2,2,2,2,2,2,1,2],[1,1,2,2,2,4,2,2,4,2,1,1,1,1,1,2,1,1,1,2,2,1,2],[1,2,4,1,1,1,2,2,1,2,1,1,1,1,1,2,1,2,1,1,1,1,2],[1,2,2,2,4,2,2,2,1,2,2,2,2,2,2,2,1,2,2,2,2,2,2],[1,2,2,4,2,1,4,2,4,2,4,1,1,1,2,2,1,2,2,2,2,2,2],[1,2,4,4,4,1,2,4,2,2,2,1,2,1,1,1,1,2,2,2,2,2,2],[1,2,2,2,2,1,2,2,4,4,2,1,2,2,2,2,2,2,2,2,2,2,2],[1,1,1,1,1,1,2,2,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2]],[[2,2,2,2,2,2,1,1,1,1,2],[1,1,1,1,1,1,1,2,6,1,2],[1,2,2,2,2,2,4,2,2,1,2],[1,2,2,2,4,1,1,2,4,1,2],[1,1,4,1,3,3,3,1,2,1,2],[2,1,2,4,3,3,3,2,2,1,2],[2,1,2,1,3,2,3,1,2,1,1],[2,1,2,2,2,1,2,1,4,2,1],[2,1,4,2,2,4,2,2,2,2,1],[2,1,2,2,1,1,1,1,1,1,1],[2,1,1,1,1,2,2,2,2,2,2]],[[2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,1,1,2,2,2],[2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,1,2,2,2],[2,2,2,2,2,2,2,2,1,1,2,2,4,4,2,2,1,2,2,2],[2,2,2,2,2,2,2,1,1,2,4,4,2,2,4,2,1,2,2,2],[2,2,2,2,2,2,2,1,2,4,2,2,2,2,4,2,1,2,2,2],[1,1,1,1,2,2,2,1,2,2,2,4,4,2,1,1,1,1,1,2],[1,2,2,1,1,1,1,1,1,1,1,2,1,1,2,2,2,2,1,2],[1,3,3,2,2,2,2,2,2,2,2,2,2,2,4,4,4,6,1,2],[1,3,1,2,1,1,1,1,1,1,1,2,1,1,2,2,2,1,1,2],[1,3,1,2,1,1,1,1,1,1,1,3,2,1,4,2,4,1,1,1],[1,3,3,3,3,3,3,3,3,3,3,3,2,1,2,2,2,4,2,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,4,2,2,1],[2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,1,1,1],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2]],[[2,1,1,1,1,1,1,1,1,2,2,2,2],[2,1,6,1,1,2,2,2,1,1,1,1,2],[2,1,2,4,2,2,2,4,2,2,2,1,2],[2,1,2,2,4,2,4,2,4,4,4,1,2],[2,1,2,4,4,1,2,1,2,2,2,1,2],[1,1,4,2,2,2,2,4,2,2,2,1,2],[1,2,2,4,2,2,4,4,4,4,4,1,1],[1,2,4,1,1,1,1,2,1,2,2,2,1],[1,2,2,4,3,3,3,3,1,2,2,2,1],[1,2,1,1,3,3,3,3,1,4,4,2,1],[1,2,1,1,3,3,3,3,2,2,2,1,1],[1,2,2,2,3,3,3,3,1,2,2,1,2],[1,1,2,1,3,3,3,3,1,4,4,1,2],[2,1,2,1,3,3,3,3,1,2,2,1,2],[2,1,2,2,2,2,2,2,2,2,2,1,2],[2,1,1,1,1,2,1,1,4,1,1,1,2],[2,2,2,2,1,2,2,2,2,1,2,2,2],[2,2,2,2,1,1,1,1,1,1,2,2,2]],[[2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],[2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,1,1],[2,2,2,2,1,2,2,1,2,1,4,4,2,4,2,2,1],[2,2,2,2,1,4,2,1,4,1,2,2,1,1,2,6,1],[2,2,2,1,1,2,1,1,2,1,2,4,2,1,2,1,1],[2,2,2,1,2,2,2,4,2,1,4,2,2,1,2,1,2],[2,2,2,1,2,2,2,1,2,4,2,2,2,1,2,1,2],[2,2,2,1,1,2,4,2,4,2,2,2,1,1,2,1,2],[2,2,2,1,2,2,1,2,2,1,1,2,2,4,2,1,2],[2,2,2,1,2,2,2,2,1,1,2,4,4,1,2,1,2],[1,1,1,1,1,1,4,4,2,2,2,1,2,2,2,1,2],[1,3,3,3,3,1,2,2,1,1,1,1,1,1,1,1,2],[1,3,1,3,3,3,2,1,1,2,2,2,2,2,2,2,2],[1,3,3,3,3,2,2,2,1,2,2,2,2,2,2,2,2],[1,3,3,3,3,2,2,2,1,2,2,2,2,2,2,2,2],[1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2]],[[2,2,2,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,1,1,1,1,1,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,1,2,2,2,1,2,1,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2],[2,2,2,1,2,4,2,1,2,2,4,2,2,2,2,1,1,1,1,1,1,2,2,2,2],[2,2,1,1,4,2,2,1,1,1,2,1,1,2,2,2,2,2,2,2,1,2,2,2,2],[1,1,1,2,2,4,4,2,4,2,4,2,1,2,2,1,1,2,2,2,1,1,1,1,1],[1,2,2,2,2,2,2,2,4,2,2,2,1,1,1,1,1,1,2,1,1,2,2,2,1],[1,2,2,1,1,1,1,1,1,1,1,2,1,6,2,2,2,1,2,1,2,2,1,2,1],[1,1,2,1,1,1,2,2,2,2,2,2,1,1,1,1,2,1,4,1,2,1,2,2,1],[2,1,2,1,1,1,2,1,1,1,1,2,1,1,3,3,2,1,2,2,2,4,2,1,1],[2,1,2,2,4,2,2,4,2,2,1,4,1,1,3,3,2,1,4,1,1,2,2,1,1],[2,1,2,2,1,2,1,2,1,2,2,2,2,2,3,3,1,1,2,1,1,2,4,2,1],[2,1,1,1,1,2,2,2,1,2,1,1,2,1,3,3,1,2,2,2,2,4,2,2,1],[2,2,2,2,1,1,1,1,1,2,2,2,2,1,3,3,1,2,1,2,1,2,2,1,1],[2,2,2,2,2,2,2,2,1,1,1,1,1,1,3,3,1,2,2,2,1,2,1,1,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,1,3,3,1,1,1,1,1,2,2,1,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,1,3,3,2,2,2,2,2,2,2,1,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,1,1,1,2,2,1,1,2],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,2,2]],[[2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2],[2,2,2,2,1,1,1,1,1,2,2,1,2,2,1,1,1,1,2],[2,2,2,2,1,2,2,2,1,2,2,2,4,2,2,2,2,1,2],[2,1,1,1,1,2,1,4,4,2,1,1,2,1,1,2,2,1,2],[1,1,2,2,2,2,2,2,1,2,1,2,2,1,1,2,1,1,1],[1,2,2,1,1,1,2,4,1,4,2,2,4,2,2,4,2,2,1],[1,3,3,3,2,2,2,2,1,2,1,1,2,2,1,2,2,2,1],[1,3,3,3,1,2,2,2,2,6,2,1,2,1,1,1,2,1,1],[1,3,3,3,1,2,2,1,1,1,2,2,4,2,2,4,2,2,1],[1,1,1,1,1,1,1,1,2,1,1,2,2,2,1,2,2,2,1],[2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1]],[[2,2,2,2,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,2,2,2],[2,2,2,2,1,2,2,2,1,1,2,2,1,1,1,1,2,2,1,2,2,2],[2,2,2,2,1,2,2,2,4,2,2,2,1,2,2,4,2,2,1,2,2,2],[2,2,2,2,1,2,2,1,2,1,1,2,1,2,2,2,2,2,1,1,1,1],[2,2,2,2,1,1,2,4,2,2,2,4,2,4,4,1,2,1,2,2,2,1],[2,2,2,2,1,1,1,1,2,2,1,2,2,1,2,4,2,4,2,2,2,1],[1,1,1,1,1,2,2,1,1,1,1,2,2,2,2,1,1,1,3,3,3,1],[1,2,2,2,1,4,2,1,2,2,1,2,1,1,1,1,3,3,3,3,3,1],[1,2,2,2,2,2,2,1,2,2,1,2,1,2,1,1,3,3,3,3,3,1],[1,1,1,1,1,1,2,1,2,2,1,4,2,2,2,1,1,1,3,3,3,1],[2,2,2,1,2,2,2,1,1,2,1,2,4,1,2,2,2,1,3,3,3,1],[2,2,1,1,2,2,2,2,2,2,2,4,2,2,4,1,2,1,1,1,1,1],[2,1,1,2,4,4,4,1,1,2,2,1,2,4,2,2,2,1,2,2,2,2],[2,1,2,2,2,1,2,2,1,2,1,1,1,2,2,1,1,1,2,2,2,2],[2,1,2,2,2,4,2,2,1,4,2,6,1,1,1,1,2,2,2,2,2,2],[2,1,1,1,1,1,2,2,1,2,2,2,1,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2]],[[2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,1,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,1,2,1,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2],[2,1,2,2,2,2,2,2,4,6,1,1,1,1,1,1,2,2,2],[2,1,2,4,2,1,1,4,2,1,1,1,2,2,2,1,2,2,2],[2,1,2,1,1,1,1,2,4,2,2,2,2,4,2,1,2,2,2],[2,1,2,1,1,1,1,1,2,1,2,2,1,4,2,1,1,1,1],[1,1,2,2,1,1,1,1,2,1,1,4,2,2,2,2,2,2,1],[1,2,2,4,1,2,2,4,2,2,1,2,1,1,2,1,1,2,1],[1,2,2,2,2,2,2,2,2,2,1,2,1,3,3,3,1,2,1],[1,1,1,1,1,1,2,2,1,1,1,2,2,3,3,3,2,2,1],[2,2,2,2,2,1,1,1,1,2,1,2,1,3,3,3,1,2,1],[2,2,2,2,2,2,2,2,2,2,1,2,1,1,1,2,1,2,1],[2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,1],[2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1]],[[2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2],[2,2,2,2,2,2,2,1,2,2,1,1,2,2,2,2],[2,2,2,2,2,2,2,1,2,2,2,1,1,2,2,2],[2,2,2,2,2,2,2,1,2,4,4,2,1,1,2,2],[2,2,2,2,2,1,1,1,4,2,2,4,2,1,1,2],[2,2,1,1,1,1,2,2,2,2,4,2,2,2,1,2],[1,1,1,2,2,1,2,1,1,1,1,1,2,2,1,2],[1,2,2,2,2,1,2,1,3,3,3,3,4,2,1,2],[1,2,1,2,2,2,4,2,3,3,3,3,1,2,1,2],[1,2,2,4,2,1,2,1,3,5,3,3,1,2,1,2],[1,1,1,2,2,1,1,1,1,2,1,1,1,2,1,2],[2,2,1,1,1,1,2,6,4,2,2,1,1,4,1,1],[2,2,2,2,2,1,1,1,2,4,2,2,2,2,2,1],[2,2,2,2,2,2,2,1,2,2,1,1,2,2,2,1],[2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1]],[[2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2],[2,2,2,2,2,1,1,3,3,2,2,2,2,1,2,2,2,1,2],[2,2,2,2,1,1,3,3,5,2,4,2,2,2,2,4,2,1,2],[2,2,2,1,1,3,3,5,3,1,2,1,2,1,4,2,1,1,2],[2,2,2,1,3,3,5,3,1,2,1,2,1,2,4,2,2,1,2],[1,1,1,1,3,3,3,1,2,2,1,2,2,2,2,1,2,1,2],[1,2,2,1,1,2,1,2,2,2,2,2,2,2,2,2,2,1,2],[1,2,6,4,2,4,2,1,1,1,2,2,1,2,1,2,1,1,2],[1,2,4,2,2,2,4,2,2,2,1,2,1,2,2,2,1,2,2],[1,1,1,4,4,2,2,2,1,2,1,2,1,2,1,2,1,2,2],[2,2,1,2,2,2,4,2,2,2,1,2,1,2,1,1,1,1,1],[2,2,1,2,4,1,2,1,1,1,1,1,2,2,2,2,2,2,1],[2,2,1,4,2,2,2,1,2,2,2,1,2,2,2,1,2,2,1],[2,2,1,2,2,1,1,1,2,2,2,1,1,2,2,2,2,2,1],[2,2,1,2,2,1,2,2,2,2,2,2,1,2,2,2,2,1,1],[2,2,1,1,1,1,2,2,2,2,2,2,1,1,1,1,1,1,2]],[[2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2],[2,2,2,2,2,1,2,2,2,2,1,1,1,2,2,2,2,1,2,2,2],[2,2,2,2,2,1,2,2,2,2,2,4,2,4,2,2,1,1,1,1,2],[2,2,2,1,1,1,1,2,1,2,2,2,4,2,4,2,2,2,2,1,2],[2,2,1,1,2,4,2,2,1,4,1,1,1,1,2,4,2,4,2,1,2],[1,1,1,2,2,2,1,2,1,2,2,2,1,1,1,2,2,4,2,1,2],[1,2,4,2,2,4,2,2,1,2,2,4,2,2,1,2,1,1,1,1,2],[1,2,1,1,4,1,1,1,1,2,1,4,1,2,2,4,2,2,1,1,1],[1,2,1,1,2,2,1,1,1,2,1,2,1,2,1,2,2,4,2,2,1],[1,2,2,2,2,6,4,2,2,2,4,2,2,2,1,2,4,2,1,2,1],[1,1,1,1,1,2,2,1,2,2,1,1,2,2,1,2,4,1,2,2,1],[2,2,1,3,3,3,2,1,1,1,1,1,4,2,2,1,2,2,1,2,1],[2,2,1,3,3,3,3,3,3,3,1,2,4,4,2,1,4,2,1,2,1],[2,2,1,3,3,3,3,3,3,3,1,2,2,2,2,2,2,2,2,2,1],[2,2,1,3,3,3,3,3,3,3,1,1,1,1,1,1,1,2,2,1,1],[2,2,1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,2]],[[1,1,1,1,1,2,1,1,1,1,2,2,2,2,2,2],[1,3,3,3,1,2,1,2,2,1,1,1,1,2,2,2],[1,3,3,3,1,1,1,2,2,4,2,2,1,2,2,2],[1,3,3,3,3,1,1,2,4,2,2,4,1,1,1,2],[1,1,3,3,3,3,1,1,2,2,2,4,2,2,1,2],[1,1,1,3,3,3,2,1,1,2,4,2,4,2,1,2],[1,2,1,1,2,2,2,2,1,2,2,4,2,2,1,2],[1,2,2,1,1,2,1,2,1,1,1,2,1,1,1,1],[1,2,4,2,1,2,1,4,2,2,4,2,2,2,2,1],[1,2,2,4,2,6,2,4,2,2,2,2,4,2,2,1],[1,2,2,2,1,2,4,2,4,4,2,4,2,1,1,1],[1,2,2,1,1,1,1,1,1,2,2,1,1,1,2,2],[1,2,1,1,2,2,2,2,1,1,1,1,2,2,2,2],[1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2]],[[2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[1,1,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2],[1,2,2,2,2,2,2,2,1,2,1,1,1,1,1,2,2,2,2,2,2],[1,2,4,1,1,1,2,2,1,1,1,2,2,2,1,2,2,2,2,2,2],[1,3,3,1,2,2,4,1,2,1,2,2,1,2,1,2,2,2,2,2,2],[1,3,3,1,2,2,2,2,2,2,4,4,1,2,1,1,1,2,2,2,2],[1,3,5,1,2,1,2,2,1,4,2,4,2,2,2,2,1,1,1,1,1],[1,3,3,1,2,2,1,1,2,2,2,2,2,1,1,4,1,2,2,2,1],[1,3,5,4,2,2,4,2,1,2,1,1,2,2,4,2,2,2,2,2,1],[1,3,3,1,1,2,2,4,2,2,2,1,2,2,2,1,1,1,1,1,1],[1,3,5,1,1,4,1,1,2,2,2,1,1,1,1,1,2,2,2,2,2],[1,3,3,2,2,4,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2],[1,2,2,1,2,6,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2],[1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2]],[[2,2,2,1,1,1,1,1,1,1,1,1,1],[2,2,2,1,2,2,1,1,1,2,2,2,1],[2,2,2,1,2,4,2,2,2,4,2,2,1],[2,2,2,1,2,2,1,1,1,1,4,1,1],[2,2,2,1,1,2,1,2,2,1,2,2,1],[2,2,1,1,2,2,1,3,5,2,2,2,1],[2,2,1,2,2,1,1,3,3,1,2,2,1],[2,2,1,2,6,2,1,3,5,1,2,1,1],[2,2,1,2,1,4,1,3,3,1,4,2,1],[2,2,1,2,4,2,1,3,3,1,2,2,1],[2,2,1,2,1,2,1,5,5,1,2,2,1],[2,2,1,2,4,2,1,3,3,1,4,1,1],[2,2,1,2,2,2,2,3,5,1,2,2,1],[2,1,1,1,2,2,1,2,2,1,2,2,1],[1,1,2,2,2,2,1,1,1,1,2,2,1],[1,2,2,1,1,1,1,1,1,1,4,1,1],[1,2,4,2,2,2,2,2,2,4,2,2,1],[1,2,2,1,1,2,2,2,1,2,2,2,1],[1,1,1,1,1,1,1,1,1,1,1,1,1]],[[2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],[2,1,2,2,2,1,1,2,2,1,2,2,2,1,2,2,2,1,2,2,2,1,2],[2,1,2,4,2,2,2,2,2,4,2,2,2,4,2,2,2,4,2,2,2,1,1],[1,1,1,1,1,2,1,2,2,1,2,2,2,1,1,1,2,1,1,4,1,1,1],[1,2,2,2,1,2,1,1,4,1,1,1,1,1,1,2,2,2,1,2,2,2,1],[1,2,4,2,2,2,1,2,3,3,3,3,3,3,1,2,2,2,1,2,4,2,1],[1,1,2,1,2,2,1,2,3,3,3,3,3,3,1,1,1,1,1,2,2,2,1],[1,1,2,1,1,1,1,1,1,1,1,1,3,3,1,2,2,2,1,2,1,1,1],[1,2,2,2,2,2,2,2,2,2,2,1,3,3,1,2,4,2,2,2,1,2,2],[1,2,1,1,2,1,1,1,2,1,1,1,3,3,1,1,2,1,2,2,1,1,1],[1,2,1,2,2,2,1,2,2,2,1,1,3,3,1,1,2,1,1,1,2,2,1],[1,2,2,2,6,2,2,2,2,2,2,4,3,3,1,2,2,2,2,2,2,2,1],[1,2,1,2,2,2,1,2,2,2,1,1,2,2,1,2,2,2,1,1,2,2,1],[1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1],[1,2,2,2,2,2,2,2,2,2,2,1,2,2,2,1,2,2,2,2,4,2,1],[1,2,4,2,2,1,2,4,2,4,2,4,2,2,2,1,2,1,2,2,2,2,1],[1,2,1,4,1,1,2,4,1,2,2,1,1,2,1,1,2,2,2,2,1,2,1],[1,2,2,4,2,4,4,2,1,1,1,1,2,4,2,2,4,2,1,2,1,2,1],[1,2,2,2,2,2,2,2,2,2,2,1,2,2,2,1,2,2,2,2,2,2,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],[[2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],[1,2,2,2,2,4,2,1,2,2,2,2,2,2,1,1,2,1,2,2,2,1],[1,2,2,1,1,1,1,1,1,2,1,1,1,2,2,1,4,1,1,2,1,1],[1,1,4,1,2,2,2,1,1,4,1,3,3,3,3,2,2,2,1,2,1,2],[1,2,2,1,2,2,2,2,4,2,1,3,3,3,3,1,1,2,1,2,1,2],[1,2,4,2,1,2,1,2,1,2,1,3,3,3,3,1,1,2,2,2,1,2],[1,2,4,2,1,4,4,2,2,2,1,3,3,3,3,1,1,4,1,2,1,2],[1,2,1,2,4,6,4,1,1,4,1,3,3,3,3,1,1,2,2,2,1,2],[1,2,2,2,4,4,4,2,2,2,1,3,3,3,3,1,2,2,2,2,1,2],[1,2,2,4,1,2,2,2,1,2,1,1,1,1,1,1,2,4,1,1,1,2],[1,1,2,2,1,2,1,1,1,4,4,2,2,4,2,2,2,4,2,1,2,2],[1,1,2,2,2,2,2,1,2,4,2,2,4,2,1,1,2,2,2,1,2,2],[2,1,1,1,1,1,2,2,2,1,2,2,2,1,1,1,1,1,1,1,2,2],[2,2,2,2,2,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2]],[[1,1,1,1,1,1,1,1,1,1,2,2,2,2],[1,2,2,2,2,2,2,2,2,1,1,1,1,2],[1,2,1,1,1,1,1,1,2,1,2,2,1,1],[1,2,1,2,4,2,4,2,4,2,2,4,2,1],[1,2,2,2,2,2,2,2,1,4,2,2,2,1],[1,1,1,4,2,2,4,4,1,2,2,1,1,1],[2,2,1,2,2,1,1,2,1,2,4,1,1,2],[2,2,1,1,4,1,2,2,2,4,2,6,1,2],[2,2,2,1,2,2,4,2,4,2,1,1,1,2],[2,2,2,1,2,1,2,2,2,4,2,2,1,2],[2,2,2,1,2,1,1,2,2,2,1,2,1,2],[2,2,1,1,2,2,1,1,1,1,1,2,1,2],[2,2,1,2,2,2,2,2,2,2,2,2,1,2],[2,2,1,3,3,3,3,3,3,3,1,1,1,2],[2,2,1,3,3,3,3,3,3,3,1,2,2,2],[2,2,1,1,1,1,1,1,1,1,1,2,2,2]],[[2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2],[2,1,1,1,1,1,1,1,1,1,2,2,1,1,2,2,2,2],[1,1,2,2,4,2,2,2,2,2,2,4,2,1,1,1,1,1],[1,2,2,2,1,1,2,1,1,2,2,2,1,1,3,3,3,1],[1,2,1,4,4,2,4,2,4,4,1,4,1,1,3,3,3,1],[1,2,1,2,2,2,2,6,2,2,1,2,2,2,3,3,3,1],[1,2,2,4,1,2,1,1,1,4,4,2,2,2,3,3,3,1],[1,2,4,2,2,4,4,2,2,4,2,1,1,3,3,3,3,1],[1,1,1,4,2,2,2,2,2,2,2,1,1,1,1,1,1,1],[2,2,1,2,2,1,1,1,1,1,1,1,2,2,2,2,2,2],[2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2]],[[2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2,1,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,2,1,2,2,1,1,2,1,2,2,1,1,1,1,1,2,2,2],[2,2,2,2,2,2,2,2,2,2,1,2,2,2,5,3,1,3,3,1,2,2,2,1,2,2,2],[2,1,1,1,1,1,2,1,1,1,1,2,4,1,3,1,3,3,3,2,2,2,2,1,2,2,2],[2,1,2,2,2,1,1,1,2,2,1,1,2,1,5,3,3,3,3,1,1,2,1,1,2,2,2],[2,1,2,4,2,2,2,2,2,2,1,1,2,1,3,3,1,3,3,1,1,2,1,2,2,2,2],[1,1,1,1,1,1,2,1,2,2,2,1,2,1,5,3,1,1,1,1,1,2,1,2,2,2,2],[1,2,2,2,1,2,4,1,4,1,2,1,2,1,3,3,1,1,1,1,1,2,1,2,2,2,2],[1,2,4,2,2,4,2,2,2,2,2,1,2,1,5,3,2,2,2,2,1,2,1,2,2,2,2],[1,1,2,1,1,2,2,4,2,1,1,1,2,1,2,2,1,1,2,2,1,2,1,2,2,2,2],[2,1,2,2,4,2,2,4,2,1,1,1,2,1,1,1,1,1,2,1,1,2,1,2,2,2,2],[2,1,1,1,4,1,1,1,4,1,1,1,2,2,1,1,1,1,2,1,1,2,1,2,2,2,2],[1,1,1,1,2,1,2,2,2,2,2,2,2,2,2,1,1,1,2,2,1,2,1,2,2,2,2],[1,2,2,4,2,1,2,2,4,1,1,1,1,2,2,1,1,1,4,4,1,6,1,1,1,1,1],[1,2,2,2,2,2,2,4,2,1,2,1,2,2,1,1,1,1,2,2,1,4,1,2,2,2,1],[1,1,1,1,2,1,2,2,4,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],[2,2,2,1,2,2,4,2,2,1,2,1,1,2,2,1,1,2,2,1,1,1,1,1,1,1,1],[2,2,2,1,1,2,2,1,1,1,2,2,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2],[2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]],[[2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2,1,2,2,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2],[2,2,2,1,1,1,1,1,1,1,2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2],[2,2,2,1,2,2,2,1,2,1,2,1,2,1,2,1,2,2,2,1,1,2,2,2,2,2,2,2,2],[2,2,2,1,2,4,2,2,2,2,2,4,2,2,1,1,2,2,4,2,1,2,2,2,2,2,2,2,2],[2,2,1,1,1,2,4,1,2,1,2,2,1,2,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1],[2,2,1,2,2,4,2,2,1,2,2,4,1,2,1,2,4,4,2,1,2,2,2,1,2,1,2,2,1],[2,1,1,2,1,2,2,2,1,2,2,2,2,2,1,1,1,2,2,2,2,4,2,1,2,1,2,2,1],[2,1,2,2,1,4,2,2,2,1,2,1,1,1,2,2,1,2,2,1,2,4,4,1,2,1,2,2,1],[2,1,2,2,2,2,4,1,1,2,4,2,2,1,2,2,2,1,1,2,4,2,2,1,2,1,2,1,1],[1,1,1,1,4,2,4,2,1,2,2,2,2,1,1,2,2,1,2,2,2,4,2,2,2,2,3,3,1],[1,2,2,1,2,2,2,2,1,1,1,2,1,2,4,2,4,2,1,1,1,2,2,1,1,1,3,5,1],[1,2,2,2,2,2,1,1,2,2,4,4,2,6,2,2,4,2,2,2,2,2,1,1,3,3,3,3,1],[1,2,2,1,1,2,2,1,1,2,2,2,4,2,2,1,4,1,2,2,1,1,3,3,3,3,5,3,1],[1,1,2,1,2,2,4,2,2,1,2,1,2,4,1,1,2,2,1,1,3,3,3,3,5,3,1,1,1],[1,1,2,1,1,2,2,4,2,2,1,2,4,2,1,2,2,1,3,3,3,3,5,3,1,1,1,2,2],[1,2,2,2,2,4,2,1,1,1,1,2,2,2,1,2,3,3,3,3,5,3,1,1,1,2,2,2,2],[1,2,2,2,1,2,2,1,2,2,1,2,2,1,2,2,3,3,5,3,1,1,1,2,2,2,2,2,2],[1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2]],]

MAPPING = {
    0: ' ',
    1: '#',
    2: '.',
    3: 'O',
    4: 'X',
    5: '%',
    6: '@',
    7: 'A'
}


def blank_outside(map):
    flipped = True

    h = len(map)
    w = len(map[0])
    
    while flipped:
        flipped = False

        for y, row in enumerate(map):
            for x, tile in enumerate(row):
                if tile == 2 and (x in [0, w-1] or y in [0, h-1]):
                    map[y][x] = 0
                    flipped = True
                elif tile == 2 and 0 in [map[y-1][x], map[y+1][x], map[y][x-1], map[y][x+1]]:
                    map[y][x] = 0
                    flipped = True
    
    return map


def main():
    for i, map in enumerate(maps):
        map = blank_outside(map)
        with open(f'{i+1:02}.sokolvl', 'w+') as f:
            f.write(';version: 1\n')
            f.write(f';name: {i+1:02}\n\n')

            for row in map:
                for tile in row:
                    f.write(MAPPING[tile])
                f.write('\n')


if __name__ == '__main__':
    main()