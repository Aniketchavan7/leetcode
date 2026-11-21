class WordDictionary {
    private static class Node {
        Node[] children = new Node[26];
        boolean isEnd = false;
    }

    private final Node root = new Node();

    public WordDictionary() {}

    public void addWord(String word) {
        Node curr = root;
        for (char c : word.toCharArray()) {
            int idx = c - 'a';
            if (curr.children[idx] == null) curr.children[idx] = new Node();
            curr = curr.children[idx];
        }
        curr.isEnd = true;
    }

    public boolean search(String word) {
        return dfs(word, 0, root);
    }

    private boolean dfs(String word, int idx, Node curr) {
        if (curr == null) return false;
        if (idx == word.length()) return curr.isEnd;

        char c = word.charAt(idx);
        if (c == '.') {
            for (Node child : curr.children) {
                if (child != null && dfs(word, idx + 1, child)) {
                    return true;
                }
            }
            return false;
        } else {
            return dfs(word, idx + 1, curr.children[c - 'a']);
        }
    }
}
