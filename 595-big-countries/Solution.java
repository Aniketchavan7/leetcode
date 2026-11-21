// SQL Solution:
// SELECT name, population, area 
// FROM World 
// WHERE area >= 3000000 OR population >= 25000000;

class Solution {
    public List<String[]> findBigCountries(String[][] world) {
        List<String[]> res = new ArrayList<>();
        for (String[] row : world) {
            long area = Long.parseLong(row[1]);
            long pop = Long.parseLong(row[2]);
            if (area >= 3000000 || pop >= 25000000) {
                res.add(new String[]{row[0], row[2], row[1]});
            }
        }
        return res;
    }
}
