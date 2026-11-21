class Solution {
    public int[] findEvenNumbers(int[] digits) {
        int[] freq = new int[10];
        for (int d : digits) freq[d]++;

        List<Integer> list = new ArrayList<>();
        for (int num = 100; num <= 998; num += 2) {
            int d1 = num / 100;
            int d2 = (num / 10) % 10;
            int d3 = num % 10;

            int[] needed = new int[10];
            needed[d1]++;
            needed[d2]++;
            needed[d3]++;

            boolean valid = true;
            for (int i = 0; i < 10; i++) {
                if (needed[i] > freq[i]) {
                    valid = false;
                    break;
                }
            }
            if (valid) list.add(num);
        }

        int[] res = new int[list.size()];
        for (int i = 0; i < list.size(); i++) res[i] = list.get(i);
        return res;
    }
}
