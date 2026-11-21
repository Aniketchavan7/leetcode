// SQL Solution:
// SELECT name 
// FROM Customer 
// WHERE referee_id != 2 OR referee_id IS NULL;

class Solution {
    // Java representation of filtering customers not referred by id=2
    public List<String> findCustomers(int[][] customers, String[] names) {
        List<String> res = new ArrayList<>();
        for (int i = 0; i < customers.length; i++) {
            Integer refereeId = customers[i][1];
            if (refereeId == null || refereeId != 2) {
                res.add(names[i]);
            }
        }
        return res;
    }
}
