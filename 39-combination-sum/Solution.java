class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> res = new ArrayList<>();
        backtrack(candidates, target, 0, new ArrayList<>(), res);
        return res;
    }

    private void backtrack(int[] candidates, int remain, int start, List<Integer> path, List<List<Integer>> res) {
        if (remain == 0) {
            res.add(new ArrayList<>(path));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remain) break; // Prune branch (sorted)
            path.add(candidates[i]);
            backtrack(candidates, remain - candidates[i], i, path, res);
            path.remove(path.size() - 1); // Backtrack
        }
    }
}
