public class Solution {
    public bool IsValidSudoku(char[][] board) {
          
          HashSet<char>[] rows=new HashSet<char>[9];
          HashSet<char>[] cols=new HashSet<char>[9];
          HashSet<char>[] boxes=new HashSet<char>[9];

          for (int i=0; i<9; i++){
            rows[i]=new HashSet<char>();
            cols[i]=new HashSet<char>();
            boxes[i]=new HashSet<char>();

          }

          int m=board.Length;
          int n=board[0].Length;

          for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){

                if (board[i][j]=='.'){
                      continue;
                }

                char num=board[i][j];
                int box_id=3*(i/3)+(j/3);

                if (rows[i].Contains(num) || cols[j].Contains(num) || boxes[box_id].Contains(num) ){
                    return false;
                }

                rows[i].Add(num);
                cols[j].Add(num);
                boxes[box_id].Add(num);


            }
          }
          return true;

    }
}
