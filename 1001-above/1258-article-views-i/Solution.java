// SQL:
// SELECT DISTINCT author_id AS id 
// FROM Views 
// WHERE author_id = viewer_id 
// ORDER BY id ASC;

class Solution {
    public List<Integer> articleViews(int[][] views) {
        Set<Integer> authors = new TreeSet<>();
        for (int[] v : views) {
            if (v[1] == v[2]) { // author_id == viewer_id
                authors.add(v[1]);
            }
        }
        return new ArrayList<>(authors);
    }
}
