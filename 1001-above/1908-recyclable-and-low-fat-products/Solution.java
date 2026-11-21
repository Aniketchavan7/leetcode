// SQL:
// SELECT product_id 
// FROM Products 
// WHERE low_fats = 'Y' AND recyclable = 'Y';

class Solution {
    public List<Integer> findProducts(int[] ids, char[] lowFat, char[] recyclable) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < ids.length; i++) {
            if (lowFat[i] == 'Y' && recyclable[i] == 'Y') {
                res.add(ids[i]);
            }
        }
        return res;
    }
}
